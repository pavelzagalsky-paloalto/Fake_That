Fake that is a simple web service that allows generating a fake user profile for mobile and web testing.

To run, simply build the docker image with a provided Dockerfile and access the service with the following endpoint:

http://<your web address>:5000/get_profile/<locale> 

for example:

http://my_fake_profile.com:5000/get_profile/en_US

Currently the following locales are supported:

de_de, en_gb, en_us, en_ca, en_nz, nl_nl, en_au, fr_fr, he_il, ja_jp.

Any contribution is welcome!!

