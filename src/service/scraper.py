import time
from playwright.sync_api import sync_playwright

from src.model.bin_day import BinDay
from src.model.bin_collections import BinCollections
from src.util.const import URL
from src.util.wrap import wrap, entering, exiting

iframe_selector = "#fillform-frame-1"


@wrap(entering, exiting)
class Scraper:
    @wrap(entering, exiting)
    def __init__(self, postcode, address, wait):
        self.url = URL
        self.postcode = postcode
        self.address = address
        self.wait = wait

    @wrap(entering, exiting)
    def scrape(self):
        with sync_playwright() as playwright:
            with playwright.chromium.launch() as browser:
                page = browser.new_page()
                page.goto(self.url)

                self.fill_in_postcode(page, iframe_selector, self.postcode)
                self.select_option_with_text(page, iframe_selector, self.address)

                time.sleep(self.wait)

                matches = self.get_all_bin_collections(page)
                return self.extract_bin_collections(matches)

    @wrap(entering, exiting)
    def get_frame_locator(self, page, selector):
        return page.frame_locator(selector)

    @wrap(entering, exiting)
    def fill_in_postcode(self, page, selector, postcode):
        self.get_frame_locator(page, selector).get_by_role("textbox").fill(postcode)

    @wrap(entering, exiting)
    def select_option_with_text(self, page, selector, text):
        option = (
            self.get_frame_locator(page, selector)
            .get_by_role("option", name=text)
            .text_content()
        )
        self.get_frame_locator(page, selector).get_by_role("combobox").select_option(
            option
        )

    @wrap(entering, exiting)
    def get_all_bin_collections(self, page):
        return (
            self.get_frame_locator(page, iframe_selector)
            .locator("div.fieldContent > span > div > center > b")
            .all_inner_texts()
        )

    @wrap(entering, exiting)
    def extract_bin_collections(self, matches):
        collections = BinCollections()
        for collection in matches:
            data = collection.strip().split("\n\n")
            collections.add(BinDay(data[1], data[0]))

        return collections.bin_collections
