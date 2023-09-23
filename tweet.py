#imports
from Authenticator import TwitterAuthenticator
from TaleGenerator import TalesSelector

######### Twitter Tale Generator ##########
#      Twitter developer application   
#      to generate random tales from various authors
#                              created: 2023_09_23
#      Emiliano Rodriguez
#########                       

# Generate random tales and extract the summary text and image
tales_selector = TalesSelector()
summary_txt, image_file = tales_selector.select_random_tale()

# Twitter authenticator V1/2
auth = TwitterAuthenticator()
api = auth.authenticate()
client = auth.create_tweepy_client()

# Text to be Tweeted
text = summary_txt

# Image to be Tweeted
media_id = api.media_upload(filename=f"img/{image_file}").media_id_string

# Send Tweet with Text and media ID
client.create_tweet(text=text, media_ids=[media_id])
print("Tweeted!")