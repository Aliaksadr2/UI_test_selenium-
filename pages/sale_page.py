from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators.sale_page_locator import *


class SalePage(BasePage):
    page_url = '/sale.html'

    def click_women_sale_image(self):
        self.wait_for_element_to_be_clickable(WOMEN_SALE_IMAGE)
        self.find(WOMEN_SALE_IMAGE).click()

    def click_men_sale_image(self):
        self.wait_for_element_to_be_clickable(MEN_SALE_IMAGE)
        self.find(MEN_SALE_IMAGE).click()

    def assert_page_title(self, expected_title):
        title_locator = (
        By.XPATH, f'//span[@class="base" and @data-ui-id="page-title-wrapper" and text()="{expected_title}"]')
        self.wait_for_element_to_be_visible(title_locator)
        page_title = self.find(title_locator)
        assert page_title.is_displayed(), f"ERROR: Element '{expected_title}' does not exist or is not visible."

    def hover_on_training_menu(self):
        training_element = self.wait_for_element_to_be_visible(TRAINING_MENU)
        action = ActionChains(self.driver)
        action.move_to_element(training_element).perform()

    def click_training_option(self):
        self.wait_for_element_to_be_clickable(TRAINING_OPTION)
        self.find(TRAINING_OPTION).click()

    def assert_training_video_is_displayed(self):
        training_video = self.wait_for_element_to_be_visible(TRAINING_VIDEO)
        assert training_video.is_displayed(), "ERROR: The training video file is not displayed on the page."
