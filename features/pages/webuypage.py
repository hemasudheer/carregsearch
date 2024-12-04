"""As the tests grow we need to implement Page Object Model so that the code can be re-used using
Inheritance and Polymorphism"""

we_buy_locators = {
    "cookies_accept": "//div[@class='ot-sdk-container']//button[@id='onetrust-accept-btn-handler']",
    "car_reg_search": "//input[@id='vehicleReg']",
    "car_mileage": "//input[@id='Mileage']",
    "valuate_button": "//button[@id='btn-go']",
    "email": "//input[@id='EmailAddress']",
    "post_code": "//input[@id='Postcode']",
    "mobile": "//input[@id='TelephoneNumber']",
    "get_my_valuation_button": "//button[@id='advance-btn']",
    "manufacturer": "/html[1]/body[1]/div[1]/wbac-app[1]/div[1]/div[1]/div[1]/vehicle-questions[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/vehicle-details[1]/div[3]/div[2]/div[1]/div[2]",
    "model": "/html[1]/body[1]/div[1]/wbac-app[1]/div[1]/div[1]/div[1]/vehicle-questions[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/vehicle-details[1]/div[3]/div[2]/div[2]/div[2]",
    "year": "/html[1]/body[1]/div[1]/wbac-app[1]/div[1]/div[1]/div[1]/vehicle-questions[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/vehicle-details[1]/div[3]/div[2]/div[3]/div[2]",
    "colour": "//div[text()='Colour:']/following-sibling::div[contains(@class, 'value')]",
    "car_value": "//div[@class='col-12 col-lg-3 d-none d-sm-block order-1 page-header']//div[@class='d-none d-lg-block']//div[@class='amount']",
    "value_different": "//span[text()=' Value a different car ']",
    "not_found": "//h1[@class='text-focus ng-star-inserted']",
}