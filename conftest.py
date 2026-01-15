import pytest
from selene import Browser, Config
from selenium import webdriver

@pytest.fixture(scope='module')
def browser():
    # Создаём options для Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')

    # Создаём драйвер с опциями
    driver = webdriver.Chrome(options=chrome_options)

    # Создаём Selene Browser
    browser = Browser(Config(driver=driver, base_url='https://demoqa.com'))

    yield browser

    # Закрываем браузер после тестов
    browser.quit()