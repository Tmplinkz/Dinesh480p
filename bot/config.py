from bot.get_cfg import get_config
class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    # AHCompressBot....
    # sucks Dude
    APP_ID = int(get_config("APP_ID", "22768681"))
    API_HASH = get_config("API_HASH", "07debb70a590c8b06f47a31a6761a28b")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "encoderlog1")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
     # Get these values from my.telegram.org
    AUTH_USERS = set(
        int(x) for x in get_config(
            "AUTH_USERS", "5066042764 6345618689 5090146108 -1002066372404").split()
    )
# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🤣
    # array to store the channel ID who are authorized to use the bot
    # dont u fucking remove this id 😤
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "6696429339:AAHHIUb0tFIrfsEPdWIwuatq6GR6z6V8U1Q")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "Upaxu_bot")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "▣")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "▢")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
