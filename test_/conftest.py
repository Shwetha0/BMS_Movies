import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Library.config import Config
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options


# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["Chrome","Edge","Firefox"])
def _driver(request):

    if request.param == "Chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-notification")

        chrome_option.add_argument("--disable-infobars")

        chrome_option.add_argument("start-maximized")

        chrome_option.add_argument("--disable-extensions")

        chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

        chrome_option.add_argument("use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path, options=chrome_option)
    elif request.param == "Firefox":
        option = Options()
        option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(executable_path=Config.Gecko_Driver_Path)

    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

        # options=Options()
        # options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge Beta\Application\msedge.exe'
        # # options = Options()

        # driver= webdriver.Edge(options = options)


    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    #driver.save_screenshot("test_movies.png")
