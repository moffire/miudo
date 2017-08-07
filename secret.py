import os, json

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
secret_file = os.path.join(BASE_DIR, 'secret_information.json')
allowed_users = os.uname()[1]

def get_secret_information(argument):

    try:
        with open(secret_file) as f:
            data = json.load(f)
            secret_key = data['SECRET_KEY']
            database_settings = [data['DATABASE']['USER'], data['DATABASE']["PASSWORD"]]
            all_arguments = {
                'SECRET_KEY': secret_key,
                'USER': database_settings[0],
                "PASSWORD": database_settings[1],
            }
            return all_arguments.get(argument)
    except FileNotFoundError:
        return "File with information isn't found"


def debug_mode():
    try:
        with open(secret_file) as f:
            data = json.load(f)
            if allowed_users in data['ALLOWED_USERS']:
                return True
            else:
                return False
    except FileNotFoundError:
        return "File with information isn't found"
