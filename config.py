# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/tg_bot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "1570274"
    API_HASH = "d463fbcaa44274b3e969028dd570d3ab"
    TOKEN = "1274895087:AAGIvQK7ua9yX4ySMbicsjA-I0oraGf_NjQ"
    OWNER_ID = 992712818  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "OtakuHarsh"
    #RECOMMENDED

    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = -345596805  # needed to make sure 'save from' messages persist
    GBAN_LOGS = -1001250093122
    LOAD = []
    NO_LOAD = ['sed']
    WEBHOOK = False
    URL = None

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    SARDEGNA_USERS = get_user_list('elevated_users.json', 'Sardegnas')
    WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'
    TIME_API_KEY = 'awoo'
    WALL_API = '4714b015a2eb31fab8d3b1849d93574d'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    SPAMMERS = None
    LASTFM_API_KEY = ""
    spamwatch_api = "VxZMFkViTz6vLAzToVAYeK5J7Bx3EGL20z2_GbGLDy3Aa3NLfFmO7wMcfKHKMGSY"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
