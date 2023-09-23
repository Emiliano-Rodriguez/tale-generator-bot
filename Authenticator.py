import tweepy
import json

######### Twitter Authenticator ##########
#      Authenticates twitter developer application  
#      for twitter bot purposes 
#                              created: 2023_09_23
#########                       

# Twitter Authenticator class, gets keys, tokens and sectrets from json file (shhh keep it a secret)
class TwitterAuthenticator:
    def __init__(self, config_file="auth.json"):
        self.config_file = config_file

        # Try to open and read the authentication json file
        try:
            with open(self.config_file, "r") as file:
                auth_data = json.load(file)
        except FileNotFoundError:
            print(f"Configuration file '{self.config_file}' not found.")
            auth_data = {}
        
        # Initialize instance variables with authentication data from the file or empty strings
        self.consumer_key = auth_data.get("consumer_key", "")
        self.consumer_secret = auth_data.get("consumer_secret", "")
        self.access_token = auth_data.get("access_token", "")
        self.access_token_secret = auth_data.get("access_token_secret", "")
        self.bearer_token = auth_data.get("bearer_token", "")

    # authenticate function creates access to the twitter API V1
    def authenticate(self):
        
        # Create an OAuthHandler and set access tokens
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        
        # Create an API object using the authenticated handler        
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        return api
    
    # Create a Tweepy Client for accessing Twitter API v2
    def create_tweepy_client(self):
        
        client = tweepy.Client(
            self.bearer_token,
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret,
            wait_on_rate_limit=True,
        )

        return client

# Example usage:
if __name__ == "__main__":
    authenticator = TwitterAuthenticator()
    api = authenticator.authenticate()
    client = authenticator.create_tweepy_client()