from playwright.sync_api import sync_playwright
import time

url = 'https://www.sharklasers.com/compose'

from creds import target, subject, body

user_agent = 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36'


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=10)
    context = browser.new_context(user_agent=user_agent)
    page = context.new_page()
    page.goto(url)
    page.mouse.wheel(0, 400)
    page.click("input[name='to']")
    page.fill("input[name='to']", target)
    time.sleep(1.2)
    page.click("input[name='subject']")
    page.fill("input[name='subject']", subject)
    time.sleep(2)
    page.click("textarea[name='body']")
    page.fill("textarea[name='body']", body)
    time.sleep(1.3)
    page.click("input[type=submit]")
    time.sleep(1.4)

    browser.close()