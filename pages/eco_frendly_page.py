from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from .locators import eco_frendly_page_locators as eco_log


class CategoryPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def open_main_category_men(self):
        main_element = self.wait_for_element_to_be_visible(eco_log.MAIN_CATEGORY)
        action = ActionChains(self.driver)
        action.move_to_element(main_element).perform()

    def select_subcategory(self):
        self.open_main_category_men()
        first_element = self.wait_for_element_to_be_visible(eco_log.SUB_CATEGORY)
        action = ActionChains(self.driver)
        action.move_to_element(first_element).perform()

        second_element = self.wait_for_element_to_be_clickable(eco_log.SUB_SUB_CATEGORY)
        second_element.click()

    def verify_image_is_displayed(self):
        image = self.wait_for_element_to_be_visible(eco_log.PRODUCT_IMAGE)
        assert image.is_displayed(), "ERROR: Expected image is not displayed on the page"

    def sort_products_by_price(self):
        dropdown = self.wait_for_element_to_be_clickable(eco_log.SORT_DROPDOWN)
        dropdown.click()
        select = Select(dropdown)
        select.select_by_value("price")

    def verify_selected_sorting_option(self):
        dropdown = self.wait_for_element_to_be_visible(eco_log.SORT_DROPDOWN)
        select = Select(dropdown)
        selected_option = select.first_selected_option.get_attribute("value")
        assert selected_option == "price", f"ERROR: Expected 'price' option selected, but got '{selected_option}'."

    def select_training_element(self):
        training_element = self.wait_for_element_to_be_visible(eco_log.TRAINING_CATEGORY)
        action = ActionChains(self.driver)
        action.move_to_element(training_element).perform()

    def select_vido_option(self):
        training_option = self.wait_for_element_to_be_visible(eco_log.TRAINING_OPTION)
        training_option.click()

    def verify_training_video_message_is_displayed(self):
        training_video_message = self.wait_for_element_to_be_visible(eco_log.TRAINING_VIDEO_MESSAGE)
        assert training_video_message.is_displayed(), "ERROR: Training video is not visible on the page."
