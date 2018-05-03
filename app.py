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
uk_prefix = '+44'
uk_header_phone_num = '77001'
uk_base_phone_num = uk_prefix + uk_header_phone_num
us_prefix = '+1'
us_header_phone_num = '71840'
us_base_phone_num = us_prefix + us_header_phone_num
nl_prefix = '+31'
nl_header_phone_num = '6199'
nl_base_phone_num = nl_prefix + nl_header_phone_num
fr_prefix = '+33'
fr_header_phone_num = '6231'
fr_base_phone_num = fr_prefix + fr_header_phone_num


def randomize(header_phone_num, base_phone_num):
    random_num = randint(00000, 99999)
    fake_number = '{}{}'.format(base_phone_num, random_num)
    fake_number_no_prefix = '{}{}'.format(header_phone_num, random_num)
    is_valid = check_validity(fake_number)
    while not is_valid:
        random_num = randint(00000, 99999)
        fake_number = '{}{}'.format(base_phone_num, random_num)
        fake_number_no_prefix = '{}{}'.format(header_phone_num, random_num)
        is_valid = check_validity(fake_number)
    return fake_number, fake_number_no_prefix


def get_phone(locale):
    if 'en_GB' in locale:
        fake_number, fake_number_no_prefix = randomize(uk_header_phone_num, uk_base_phone_num)
        return fake_number, fake_number_no_prefix
    elif 'en_US' in locale:
        fake_number, fake_number_no_prefix = randomize(us_header_phone_num, us_base_phone_num)
        return fake_number, fake_number_no_prefix
    elif 'nl_NL' in locale:
        fake_number, fake_number_no_prefix = randomize(nl_header_phone_num, nl_base_phone_num)
        return fake_number, fake_number_no_prefix
    elif 'fr_FR' in locale:
        fake_number, fake_number_no_prefix = randomize(fr_header_phone_num, fr_base_phone_num)
        return fake_number, fake_number_no_prefix


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
    phone_number, phone_number_no_prefix = get_phone(locale)
    credit_card_number = fake.credit_card_number()
    credit_card_expire = fake.credit_card_expire()
    credit_card_provider = fake.credit_card_provider()
    currency = fake.currency()
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    profile_list = {
        "phone_number": phone_number,
        "phone_number_no_prefix": phone_number_no_prefix,
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
