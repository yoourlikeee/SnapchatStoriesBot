import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "10683462"))
    API_HASH = os.environ.get("API_HASH", "8ab812d6e6849bd6352dcb731e44c31e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5680348811:AAE_Q6psuUfYj3HXXYuT_GCKI6v-FJvIBRg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "greymatters_test_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
