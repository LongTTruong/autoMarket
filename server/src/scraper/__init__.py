if __name__ == "__main__":
    import asyncio
    from playwright.async_api import async_playwright
    from bs4 import BeautifulSoup as bs

    async def scrape():
        URL = 'https://www.facebook.com/marketplace/112198545462061/electronics'

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            print("Getting content...\n")
            await page.goto(URL)

            content = await page.content()
            soup = bs(content, 'html.parser')

            links = soup.findAll('a')
            for link in links:
                print(f"Link Text: {link.get_text()}, URL: {link['href']}")

            print("Job done!\n")
            await browser.close()

    asyncio.run(scrape())