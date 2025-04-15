from selenium.webdriver.common.by import By

MAIN_CATEGORY = (By.ID, 'ui-id-5')
SUB_CATEGORY = (By.ID, 'ui-id-17')
SUB_SUB_CATEGORY = (By.ID, 'ui-id-19')

PRODUCT_IMAGE = (
    By.XPATH,
    '//img[@class="product-image-photo" and @src="https://magento.softwaretestingboard.com/pub/media/catalog/'
    'product/cache/7c4c1ed835fbbf2269f24539582c6d44/m/j/mj12-orange_main_1.jpg"]'
)

SORT_DROPDOWN = (By.ID, 'sorter')
PRODUCT_IMAGES = (By.XPATH, '//img[@class="product-image-photo"]')

TRAINING_CATEGORY = (By.ID, 'ui-id-7')
TRAINING_OPTION = (By.ID, 'ui-id-28')
TRAINING_VIDEO_MESSAGE = (By.XPATH, '//div[text()="We can\'t find products matching the selection."]')

NO_PRODUCTS_MESSAGE = (
    By.XPATH,
    '//div[text()="We can\'t find products matching the selection."]'
)


