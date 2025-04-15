from selenium import webdriver
import pytest
from pages.user_login import UserLogin
from pages.sale_page import SalePage
from pages.eco_frendly_page import CategoryPage


@pytest.fixture(scope="function")
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.maximize_window()
    chrom_driver.set_page_load_timeout(220)
    yield chrom_driver
    chrom_driver.quit()


@pytest.fixture()
def login_page(driver):
    return UserLogin(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def category_page(driver):
    return CategoryPage(driver)
