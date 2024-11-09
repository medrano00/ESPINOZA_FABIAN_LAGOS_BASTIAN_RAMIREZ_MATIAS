from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

########## Credenciales de Testing ##########
username = "TestPC"
nombre = "Testing"
apellido = "PárvuloConnect"
email = "parvuloconnect_test@parvuloconnect.cl"
telefono = "12345678"
password = "Medrano00!"
password2 = "Medrano00!"

########## Credenciales de usuario: Parvularia ##########
usernameParvularia = "blagos"
passwordParvularia = "basti1234"

########## Credenciales de usuario: Apoderado ##########
usernameApoderado = "bvidal"
passwordApoderado = "brandon1234"

# Create your tests here.
class TestParvuloConnect(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()
    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_pc01(self): # Verificar que la página principal funciona correctamente
        self.selenium.get('http://localhost:8000')
        time.sleep(5)

    def test_pc02(self): # Verificar que el registro funciona correctamente
        self.selenium.get('http://localhost:8000')
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/a/i').click()
        time.sleep(5)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/button[2]').click()
        time.sleep(5)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[1]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[1]/input').send_keys(username)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[2]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[2]/input').send_keys(nombre)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[3]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[3]/input').send_keys(apellido)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[4]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[4]/input').send_keys(email)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[5]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[5]/input').send_keys(telefono)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[6]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[6]/input').send_keys(password)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[7]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[7]/input').send_keys(password2)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/div[8]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/button').click()
        time.sleep(5)

    def test_pc03(self): # Verificar que el login funciona correctamente
        self.selenium.get('http://localhost:8000')
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/a/i').click()
        time.sleep(5)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[1]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[1]/input').send_keys(username)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[2]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[2]/input').send_keys(password)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/button[1]').click()
        time.sleep(5)

    def test_pc04(self): # Verificar que el login de parvularia funciona correctamente
        self.selenium.get('http://localhost:8000')
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/a/i').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[1]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[1]/input').send_keys(usernameParvularia)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[2]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[2]/input').send_keys(passwordParvularia)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/button[1]').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/div/a').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/div/div/a[1]').click()
        time.sleep(5)
    
    def test_pc05(self): # Verificar que el login de apoderado funciona correctamente
        self.selenium.get('http://localhost:8000')
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/a/i').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[1]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[1]/input').send_keys(usernameApoderado)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[2]/input').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/p[2]/input').send_keys(passwordApoderado)
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/div/form/button[1]').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/div/a').click()
        time.sleep(2)
        self.selenium.find_element(By.XPATH, '/html/body/div/header/div/div/div/div/a[1]').click()
        time.sleep(5)