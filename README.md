**What is it?**

Fake that is a simple web service that allows generating a fake user profile for mobile and web testing.

**How can I run it?**

To run, simply build the docker image with a provided Dockerfile and access the service with the following endpoint:

http://"your web address":5000/get_profile/"locale"

for example:

http://my_fake_profile.com:5000/get_profile/en_US

**Sample output:**

`{
    "phone_number": "+6444920079",
    "currency": "NZD ",
    "first_name": "Jose",
    "phone_number_no_prefix": "44920079",
    "last_name": "Smith",
    "address": "",
    "e_mail": "qaustin@dominguez.biz",  
    "credit_card": {
        "credit_card_expire": "11/23",
        "credit_card_provider": "VISA 16 digit",
        "credit_card_number": "5541175655748023"
    }
}`

Currently the following locales are supported:

Currently the following locales are supported:

de_de, en_gb, en_us, en_ca, en_nz, es_es, es_mx, nl_nl,
en_au, fr_fr, he_il, ja_jp, pt_br, in_id, ar_qa, hi_in,
ru_ru, ko_kr, el_gr, ar_sa, dk_dk, fi_fi, nb_no, hr_hr,
mt_mt, sl_si, pt_pt


Supported countries: 
Germany,
UK,
USA,
Canada,
New Zealand,
Singapore,
Spain,
Mexico,
Netherlands,
Australia,
France,
Israel,
japan,
Brazil,
Indonesia,
Qatar,
India,
Russia,
South Korea,
Greece,
Saudi Arabia,
Denmark,
Finland,
Norway,
Croatia,
Malta,
Slovenia,
Portugal

**Any contribution is welcome!!**

