import re
import os

"""Data input can be achieved in several ways such as from excel file, json format or calling an endpoint and store"""

"""Manually we can add the reg numbers and store in a list. This is good if the data is small and consistent"""

car_regs = [
    "SG18HTN", "AD58VNF", "BW57BOF", "KT17DLX"
]

"""The following way extracts the reg numbers from the file"""


def extract_car_registration_from_file(file_name):
    # Define the regex pattern for the car registration format
    file_path = os.path.join(os.getcwd(), 'features', 'data', file_name)
    pattern = r'\b[A-Z]{2}\d{2} ?[A-Z\d]{3}\b'
    with open(file_path, 'r') as file:
        text = file.read()
    registrations = re.findall(pattern, text)
    return registrations

file_name = 'car_input_v3.py'
registrations = extract_car_registration_from_file(file_name)
"""The function will retrieve ['AD58 VNF', 'BW57 BOW', 'KT17DLX', 'SG18 HTN']"""

"""If there are multiple files we can loop through all the files and add to the variable"""
# file_paths = ['car_1.txt', 'car_2.txt', 'car_3.txt']
# for file in file_paths:
#     all_registrations = []
#     regs = extract_car_registration_from_file(file)
#     all_registrations.append(regs)
