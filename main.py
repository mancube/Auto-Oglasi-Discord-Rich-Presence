from time import mktime
import time
import rpc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

client_id = '879374063779336202'
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module

time.sleep(2)
start_time = mktime(time.localtime())

global originalTitle

originalTitle = ""

while True:

    urlCache = open("url.txt", "r")
    shortUrlCache = open("urlshort.txt", "r")
    titleCache = open("title.txt", "r")

    url = urlCache.read()
    shortUrl = shortUrlCache.read()
    title = titleCache.read()



    if shortUrl == "www.polovniautomobili.com":

        driver = webdriver.PhantomJS()
        driver.get(url)
        script = 'return document.getElementsByClassName("priceClassified")[0].innerText'
        cena = driver.execute_script(script)
        driver.quit()

        if title != originalTitle:
            originalTitle = title
        tekst = title
        pare = cena
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
                "small_text": "Polovni Automobili",  # anything you like
                "small_image": "logo",  # must match the image key
                "large_text": "Polovni Automobili",  # anything you like
                "large_image": "logo"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(10)

