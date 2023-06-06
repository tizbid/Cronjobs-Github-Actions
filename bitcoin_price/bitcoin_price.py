import logging
import logging.handlers
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    r"C:\Users\tizbi\Desktop\Git-Repos\Cron-job\bitcoin_price\bitcoin_price.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)



if __name__ == "__main__":
    
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    bitcoin_price = data["bitcoin"]["usd"]
    logger.info(f'Bitcoin price is: {bitcoin_price} USD')
  