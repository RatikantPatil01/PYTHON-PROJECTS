import os
from instagrapi import Client

USERNAME = "iamuser01032002"
PASSWORD = "User@007"
SESSION_FILE = f"{USERNAME}_session.json"
#
cl = Client()
#
# # Handle OTP input only once
def challenge_code_handler(username, choice):
    print(f"OTP sent to: {choice}")
    return input("Enter the OTP sent by Instagram: ")

cl.challenge_code_handler = challenge_code_handler

if os.path.exists(SESSION_FILE):
    print("Loading saved session...")
    cl.load_settings(SESSION_FILE)
    cl.login(USERNAME, PASSWORD)
else:
    print("No session found. Logging in and saving session...")
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)
#
print("Login successful. You can now use the bot without OTP.")
#
# cl.user_follow(USERNAME,'onlyrp01')

# Step 1: Reel URL
# reel_url = "https://www.instagram.com/reel/DJD4oStPRdD/"
#
# # Step 2: Get media ID from URL
# media_id = cl.media_pk_from_url(reel_url)
#
# # Step 3: Download the Reel
# cl.video_download(media_id, folder="./")
# print("Reel downloaded successfully.")
