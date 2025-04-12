from selenium.webdriver.common.by import By


def test_click_women_sale_image(sale_page):
    sale_page.open_page()
    sale_page.wait_for_element_to_be_clickable(
        (By.XPATH, '//img[@src="https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-main.jpg"]'))
    sale_page.click_women_sale_image()
    sale_page.assert_page_title("Women Sale")


def test_click_men_sale_image(sale_page):
    sale_page.open_page()
    sale_page.wait_for_element_to_be_clickable(
        (By.XPATH, '//img[@src="https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-mens.jpg"]'))
    sale_page.click_men_sale_image()
    sale_page.assert_page_title("Men Sale")


def test_training_video_displayed(sale_page):
    sale_page.open_page()
    sale_page.wait_for_element_to_be_visible((By.ID, 'ui-id-7'))
    sale_page.hover_on_training_menu()
    sale_page.wait_for_element_to_be_clickable((By.ID, 'ui-id-7'))
    sale_page.click_training_option()
    sale_page.assert_training_video_is_displayed()
