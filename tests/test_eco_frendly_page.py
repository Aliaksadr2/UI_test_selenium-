import pytest


@pytest.mark.smoke
def test_select_option(category_page):
    category_page.open_page()
    category_page.select_subcategory()
    category_page.verify_image_is_displayed()

@pytest.mark.regression
def test_select_sort_price(category_page):
    category_page.open_page()
    category_page.sort_products_by_price()
    category_page.verify_selected_sorting_option()

@pytest.mark.extended
def test_check_training_option(category_page):
    category_page.open_page()
    category_page.select_training_element()
    category_page.select_vido_option()
    category_page.verify_training_video_message_is_displayed()
