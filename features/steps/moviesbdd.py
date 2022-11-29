from behave import *
from selenium import webdriver
import time



# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--disable-notification")
# chrome_option.add_argument("--disable-infobars")
# chrome_option.add_argument("start-maximized")
# chrome_option.add_argument("--disable-extensions")
# chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
# chrome_option.add_argument("use-fake-ui-for-media-stream")
# driver = webdriver.Chrome(executable_path=r"C:\Users\Soorya V\Downloads\chromedriver_win32\chromedriver.exe", options=chrome_option)


@given('launch chrome browser')
def launch_browser(context):
    path = r"C:\Users\Soorya V\Downloads\chromedriver_win32\chromedriver.exe"
    context.driver = webdriver.Chrome(path)


@when('Open BookMyShow homepage')
def open_browser(context):
    context.driver.get("https://in.bookmyshow.com")
    context.driver.maximize_window()
    context.driver.implicitly_wait(40)


@then('Choose location')
def choose_loc(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('(//img[@class="sc-fQkuQJ ciyWra"])[3]').click()


@then('Click on Movies button')
def click_movies(context):
    time.sleep(2)
    context.driver.find_element_by_css_selector('a[class = "sc-eKZiaR caGbXw"]').click()


@then('Choose English')
def choose_english(context):
    time.sleep(2)
    context.driver.find_element("xpath", '(//div[text()="English"])[2]').click()


@then('Choose a movie')
def select_movie(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('//img[@alt="Black Panther: Wakanda Forever"]').click()


@then('Click on BookTickets button')
def click_BookTicketsbutton(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('//button[@class="sc-8f9mtj-0 sc-8f9mtj-1 sc-1vmod7e-0 gsJmXR"]').click()


@then('Choose 3D')
def choose_3D(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('(//span[text()="3D"])[1]').click()


@then('Choose date')
def choose_date(context):
    time.sleep(9)
    context.driver.find_element_by_xpath('(//a[@class="date-href"])[3]').click()


@then('Choose showtimings')
def choose_showtimings(context):
    time.sleep(8)
    context.driver.find_element_by_xpath('//a[@data-session-id="68248"]').click()
    time.sleep(3)

@then('Accept Terms and Conditions')
def accept_terms(context):
    time.sleep(6)
    context.driver.find_element_by_xpath('//div[@id="btnPopupAccept"]').click()


@then('Select no of seats')
def select_no_of_seats(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//li[text()="1"]').click()


@then('Click on Selectseats')
def click_selectseat(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//div[@id="proceed-Qty"]').click()


@then('Select desired seat')
def select_desiredseat(context):
    time.sleep(9)
    context.driver.find_element("xpath", '//a[contains(text(),"8")]').click()



@then('Click on Pay button')
def click_pay(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('(//a[@id="btmcntbook"])[1]').click()
    time.sleep(6)


@then('Close browser')
def close_browser(context):
    time.sleep(5)
    context.driver.close()
