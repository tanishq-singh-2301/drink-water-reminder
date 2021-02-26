from discord_webhooks import DiscordWebhooks
import time
from os import environ

#Put your discord webhook url here.

webhook_url = 'WEBHOOK_URL_KEY'

def send_msg():

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_content(title= "Drink Water")
    webhook.send()
    print("Sent message to discord")

def millionsTime():
    while(True):
        send_msg()
        time.sleep(3600)

millionsTime()