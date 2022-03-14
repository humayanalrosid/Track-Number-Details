import re
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

country_code = input("Enter country code : ")
user_number = input("Enter Number : ")

if country_code.isnumeric() and user_number.isnumeric():

    def is_valid(phone_number):
        valid_number = re.compile("(0|91)?[7-9][0-9]{9}")
        return valid_number.match(phone_number)

    phone_number = (f"{user_number}")

    if is_valid(phone_number):
        full_number = (f"+{country_code}{phone_number}")

        phone_details = phonenumbers.parse(full_number)
        print(phone_details)

        time = timezone.time_zones_for_number(phone_details)
        print(time)

        provider = carrier.name_for_number(phone_details, "en")
        print(provider)

        reg_country = geocoder.description_for_number(phone_details, "en")
        print(reg_country)
    else:
        print("Invalid Number")

else:
    print("Enter Numbers only")


