from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import unittest
import HtmlTestRunner
import time
import random
import string



dict = {
    0:
        [
            '/html/body/div[5]/div/div[1]/div/a[2]',
            '//*[@id="tbodyid"]/div[1]/div/div/h4/a',
            '//*[@id="tbodyid"]/div[2]/div/div/h4/a'
        ],
    1:
        [
            '/html/body/div[5]/div/div[1]/div/a[3]',
            '//*[@id="tbodyid"]/div[1]/div/div/h4/a',
            '//*[@id="tbodyid"]/div[2]/div/div/h4/a'
        ],
    2:
        [
            '/html/body/div[5]/div/div[1]/div/a[4]',
            '//*[@id="tbodyid"]/div[1]/div/div/h4/a',
            '//*[@id="tbodyid"]/div[2]/div/div/h4/a'
        ]
}

form = ['//*[@id="name"]', '//*[@id="country"]', '//*[@id="city"]', '//*[@id="card"]', '//*[@id="month"]', '//*[@id="year"]']


class TestUntil(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome(r"C:\Users\ianve\Documents\Universidad\8 Semestre\Calidad\Proyecto final calidad\chromedriver.exe")
        self.d.get("https://www.demoblaze.com/index.html")
        self.d.maximize_window()

    def test_a_registrar(self):
        reg = self.d.find_element(By.ID, "signin2")
        reg.click()

        time.sleep(2)
        self.d.find_element(By.XPATH, '//*[@id="sign-username"]').send_keys('Usuario123.')
        self.d.find_element(By.ID, "sign-password").send_keys('Contraseña')

        enter = self.d.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

        time.sleep(2)
        enter.click()

        time.sleep(2)
        Alert(self.d).accept()

    def test_b_ingresar(self):
        log = self.d.find_element(By.ID, "login2")
        log.click()

        time.sleep(2)
        self.d.find_element(By.ID, "loginusername").send_keys('Usuario123')
        self.d.find_element(By.ID, "loginpassword").send_keys('Contraseña')

        enter = self.d.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        
        time.sleep(2)
        enter.click()
        time.sleep(2)

    # def test_c_seleccion(self):
        for i in range(0, len(dict)):
            for j in range(0, len(dict[i])):
                tmp = str(dict[i][j])
                self.d.find_element(By.XPATH, str(dict[i][j])).click()
                time.sleep(5)
                if j > 0:
                    self.d.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a").click()
                    time.sleep(2)
                    Alert(self.d).accept()
                    time.sleep(3)
                    self.d.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
                    time.sleep(5)
                    self.d.find_element(By.XPATH, str(dict[i][0])).click()
                    time.sleep(3)
            time.sleep(5)
        time.sleep(2)
    # def test_d_comprar(self):
        carrito = self.d.find_element(By.ID, 'cartur')
        time.sleep(2)
        carrito.click()
        time.sleep(2)
        self.d.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        for i in range(len(form)):
            tmp = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            print(tmp)
            self.d.find_element(By.XPATH, form[i]).send_keys(tmp)
        self.d.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
        self.d.find_element(By.XPATH, '/html/body/div[10]/div[7]/div/button').click()

    def tearDown(self):
        time.sleep(10)
        self.d.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output'))
