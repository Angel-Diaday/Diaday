from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class PageTest(LiveServerTestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()

   #def tearDown(self):
      #self.browser.quit()
      
   def test_start_list_and_retrieve_it(self):
      self.browser.get(self.live_server_url)
      self.assertIn('EQKnows', self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h2').text
      self.assertIn('Rescue Form', headerText)

      inpnewAppellations = self.browser.find_element_by_id('first_name')
      inpnewAppellations.send_keys('Angel')
      time.sleep(1)

      inpnewSobriquet = self.browser.find_element_by_id('surname')
      inpnewSobriquet.send_keys('Diaday')
      time.sleep(1)

      inpnewEmplacement = self.browser.find_element_by_id('location')
      inpnewEmplacement.send_keys('Dasmarinas, Cavite')
      time.sleep(1)

      inpnewCallingnumber = self.browser.find_element_by_id('number')
      inpnewCallingnumber.send_keys('639691428480')
      time.sleep(1)

      # inpnewAppointment = self.browser.find_element_by_id('date')
      # inpnewAppointment.send_keys('04--22--2022')
      # time.sleep(1)

      # inpnewTimer = self.browser.find_element_by_id('time')
      # inpnewTimer.send_keys('03:00')
      # time.sleep(1)

      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inpnewAppellations.get_attribute('placeholder'),'Enter your first name here.')
      self.assertEqual(inpnewSobriquet.get_attribute('placeholder'),'Enter your surname here.')
      self.assertEqual(inpnewEmplacement.get_attribute('placeholder'),'Enter your location')
      self.assertEqual(inpnewCallingnumber.get_attribute('placeholder'),'+639-00-000-0000')
      #self.assertEqual(inpnewAppointment.get_attribute('placeholder'),'mm--dd--yyyy')
      # self.assertEqual(inpnewTimer.get_attribute('placeholder'),'00:00')

      # checkbox_disaster1 = self.browser.find_element_by_id('checkbox_disaster1')
      # checkbox_disaster1.click()

      # victim = self.browser.find_element_by_id('victim')
      # victim.send_keys('8')
      # victim.click()

      # checkbox_equipment1 = self.browser.find_element_by_id('checkbox_equipment1')
      # checkbox_equipment1.click()

      btnConfirm.click()
      time.sleep(1)

      inpnewAppellations = self.browser.find_element_by_id('first_name')
      inpnewAppellations.send_keys('Cassandra')
      time.sleep(1)

      inpnewSobriquet = self.browser.find_element_by_id('surname')
      inpnewSobriquet.send_keys('Borromeo')
      time.sleep(1)

      inpnewEmplacement = self.browser.find_element_by_id('location')
      inpnewEmplacement.send_keys('Calamba, Laguna')
      time.sleep(1)

      inpnewCallingnumber = self.browser.find_element_by_id('number')
      inpnewCallingnumber.send_keys('639226148184')
      time.sleep(1)

      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inpnewAppellations.get_attribute('placeholder'),'Enter your first name here.')
      self.assertEqual(inpnewSobriquet.get_attribute('placeholder'),'Enter your surname here.')
      self.assertEqual(inpnewEmplacement.get_attribute('placeholder'),'Enter your location')
      self.assertEqual(inpnewCallingnumber.get_attribute('placeholder'),'+639-00-000-0000')

      btnConfirm.click()
      time.sleep(1)

      table = self.browser.find_element_by_id('reviewTable')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn('1: Diaday, Angel, Dasmarinas, Cavite, 639691428480', [row.text for row in rows])
      self.assertIn('2: Borromeo, Cassandra, Calamba, Laguna, 639226148184', [row.text for row in rows])

      # self.assertTrue(any(row.text == '1: Angel, Diaday, Cavite, 639691428480,04--22--2022, 03:00, Earthquake, 8, Ambulance'), "Wala ka pang table!", )

if __name__ == '__main__':
   unittest.main(warnings='ignore')
