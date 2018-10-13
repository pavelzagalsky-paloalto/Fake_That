FROM python:2.7

ADD app.py /
ADD configuration.py /
ADD fake_profile_builder.py /
ADD phone_num_builder.py /
ADD phone_nums_config.yml /
ADD requirements.txt /


RUN pip install pycountry
RUN pip install Flask
RUN pip install Faker
RUN pip install phonenumbers
RUN pip install PyYAML


CMD [ "python", "./app.py" ]