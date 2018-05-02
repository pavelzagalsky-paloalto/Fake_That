from flask import Flask, jsonify
from faker import Faker
import phonenumbers
import logging
import os
from random import randint
app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('faker.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
uk_base_phone_num = '+4477001'
us_base_phone_num = '+171840'


def get_phone(locale):
    if 'en_GB' in locale:
        random_num = randint(00000, 99999)
        fake_number = '{}{}'.format(uk_base_phone_num, random_num)
        is_valid = check_validity(fake_number)
        if not is_valid:
            random_num = randint(00000, 99999)
            fake_number = '{}{}'.format(uk_base_phone_num, random_num)
        return fake_number
    elif 'en_US' in locale:
        random_num = randint(00000, 99999)
        fake_number = '{}{}'.format(us_base_phone_num, random_num)
        is_valid = check_validity(fake_number)
        if not is_valid:
            random_num = randint(00000, 99999)
            fake_number = '{}{}'.format(uk_base_phone_num, random_num)
        return fake_number


def check_validity(phone_number):
    parsed_phone_number = phonenumbers.parse(phone_number, None)
    is_valid = phonenumbers.is_valid_number(parsed_phone_number)
    return is_valid


@app.route("/test", methods=['GET', 'POST'])
def test():
    message = 'This is the test route'
    logger.info(message)
    print(message)
    return message


@app.route('/get_profile/<locale>', methods=['GET'])
def get_profile(locale):
    logger.info(locale)
    fake = Faker(locale)
    phone_number = get_phone(locale)
    credit_card_number = fake.credit_card_number()
    credit_card_expire = fake.credit_card_expire()
    credit_card_provider = fake.credit_card_provider()
    currency = fake.currency()
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    profile_list = {
        "phone_number": phone_number,
        "credit_card": {
            "credit_card_number": credit_card_number,
            "credit_card_expire": credit_card_expire,
            "credit_card_provider": credit_card_provider
        },
        "currency": currency,
        "first_name": first_name,
        "last_name": last_name,
        "address": address
    }
    profile_json = jsonify(profile_list)
    return profile_json


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', use_reloader=True, port=port)
