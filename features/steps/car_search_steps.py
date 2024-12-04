import time
from behave import given, when, then
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from features.data.car_input_v4 import registrations
from features.pages.webuypage import we_buy_locators
from features.data.car_output_v4 import vehicle_data

"""In the actual framework common methods such as sendkeys, findelements, click will be moved to basepage
and encapsulated to normal functions and reused. the context.driver will not be visible"""


def accept_cookies(context):
    try:
        cookie_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        cookie_button.click()
        print("Cookies accepted.")
    except Exception as e:
        print(f"Modal window could not be found with: {e}")


@given('the user launches webuyanycar website')
def webuyanycar_page_is_loaded(context):
    """The url data will be inherited from data page"""
    context.driver.get('https://www.webuyanycar.com/')
    accept_cookies(context)
    time.sleep(5)


@when('user searches for car registration fills the details')
def user_searches_for_reg_fill_the_details(context):
    we_buy_any_car_dict = []
    for reg in registrations:
        context.driver.find_element(By.XPATH, we_buy_locators["car_reg_search"]).send_keys(reg)
        print("Searching for car reg: " + reg)
        context.driver.find_element(By.XPATH, we_buy_locators["car_mileage"]).send_keys("15000")
        print("Entered Mileage: 15000")
        time.sleep(3)  # For the user to verify the data has been entered
        context.driver.find_element(By.XPATH, we_buy_locators["valuate_button"]).click()
        time.sleep(5)  # Wait for element can be used instead of static timeout
        # We will only try to get the price and car details if the details are found
        try:
            if context.driver.find_element(By.XPATH, we_buy_locators["manufacturer"]).is_displayed():
                # Grabbing the data for comparison to the output file
                make = context.driver.find_element(By.XPATH, we_buy_locators["manufacturer"]).text
                model = context.driver.find_element(By.XPATH, we_buy_locators["model"]).text
                year = context.driver.find_element(By.XPATH, we_buy_locators["year"]).text
                context.driver.find_element(By.XPATH, we_buy_locators["email"]).clear()
                context.driver.find_element(By.XPATH, we_buy_locators["email"]).send_keys("hello@gmail.com")
                context.driver.find_element(By.XPATH, we_buy_locators["post_code"]).clear()
                context.driver.find_element(By.XPATH, we_buy_locators["post_code"]).send_keys("M71 1UN")
                context.driver.find_element(By.XPATH, we_buy_locators["mobile"]).clear()
                context.driver.find_element(By.XPATH, we_buy_locators["mobile"]).send_keys("07456875855")
                context.driver.find_element(By.XPATH, we_buy_locators["get_my_valuation_button"]).click()
                time.sleep(5)
                car_value = context.driver.find_element(By.XPATH, we_buy_locators["car_value"]).text
                print("The Price of " + reg + " is " + str(car_value))

                car_data = {
                    "VARIANT_REG": reg,
                    "MAKE": make,
                    "MODEL": model,
                    "YEAR": year,
                    "PRICE": car_value
                }
                print(car_data)
                we_buy_any_car_dict.append(car_data)
                context.driver.get('https://www.webuyanycar.com/')
                time.sleep(2)
                context.driver.find_element(By.XPATH, we_buy_locators["value_different"]).click()
                time.sleep(2)
        except NoSuchElementException:
                print("car is not visible")
                car_data = {
                    "VARIANT_REG": reg,
                    "MAKE": "Not Found",
                    "MODEL": "Not Found",
                    "YEAR": "Not Found",
                    "PRICE": 0
                }
                we_buy_any_car_dict.append(car_data)
                context.driver.get('https://www.webuyanycar.com/')
                time.sleep(2)
                context.driver.find_element(By.XPATH, we_buy_locators["value_different"]).click()
                time.sleep(2)
        context.car_details = we_buy_any_car_dict


@then('car details and the price will be retrieved and compared')
def price_details_are_comapred(context):
    print(vehicle_data, context.car_details)
    # vehicle data is the expected output format in file and context.car details is the data scraped from web
    # we are comparing these 2 by reg numbers by looping both dicts and matching reg number
    # The price is stored in dict 2 and not compared. But can be used to verify the price to compare
    for dict1 in vehicle_data:
        variant_reg1 = dict1.get('VARIANT_REG', '').replace(" ", "")
        for dict2 in context.car_details:
            variant_reg2 = dict2.get('VARIANT_REG', '').replace(" ", "")
            # Comparing the data from the output file to the data extracted from website
            if variant_reg1 == variant_reg2:
                for key in dict1:
                    if key in dict2:
                        assert dict1[key] == dict2[key], (
                            f"Assertion Failed: Value for key '{key}' does not match please check the data"
                            f"(VARIANT_REG: '{dict1['VARIANT_REG']}', dict1: '{dict1[key]}', dict2: '{dict2[key]}')"
                        )
