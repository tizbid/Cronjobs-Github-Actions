import logging
import logging.handlers
import os
import tweepy

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define a RotatingFileHandler to handle logging output
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",  # File name
    maxBytes=1024 * 1024,  # Maximum size in bytes before rollover
    backupCount=1,  # Number of backup files to keep
    encoding="utf8",  # File encoding
)

# Set the log message format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Attach the log message format to the logger
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

# Attempt to retrieve the required authentication tokens from the environment variables
try:
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN= os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
except KeyError:
    # Log an error message if any of the required environment variables are missing
    logger.info("Authentication failed!")


if __name__ == "__main__":
    
    logger.info("Authentication for Twitter API successful!")
    
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Create API object
    api = tweepy.API(auth)

    # Get the current trending topics for the specified location (here, global)
    trends = api.get_place_trends(id=23424829)


    #Find the maximum tweet volume
    max_tweet_volume = max(trend["tweet_volume"] or 0 for trend in trends[0]["trends"])

    # Loop through the trends and print the name and tweet volume
    for trend in trends[0]["trends"]:
        if trend["tweet_volume"] == max_tweet_volume:
            most_trending_topic = trend["name"]
            
    #Log in the most trending topic
    logger.info(f'Todays trending Twitter Topic in Germany is: {most_trending_topic} with  {max_tweet_volume} tweets')
    
    
    
    
    
