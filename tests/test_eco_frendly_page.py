from selenium.webdriver.common.by import By

def test_select_option(category_page):
    category_page.open_page()
    category_page.wait_for_element_to_be_visible((By.ID, 'ui-id-5'))
    category_page.select_subcategory()
    category_page.assert_image_is_displayed()

def test_select_sort_price(category_page):
    category_page.open_page()
    category_page.wait_for_element_to_be_visible((By.ID, 'sorter'))
    category_page.sort_by_price()
    category_page.assert_product_image_order()

def test_check_training_option(category_page):
    category_page.open_page()
    category_page.wait_for_element_to_be_visible((By.ID, 'ui-id-7'))
    category_page.select_training_option()
