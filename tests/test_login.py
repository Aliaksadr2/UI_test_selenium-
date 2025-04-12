from selenium.webdriver.common.by import By


def test_login_form_conf_pass_attribute_empty(login_page):
    login_page.open_page()
    login_page.wait_for_element_to_be_visible((By.ID, 'password-confirmation'))
    login_page.fill_login_form('Alex', 'Traf', 'Soulsesiz@rambler.ru', 'Galuzoid@1', '')
    login_page.assert_confirm_password_error_is_displayed()


def test_login_form_first_name_invalid(login_page):
    login_page.open_page()
    login_page.wait_for_element_to_be_visible((By.ID, 'firstname'))
    login_page.fill_login_form('Alex@134', 'Traf', 'Soulsesiz@rambler.ru', 'Galuzoid@1', 'Galuzoid@1')
    login_page.assert_validation_message_is_displayed()


def test_login_form_last_name_invalid(login_page):
    login_page.open_page()
    login_page.wait_for_element_to_be_visible((By.ID, 'lastname'))
    login_page.fill_login_form('Alex', 'Traf@123', 'Soulsesiz@rambler.ru', 'Galuzoid@1', 'Galuzoid@1')
    login_page.assert_validation_message_is_displayed()
