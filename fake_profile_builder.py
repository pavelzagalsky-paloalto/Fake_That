from faker import Faker
import os,binascii


class FakeProfile():
    """
    This Class generates a fake profile to be sent per a request with the following parameters:
    address, credit_card: credit_card_expire, credit_card_number,
    currency, e_mail, first_name, last_name, phone_number, phone_number_no_prefix
    """
    def __init__(self, locale, fake_number, fake_number_no_prefix):
        self.locale = locale
        self.fake_number = fake_number
        self.fake_number_no_prefix = fake_number_no_prefix

    def build_fake_profile(self):
        locale_temp = self.locale
        # locale_str = locale_temp.encode("utf-8")
        # locale.setlocale(locale.LC_ALL, locale_str)
        # sym = locale.localeconv()['int_curr_symbol']
        # currency_name = numbers.get_currency_name(sym, locale=locale_str)

        # reverting the original locale to en_US
        original_locale = 'en_US'
        # locale.setlocale(locale.LC_ALL, original_locale)
        try:
            fake = Faker(self.locale)
            address = fake.address()
        except:
            fake = Faker('en_US')
            address = ''
        credit_card_number = fake.credit_card_number()
        credit_card_expire = fake.credit_card_expire()
        credit_card_provider = fake.credit_card_provider()
        first_name = fake.first_name()
        last_name = fake.last_name()
        random_base64 = binascii.b2a_hex(os.urandom(5))
        e_mail = '{}_{}'.format(random_base64, fake.email())
        profile_list = {
            "phone_number": self.fake_number,
            "phone_number_no_prefix": self.fake_number_no_prefix,
            "credit_card": {
                "credit_card_number": credit_card_number,
                "credit_card_expire": credit_card_expire,
                "credit_card_provider": credit_card_provider
            },
            # "currency": currency_name,
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "e_mail": e_mail
        }
        return profile_list

