#functions.py
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  
import time
import sys
import pprint

MAIL = "youremail@gmail.com"
PASSWORD = "********"
ARRAY_DEPT = ["Seine-et-Marne", "Seine-Saint-Denis", "Val-d'Oise", "Val-de-Marne", "Yvelines", "Essonne", "Hauts-de-Seine", "Paris"] 
ARRAY_AGE = ['vingtaine', 'trentaine', 'quarantaine']

def connectionAuM(log_errors_string):
        pprint.pprint('start function connectionAuM...\n')
        log_errors_string += 'start function connectionAuM...\n'
        webpage = "https://www.adopteunmec.com/home" # edit me

        driver = webdriver.Chrome(executable_path="/home/linux/Code/python/mon_depot/AdopteUnMecBrowser/chromedriver")
        driver.get(webpage)
        #fill mail
        strLocator = driver.find_element_by_css_selector("input[id='mail']")
        pprint.pprint(strLocator)
        strLocator.send_keys(MAIL)
        #fill psw
        strLocator = driver.find_element_by_css_selector("input[id='password']")
        pprint.pprint(strLocator)
        strLocator.send_keys(PASSWORD)
        #click OK
        strLocator = driver.find_element_by_css_selector("button[type='submit']")
        pprint.pprint(strLocator)
        strLocator.click()
        time.sleep(5)
        
        #do a reasearch
        urlFound = driver.current_url
        pprint.pprint(urlFound)

        for dept in ARRAY_DEPT:
                for age in ARRAY_AGE:
                        driver.get(urlFound)
                        strLocator = driver.find_element_by_css_selector("input[id='input-sentence']")
                        strLocator.send_keys(age + ' ' + dept)
                        time.sleep(5)
                        strLocator = driver.find_element_by_css_selector("button[type='submit']")
                        strLocator.click()
                        time.sleep(5)
                        main_window = driver.current_window_handle 
                        #init first profile if there is
                        profilNumber = 0
                        firstProfile = currentProfile = driver.find_element_by_css_selector("div.someone")
                        stillProfile = False
                        currentIdProfile = None
                        currentLinkProfile = None
                        if(firstProfile != 0):
                                profilNumber+=1
                                stillProfile = True
                                currentLinkProfile = firstProfile.find_element_by_css_selector("h4 a")
                                pprint.pprint(currentLinkProfile)
                        while stillProfile:
                                pprint.pprint("profil n°" + str(profilNumber))
                                currentLinkProfile.send_keys(Keys.CONTROL + Keys.RETURN)
                                time.sleep(5)
                                driver.switch_to_window(driver.window_handles[1])
                                time.sleep(10)
                                driver.close()
                                driver.switch_to_window(main_window)
                                #prepare new profile
                                currentProfile = driver.execute_script("""
                                        return arguments[0].nextElementSibling
                                """, currentProfile)
                                pprint.pprint(currentProfile)
                                if currentProfile != None:
                                        profilNumber+=1
                                        currentLinkProfile = currentProfile.find_element_by_css_selector("h4 a")
                                        pprint.pprint(currentLinkProfile)
                                else:
                                        stillProfile = False

                
                
                                       
                
                
        return
log_errors_string = ""

connectionAuM(log_errors_string)