from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import HTMLTestRunner


class OnlineCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home = 'http://localhost:5000'
        self.options = self.home + '/options'
        self.test_change_mode()

    def test_change_mode(self, mode = 'soap'):
        self.driver.get(self.options)
        form = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'options')))
        form.find_element_by_id(mode).click()
        form.submit()

    def test_home_page_simple_local(self):
        self.test_change_mode('local')
        self.driver.get(self.home)
        calc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calculator')))
        calc.find_element_by_name('2').click()
        calc.find_element_by_name('+').click()
        calc.find_element_by_name('2').click()
        calc.find_element_by_name('=').click()
        time.sleep(3)
        self.assertEquals(calc.find_element_by_id('input').text, '4')

    def test_home_page_simple_soap(self):
        self.test_change_mode('soap')
        self.driver.get(self.home)
        calc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calculator')))
        calc.find_element_by_name('2').click()
        calc.find_element_by_name('+').click()
        calc.find_element_by_name('2').click()
        calc.find_element_by_name('=').click()
        time.sleep(3)
        self.assertEquals(calc.find_element_by_id('input').text, '4')

    def test_home_page_brackets_local(self):
        self.test_change_mode('local')
        self.driver.get(self.home)
        calc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calculator')))
        calc.find_element_by_name('(').click()
        calc.find_element_by_name('8').click()
        calc.find_element_by_name('+').click()
        calc.find_element_by_name('5').click()
        calc.find_element_by_name('*').click()
        calc.find_element_by_name('2').click()
        calc.find_element_by_name(')').click()
        calc.find_element_by_name('/').click()
        calc.find_element_by_name('(').click()
        calc.find_element_by_name('2').click()
        calc.find_element_by_name('*').click()
        calc.find_element_by_name('3').click()
        calc.find_element_by_name('+').click()
        calc.find_element_by_name('1').click()
        calc.find_element_by_name(')').click()
        calc.find_element_by_name('=').click()
        time.sleep(3)
        self.assertEquals(calc.find_element_by_id('input').text, '2')

    def test_home_page_brackets_soap(self):
        self.test_change_mode('soap')
        self.driver.get(self.home)
        calc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calculator')))
        calc.find_element_by_name('(').click()
        calc.find_element_by_name('8').click()
        calc.find_element_by_name('+').click()
        calc.find_element_by_name('5').click()
        calc.find_element_by_name('*').click()
        calc.find_element_by_name('2').click()
        calc.find_element_by_name(')').click()
        calc.find_element_by_name('/').click()
        calc.find_element_by_name('(').click()
        calc.find_element_by_name('2').click()
        calc.find_element_by_name('*').click()
        calc.find_element_by_name('3').click()
        calc.find_element_by_name('+').click()
        calc.find_element_by_name('1').click()
        calc.find_element_by_name(')').click()
        calc.find_element_by_name('=').click()
        time.sleep(3)
        self.assertEquals(calc.find_element_by_id('input').text, '2')

    def test_option_page_save(self):
        self.driver.get(self.options)
        form = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'options')))
        form.submit()
        self.assertEqual("Settings successful saved" in self.driver.page_source, True)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   HTMLTestRunner.main()