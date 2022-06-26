from time import mktime
import time
import rpc
import os

client_id = '879374063779336202'
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module

start_time = mktime(time.localtime())

global originalTitle
global imeSajta

originalTitle = ""
imeSajta = ""
logo = ""

while True:

    urlCache = open("url.txt", "r", encoding='utf-8')
    shortUrlCache = open("urlshort.txt", "r", encoding='utf-8')
    titleCache = open("title.txt", "r", encoding='utf-8')
    priceCache = open("price.txt", "r")

    url = urlCache.read()
    shortUrl = shortUrlCache.read()
    title = titleCache.read()
    price = priceCache.read()

    if shortUrl == "www.polovniautomobili.com":
        imeSajta = "Polovni Automobili"
        if title != originalTitle:
            originalTitle = title
        tekst = title
        pare = price
        logo = "logo"
        
    elif shortUrl == "suchen.mobile.de" or shortUrl == "m.mobile.de":
        imeSajta = "mobile.de"
        if title != originalTitle:
            originalTitle = title
        tekst = title
        pare = price
        logo = "mobile"
        
    else:
        tekst = ""
        pare = ""
        
    activity = {
            "state": pare,  # anything you like
            "details": tekst,  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": imeSajta,  # anything you like
                "small_image": logo,  # must match the image key
                "large_text": imeSajta,  # anything you like
                "large_image": logo  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(5)
