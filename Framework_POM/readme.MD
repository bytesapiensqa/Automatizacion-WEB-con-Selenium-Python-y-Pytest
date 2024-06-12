
# Proyecto de Automatización Web con Selenium y Python

Este repositorio contiene un framework de automatización web utilizando Selenium y Python. A continuación, se detallan los pasos para configurar el entorno, ejecutar las pruebas e incluir nuevas pruebas.

## Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)
- Navegador web (Chrome, Firefox, etc.)

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL-del-repositorio>
   cd Framework_POM
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

- `pages/`: Contiene las clases del modelo de página.
- `tests/`: Contiene las pruebas.
- `utils/`: Contiene utilidades y funciones auxiliares.
- `conftest.py`: Configuraciones y fixtures para pytest.
- `pytest.ini`: Archivo de configuración de pytest.
- `requirements.txt`: Lista de dependencias del proyecto.

## Ejecución de Pruebas

Para ejecutar todas las pruebas, utiliza el siguiente comando:
```bash
pytest
```

Si deseas generar un reporte en HTML, usa:
```bash
pytest --html=report.html
```

## Incluir Nuevas Pruebas

1. Crea un nuevo archivo de prueba en el directorio `tests/` con el prefijo `test_`, por ejemplo, `test_nueva_funcionalidad.py`.

2. Dentro de este archivo, define tus casos de prueba utilizando la sintaxis de pytest. Aquí hay un ejemplo básico:
   ```python
   import pytest
   from pages.some_page import SomePage

   def test_nueva_funcionalidad(browser):
       page = SomePage(browser)
       page.some_action()
       assert page.some_result() == "Expected Result"
   ```

3. Asegúrate de que tus pruebas sigan la convención de nombres y estructura para ser detectadas por pytest.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commits descriptivos.
4. Envía tus cambios a tu fork (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request describiendo tus cambios.

## Contacto

Para cualquier duda o consulta, puedes contactarme por WhatsApp o Discord.
