#!/usr/bin/env python3
"""将 HTML 幻灯片截图为 PNG 图片

用法:
    python capture_slides.py [html文件] [输出目录] [清晰度]

参数:
    html文件    默认: index.html
    输出目录    默认: slides
    清晰度      默认: 2 (2=4K, 3=8K)

示例:
    python capture_slides.py index.html slides/     # 基本用法 (4K)
    python capture_slides.py index.html slides/ 1   # 高清 (2K)
    python capture_slides.py index.html slides/ 3   # 超高清 (8K)
"""

import asyncio
from playwright.async_api import async_playwright
import os
import sys

def main():
    HTML_FILE = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    OUTPUT_DIR = sys.argv[2] if len(sys.argv) > 2 else "slides"
    SCALE = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    async def capture_slides():
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page(
                viewport={"width": 1920, "height": 1080},
                device_scale_factor=SCALE
            )

            html_path = os.path.abspath(HTML_FILE)
            await page.goto(f"file://{html_path}")
            await page.wait_for_timeout(1500)  # 等待字体加载

            slide_count = await page.locator(".slide").count()
            print(f"共 {slide_count} 张幻灯片")
            print(f"清晰度: {SCALE}x ({1920*SCALE}x{1080*SCALE})")

            for i in range(slide_count):
                if i > 0:
                    await page.keyboard.press("Space")
                    await page.wait_for_timeout(800)  # 等待动画

                filename = f"{OUTPUT_DIR}/slide-{i+1:02d}.png"
                await page.screenshot(path=filename, full_page=False)
                print(f"已保存: {filename}")

            await browser.close()
            print(f"\n完成! 输出目录: {OUTPUT_DIR}")

    asyncio.run(capture_slides())

if __name__ == "__main__":
    main()
