import time
import pytest
from Data import reading_objects
movies_objects = reading_objects.read_locators()

class Bms_Movies:

    def __init__(self,driver):
        self.driver = driver

    def choose_location(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Location_icon']).click()

    def click_moviesbutton(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['movies_button']).click()

    def choose_English(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Language_filter']).click()

    def choose_movie(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Choosing_movie']).click()

    def click_BookTickets(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Booktickets_button']).click()

    def choose_3D(self):
        time.sleep(6)
        self.driver.find_element(*movies_objects['Languageformat_popup']).click()

    def choose_date(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Choosing_desired_date']).click()

    def choosing_showtimings(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Choosing_showtimings']).click()

    def chooseAccept_termsandconditions(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Terms&conditions_popup']).click()

    def select_no_of_seats(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Choosing_no_of_seats']).click()

    def click_Selectseats(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Click_Selectseats']).click()

    def select_desiredseat(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Choosing_desired_seats']).click()

        # element = self.driver.find_element_by_xpath('//div[@class="wzrk-alert wiz-show-animate"]')
        # if element.is_displayed():
        #     self.driver.find_element_by_xpath('//button[text()="OK"]').click()
        # else:
        #     self.driver.find_element(*movies_objects['Choosing_desired_seats']).click()

    def click_paybutton(self):
        time.sleep(5)
        self.driver.find_element(*movies_objects['Pay_button']).click()

        # element = self.driver.find_element_by_xpath('//div[@class="wzrk-alert wiz-show-animate"]')
        # if element.is_displayed():
        #     self.driver.find_element_by_xpath('//button[text()="OK"]').click()
        # else:
        #     self.driver.find_element(*movies_objects['Pay_button']).click()













