from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    """
    Clase que contiene los elementos de la página de login
    """
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    @property
    def __input_username(self):
        return self.driver.find_element(By.ID, "user-name")
    
    @property
    def __input_password(self):
        return self.driver.find_element(By.ID, "password") 
    
    @property
    def __button_login(self):
        return self.driver.find_element(By.ID, "login-button")
    
    @property
    def __h3_mensajeError(self):
        return self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']//h3")
    
    def login_completo(self, username, password):
        """
        Método que se encarga de realizar el login completo
        Args:
        username: nombre de usuario
        password: contraseña
        """
        self.__input_username.send_keys(username)
        self.__input_password.send_keys(password)
        self.__button_login.click()
        
    
    def obtener_mensaje_error(self):
        """
        Método que se encarga de obtener el mensaje de error
        Return: mensaje de error
        """
        return self.__h3_mensajeError.text

    def get_title(self):
        """
        Función para obtener el título de la página
        """
        title = self.driver.title
        print(f"The title of the page is: {title}")
        return title

    def test_get_title(self):
        """
        Función para probar el método get_title
        """
        expected_title = "Titulo incorrecto para que falle" # El titulo deberia ser Swags Labs
        actual_title = self.get_title()
        assert actual_title == expected_title, f"Title mismatch. Expected: {expected_title}, Actual: {actual_title}"
        print("Title test passed successfully!")

    
    def is_logged_in(self):
        """
        Función para verificar si el usuario está loggeado
        """
        return "inventory.html" in self.driver.current_url