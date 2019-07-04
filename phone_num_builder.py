from configuration import get_config
from random import randint
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type


class PhoneNum():
    """
    This class generates a valid formatted phone number with and without the prefix.
    It also validates with the phonenumbers library
    """

    def __init__(self, locale):
        prefix_configuration_name = '{}_{}'.format(locale.lower(), 'prefix')
        header_configuration_name = '{}_{}'.format(locale.lower(), 'header')
        self.locale = str(locale)
        try:
            self.prefix = int(get_config(prefix_configuration_name))
            self.header = int(get_config(header_configuration_name))
        except:
            self.prefix = False
            self.header = False

    def randomize(self):
        fake_number, fake_number_no_prefix = randomize_local(prefix=self.prefix, header=self.header)
        if 'False' in fake_number or 'False' in str(fake_number_no_prefix):
            return False
        counter = 0
        while not carrier._is_mobile(number_type(phonenumbers.parse(fake_number))) and counter < 5:
            fake_number, fake_number_no_prefix = randomize_local(prefix=self.prefix, header=self.header)
            counter += 1
            if counter == 5:
                return 0
        return fake_number, fake_number_no_prefix


def randomize_local(prefix, header):
    random_num = randint(00000, 99999)
    base_phone_num = '{}{}'.format(prefix, header)
    fake_number = '+{}{}'.format(base_phone_num, random_num)
    fake_number_no_prefix = int('{}{}'.format(header, random_num))
    return fake_number, fake_number_no_prefix

