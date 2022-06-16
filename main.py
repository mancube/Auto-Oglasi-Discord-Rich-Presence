from time import mktime
import time
import rpc
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

client_id = '879374063779336202'
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module

time.sleep(2)
start_time = mktime(time.localtime())

options = Options()
options.headless = True

global originalTitle
global imeSajta

originalTitle = ""
imeSajta = ""
logo = ""

while True:

    urlCache = open("url.txt", "r")
    shortUrlCache = open("urlshort.txt", "r")
    titleCache = open("title.txt", "r")

    url = urlCache.read()
    shortUrl = shortUrlCache.read()
    title = titleCache.read()

    if shortUrl == "www.polovniautomobili.com":
        imeSajta = "Polovni Automobili"
        script1 = 'return document.getElementsByClassName("priceClassified")[0].innerText'
        try:
            driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
            driver.get(url) 
            cena = driver.execute_script(script1)
            driver.quit()
        except JavascriptException:
                cena = "~cena ne radi~"
        if title != originalTitle:
            originalTitle = title
        tekst = title
        pare = cena
        logo = "logo"
        
    elif shortUrl == "suchen.mobile.de":
        imeSajta = "mobile.de"
        script2 = 'return document.getElementsByClassName("h3")[1].textContent'
        spliturl = url.split("/")
        
        if spliturl[3] == "fahrzeuge":
            spliturl1 = url.split("&")
            sredjenurl1 = spliturl1[0] 
            driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
            try:
                driver.get(sredjenurl1)
                cena = driver.execute_script(script2)
                driver.quit()
            except JavascriptException:
                cena = "~cena ne radi~"
            
        elif spliturl[3] == "auto-inserat":
            driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
            driver.get(url)
            cena = driver.execute_script(script2)
            driver.quit()
            
        if title != originalTitle:
            originalTitle = title
        tekst = title
        pare = cena
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
    time.sleep(10)
