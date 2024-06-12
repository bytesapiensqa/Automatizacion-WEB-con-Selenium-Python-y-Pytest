# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Configura tu driver aquí, por ejemplo, Chrome
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Opcional: ejecuta Chrome en modo headless
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         mode = "w" if isinstance(call.excinfo.value, AssertionError) else "a"
#         with open("failures.log", mode) as f:
#             if "driver" in item.fixturenames:
#                 web_driver = item.funcargs["driver"]
#                 screenshot_file = f"{item.name}.png"
#                 web_driver.save_screenshot(screenshot_file)
#                 f.write(f"{item.name} failed. Screenshot saved to {screenshot_file}\n")
