from .base_page import BasePage
from .locators.login_locators import *


class UserLogin(BasePage):
    page_url = '/customer/account/create/'

    def fill_login_form(self, first_name, last_name, email, password, confirm_password):
        self.find(FIRST_NAME_INPUT).send_keys(first_name)
        self.find(LAST_NAME_INPUT).send_keys(last_name)
        self.find(EMAIL_INPUT).send_keys(email)
        self.find(PASSWORD_INPUT).send_keys(password)
        confirm_password_field = self.find(CONFIRM_PASSWORD_INPUT)
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)

        self.wait_for_element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        self.find(CREATE_ACCOUNT_BUTTON).click()

    def assert_confirm_password_error_is_displayed(self):
        self.wait_for_element_to_be_visible(CONFIRM_PASSWORD_ERROR)
        confirm_password_error = self.find(CONFIRM_PASSWORD_ERROR)
        assert confirm_password_error.is_displayed(), "Error message for confirm password is not displayed"

    def assert_validation_message_is_displayed(self):
        self.wait_for_element_to_be_visible(VALIDATION_MESSAGE)
        validation_message = self.find(VALIDATION_MESSAGE)
        assert validation_message.is_displayed(), "Validation message is not displayed"
