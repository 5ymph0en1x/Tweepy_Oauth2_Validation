import tweepy

# Replace these with your actual credentials from the Twitter Developer Portal
client_id = "xxxxx"
client_secret = "xxxxx"
redirect_uri = "https://localhost"

# Create the OAuth2UserHandler instance
oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=client_id,
    redirect_uri=redirect_uri,
    scope=['tweet.read', 'tweet.write', 'users.read'],
    client_secret=client_secret
)

# Step 1: Generate the authorization URL and prompt the user to visit it
auth_url = oauth2_user_handler.get_authorization_url()
print("Please visit this URL to authorize the application:")
print(auth_url)

# Step 2: Prompt the user to enter the callback URL after authorization
response_url = input("Enter the full callback URL you were redirected to: ")

# Step 3: Fetch the access token using the callback URL
access_token = oauth2_user_handler.fetch_token(response_url)

# Step 4: Create a client and post the tweet
client = tweepy.Client(access_token['access_token'])
response = client.create_tweet(text='hi', user_auth=False)

print("Tweet posted successfully:", response.data)
