import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "24123408"))
    API_HASH = os.environ.get("API_HASH", "31b8525e9486aed13fc6d8cf9473cd4b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6040448297:AAEQ_lG3UbUmjD0ftk50rA0SVrH26-szAm0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RadheRaniMusic_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
