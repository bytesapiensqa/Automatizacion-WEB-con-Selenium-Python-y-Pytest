# conftest.py
import pytest
from selenium import webdriver
import csv

@pytest.fixture
def driver():
    # Configura tu driver aquí, por ejemplo, Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Opcional: ejecuta Chrome en modo headless
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Pendiente de ver en la clase de pytest del 19/06/2024
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Función para tomar capturas de pantalla en caso de fallo y guardarlas en un archivo de log 
    llamado failures.log en la carpeta screenshots del directorio raíz del proyecto.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        mode = "w" if isinstance(call.excinfo.value, AssertionError) else "a"
        with open("failures.log", mode) as f:
            if "driver" in item.fixturenames:
                web_driver = item.funcargs["driver"]
                screenshot_file = f"screenshots/{item.name}.png"
                web_driver.save_screenshot(screenshot_file)
                f.write(f"{item.name} failed. Screenshot saved to {screenshot_file}\n")