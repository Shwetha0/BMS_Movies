import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


path=r"C:\Users\Soorya V\Downloads\chromedriver_win32\chromedriver.exe"
opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
driver=webdriver.Chrome(path,options=opt)
driver.get("https://in.bookmyshow.com")
driver.maximize_window()
driver.implicitly_wait(40)



# driver.find_element_by_xpath('//span[text()="Bengaluru"]').click()

driver.find_element_by_xpath('(//img[@class="sc-fQkuQJ ciyWra"])[3]').click() #locationpopup
time.sleep(2)
driver.find_element_by_css_selector('a[class = "sc-eKZiaR caGbXw"]').click() #moviesbutton
time.sleep(2)
driver.find_element("xpath", '(//div[text()="English"])[2]').click()  # English from language filter
time.sleep(2)
driver.find_element_by_xpath('//img[@alt="Black Panther: Wakanda Forever"]').click() #Clicking on a movie
time.sleep(6)
driver.find_element_by_xpath('//button[@class="sc-8f9mtj-0 sc-8f9mtj-1 sc-1vmod7e-0 gsJmXR"]').click() #Clicking on Booktickets


time.sleep(6)
driver.find_element_by_xpath('(//span[text()="3D"])[1]').click() #Choosing on 3D on language format
time.sleep(2)
driver.find_element_by_xpath('(//a[@class="date-href"])[3]').click() #Choose desired date

time.sleep(2)
driver.find_element_by_xpath('//a[@data-session-id="68248"]').click() #showtimings
time.sleep(2)
driver.find_element_by_xpath('//div[@id="btnPopupAccept"]').click() #termsandcondition
time.sleep(2)

driver.find_element_by_xpath('//li[text()="1"]').click() #selecting no of seats
time.sleep(2)
driver.find_element_by_xpath('//div[@id="proceed-Qty"]').click() #Selectseats button
time.sleep(2)
element = driver.find_element("xpath", '//a[contains(text(),"8")]')

if element.get_attribute("class") == "_available":
    element.click()
else:
    raise Exception("seat already booked")

time.sleep(2)
driver.find_element_by_xpath('(//a[@id="btmcntbook"])[1]').click() #Click on pay button


