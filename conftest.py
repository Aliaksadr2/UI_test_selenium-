from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Новый импорт
import pytest
from pages.user_login import UserLogin
from pages.sale_page import SalePage
from pages.eco_frendly_page import CategoryPage


# Фикстура для настройки драйвера
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--headless')  # Запуск в фоновом режиме (без графического интерфейса)
    options.add_argument('--disable-gpu')  # Отключение GPU (рекомендуется для стабильности)
    options.add_argument('--no-sandbox')  # Отключить Sandbox (для работы в контейнере Docker)
    options.add_argument('--disable-dev-shm-usage')  # Устраняет проблему с shared memory в Docker

    # WebDriverManager автоматически подбирает и загружает правильный ChromeDriver
    service = Service(ChromeDriverManager().install())
    chrom_driver = webdriver.Chrome(service=service, options=options)

    chrom_driver.maximize_window()
    chrom_driver.set_page_load_timeout(220)

    yield chrom_driver  # Возвращаем драйвер для использования тестами
    chrom_driver.quit()  # Закрываем браузер после завершения теста


# Остальные фикстуры остаются неизменными
@pytest.fixture()
def login_page(driver):
    return UserLogin(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def category_page(driver):
    return CategoryPage(driver)
