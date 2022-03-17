from playwright.sync_api import sync_playwright
import time

url = 'https://www.sharklasers.com/compose'



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(url)
    page.click("input[name='to']")
    page.fill("input[name='to']", target)
    time.sleep(1.2)
    page.click("input[name='subject']")
    page.fill("input[name='subject']", subject)
    time.sleep(2)
    page.click("textarea[name='body']")
    page.fill("textarea[name='body']", body)
    time.sleep(1.3)
    page.click("input[name='send']")

    browser.close()