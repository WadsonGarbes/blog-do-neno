from playwright.sync_api import expect

def test_post_creation(page):
    # GIVEN
    page.goto("http://localhost:5000/posts")

    # WHEN
    hello_p = page.locator(".hello")

    # THEN
    expect(hello_p).to_contain_text("Hello, World!")
