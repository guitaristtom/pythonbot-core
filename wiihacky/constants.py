# File Names
FILE_DEFAULT_CONFIG = 'config.yml'

# Init log strings
LOG_FORMAT_STRING = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
TXT_LOGGER_SUCC = 'successfully initialized logger.'
TXT_REDDIT_SUCC = 'successfully initialized reddit instance.'
TXT_LOGGED_IN = 'logged in to reddit as {}.'
TXT_INTERRUPT = 'ctrl-c interrupt detected.'
TXT_START_BOT = 'starting bot. press ctrl-c to interrupt.'
TXT_CONFIG_LOADED = 'Configuration loaded.'
TXT_DISCORD_INIT = 'Discord has been successfully initialized.'
TXT_DISCORD_SEND_FAILED = 'Failed to send to discord! {} -> {} -> {}'
TXT_DISCORD_DISCON = '{} disconnected from Discord.'
TXT_BOT_READY = \
    '{} is ready, version {}. Praw version {}. Discord.py version {}.'
TXT_BOT_USERS = 'Discord User: {} | Reddit User: {}'
TXT_DISCORD_CONNECT = '{} connected to Discord.'

# Version
__version__ = 'v0.0.2'
VERSION_TEXT = 'wiihacky_version'

# TODO: This currently isn't used, but it's a template for a default, empty
#  config.
DEFAULT_CONFIG = {
    'reddit': {
        'user_agent': 'PutAgentNameHere',
        'client_id': 'PutClientIDHere',
        'client_secret': 'PutClientSecretHere',
        'username': 'PutUserNameHere',
        'password': 'PutPasswordHere',
        'admins': ["ListAdmins", "ByUserName", "Here"]}}
