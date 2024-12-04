from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def before_all(context):
    """Before running any tests this method gets called and initializes browser for testing"""
    """Testing can be run in headless mode where the browser starts invisible mode but tests are run"""
    """To run in headless mode pass the variable headless True or false if nothing passed it will not run in headless"""
    """To pass the parameter it should be passed like behave -D headless=true"""
    """Cross browser Testing can be achieved by having the support of multiple browser drivers"""
    """To change the browser add the argument behave -D browser=chrome"""
    """If browser param is not passed the test will use chrome by default"""

    headless = context.config.userdata.get('headless', 'false').lower() == 'true'
    browser = context.config.userdata.get('browser', 'chrome').lower()

    # Create the options for the browser
    if browser == 'chrome':
        options = Options()
        options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        if headless:
            options.add_argument('--headless')  # Run Chrome in headless mode
            options.add_argument('--disable-gpu')  # Required for headless mode in some systems
        print(f"Running tests with Chrome, headless={headless}")
        context.driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')  # Run Firefox in headless mode
        print(f"Running tests with Firefox, headless={headless}")
        context.driver = webdriver.Firefox(options=options)

    else:
        # This will make sure an exception raised if invalid value is passed
        raise ValueError(f"Unsupported browser: {browser}")

    context.driver.maximize_window()  # This will maximise the window


def after_all(context):
    """This function will quit the WebDriver after all tests."""
    context.driver.quit()
    print("Browser WebDriver closed")
