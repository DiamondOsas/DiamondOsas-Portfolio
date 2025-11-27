from playwright.sync_api import Page, expect, sync_playwright

def verify_portfolio(page: Page):
    # Go to local dev server (default Astro port is 4321)
    page.goto("http://localhost:4321")

    # Wait for content to load
    page.wait_for_selector("h1")

    # Verify Name (First instance in Hero)
    expect(page.get_by_role("heading", name="I'm Diamond Osazuwa").locator("span")).to_be_visible()

    # Verify Dark Theme (Background color check)
    # Get the background color of the body
    bg_color = page.evaluate("getComputedStyle(document.body).backgroundColor")
    print(f"Body background color: {bg_color}")
    # rgb(11, 17, 32) corresponds to #0B1120
    assert bg_color == "rgb(11, 17, 32)"

    # Verify Social Icons
    # Discord title (using .first() because it appears in Hero and Footer)
    expect(page.locator("a[title*='Discord']").first).to_be_visible()
    # Telegram label (using .first() because it appears in Hero and Footer)
    expect(page.locator("a[aria-label='Telegram']").first).to_be_visible()

    # Screenshot
    page.screenshot(path="/app/verification/portfolio_dark_theme.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_portfolio(page)
        finally:
            browser.close()
