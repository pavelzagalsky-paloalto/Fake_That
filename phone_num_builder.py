from configuration import get_config
from random import randint
import phonenumbers


class PhoneNum():
    """
    This class generates a valid formatted phone number with and without the prefix.
    It also validates with the phonenumbers library
    """

    def __init__(self, locale):
        prefix_configuration_name = '{}_{}'.format(locale.lower(), 'prefix')
        header_configuration_name = '{}_{}'.format(locale.lower(), 'header')
        self.locale = locale
        try:
            self.prefix = str(get_config(prefix_configuration_name))
            self.header = str(get_config(header_configuration_name))
        except:
            self.prefix = False
            self.header = False

    def randomize(self):
        fake_number, fake_number_no_prefix = randomize_local(prefix=self.prefix, header=self.header)
        if 'False' in fake_number or 'False' in fake_number_no_prefix:
            return False
        while not check_validity(fake_number):
            fake_number, fake_number_no_prefix = randomize_local(prefix=self.prefix, header=self.header)
        return fake_number, fake_number_no_prefix


def randomize_local(prefix, header):
    random_num = randint(00000, 99999)
    base_phone_num = '{}{}'.format(prefix, header)
    fake_number = '+{}{}'.format(base_phone_num, random_num)
    fake_number_no_prefix = '{}{}'.format(header, random_num)
    return fake_number, fake_number_no_prefix


def check_validity(fake_number):
    parsed_phone_number = phonenumbers.parse(fake_number, None)
    is_valid = phonenumbers.is_valid_number(parsed_phone_number)
    return is_valid
