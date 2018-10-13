from flask import Flask, Response
import json
import logging
import os

from phone_num_builder import PhoneNum
from fake_profile_builder import FakeProfile

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('faker.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


app = Flask(__name__)


@app.route("/test", methods=['GET', 'POST'])
def test():
    message = 'This is a test route'
    logger.info(message)
    message_json = json.dumps(message)
    return Response(message_json, status=200, mimetype='application/json')


@app.route('/get_profile/<locale>', methods=['GET'])
def get_profile(locale):
    locale_error_message = '{} {}'.format(locale, 'is an unsupported locale')
    fail_response = json.dumps({"status": locale_error_message})

    logger.info('{} {} {}'.format('A request for', locale, 'locale was received'))
    # Generating random phone.
    rand_phone_obj = PhoneNum(locale)
    try:
        fake_number, fake_number_no_prefix = rand_phone_obj.randomize()
        logger.info('{} {}'.format(fake_number, 'number was generated'))
    except:
        return Response(fail_response, status=400, mimetype='application/json')

    # Generating fake profile.
    fake_profile_obj = FakeProfile(locale, fake_number, fake_number_no_prefix)
    profile_dict = fake_profile_obj.build_fake_profile()
    profile_json = json.dumps(profile_dict)
    logger.info('{} {}'.format('The served jsoned profile was', profile_json))
    return Response(profile_json, status=200, mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', use_reloader=True, port=port)

