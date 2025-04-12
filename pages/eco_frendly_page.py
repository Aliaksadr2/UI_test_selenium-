from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from .locators.eco_frendly_page_locators import *

class CategoryPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def select_subcategory(self):
        main_element = self.wait_for_element_to_be_visible(MAIN_CATEGORY)
        action = ActionChains(self.driver)
        action.move_to_element(main_element).perform()

        first_element = self.wait_for_element_to_be_visible(SUB_CATEGORY)
        action.move_to_element(first_element).perform()

        second_element = self.wait_for_element_to_be_clickable(SUB_SUB_CATEGORY)
        second_element.click()

    def assert_image_is_displayed(self):
        image = self.wait_for_element_to_be_visible(PRODUCT_IMAGE)
        assert image.is_displayed(), "ERROR: Expected image is not displayed on the page"

    def sort_by_price(self):
        sort_dropdown = self.wait_for_element_to_be_clickable(SORT_DROPDOWN)
        sort_dropdown.click()
        select = Select(sort_dropdown)
        select.select_by_value("price")

    def assert_product_image_order(self):
        images = self.find_all(PRODUCT_IMAGES)
        first_image_src = images[0].get_attribute("src")
        assert first_image_src in EXPECTED_FIRST_IMAGE_SRC, \
            f"ERROR: The first image is not as expected. Got '{first_image_src}', expected one of '{EXPECTED_FIRST_IMAGE_SRC}'"

    def select_training_option(self):
        training_element = self.wait_for_element_to_be_clickable(TRAINING_CATEGORY)
        action = ActionChains(self.driver)
        action.move_to_element(training_element).perform()
