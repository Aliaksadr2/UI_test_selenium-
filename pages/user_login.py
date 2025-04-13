from .base_page import BasePage
from .locators import login_locators as log_loc


class UserLogin(BasePage):
    page_url = '/customer/account/create/'

    def open_registration_page(self):
        self.open_page()

    def fill_login_form(self, first_name, last_name, email, password, confirm_password):
        self.find(log_loc.FIRST_NAME_INPUT).send_keys(first_name)
        self.find(log_loc.LAST_NAME_INPUT).send_keys(last_name)
        self.find(log_loc.EMAIL_INPUT).send_keys(email)
        self.find(log_loc.PASSWORD_INPUT).send_keys(password)
        confirm_password_field = self.find(log_loc.CONFIRM_PASSWORD_INPUT)
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)

    def submit_registration_form(self):
        self.wait_for_element_to_be_clickable(log_loc.CREATE_ACCOUNT_BUTTON)
        self.find(log_loc.CREATE_ACCOUNT_BUTTON).click()

    def verify_confirm_password_error_is_displayed(self):
        self.wait_for_element_to_be_visible(log_loc.CONFIRM_PASSWORD_ERROR)
        confirm_password_error = self.find(log_loc.CONFIRM_PASSWORD_ERROR)
        assert confirm_password_error.is_displayed(), "Error message for confirm password is not displayed"

    def verify_validation_message_is_displayed(self):
        self.wait_for_element_to_be_visible(log_loc.VALIDATION_MESSAGE)
        validation_message = self.find(log_loc.VALIDATION_MESSAGE)
        assert validation_message.is_displayed(), "Validation message is not displayed"