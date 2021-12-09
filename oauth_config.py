#Sets up environmental variables
import os
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token' 
callback_url = 'https://final-s7366uagdq-uw.a.run.app/callback'
