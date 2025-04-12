from selenium.webdriver.common.by import By

FIRST_NAME_INPUT = (By.ID, 'firstname')
LAST_NAME_INPUT = (By.ID, 'lastname')
EMAIL_INPUT = (By.ID, 'email_address')
PASSWORD_INPUT = (By.ID, 'password')
CONFIRM_PASSWORD_INPUT = (By.ID, 'password-confirmation')
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[span[text()='Create an Account']]")
CONFIRM_PASSWORD_ERROR = (By.ID, 'password-confirmation-error')
VALIDATION_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
