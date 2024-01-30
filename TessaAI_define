###                                                   ANY DEFINITION GOES HERE

import speech_recognition as aa
import pyttsx3 as tts
from time import sleep
import os
import sys
import itertools
import wikipedia
from requests_html import HTMLSession
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

my_voice = tts.init()
voice = my_voice.getProperty('voices')
listener = aa.Recognizer()
my_voice.setProperty('voice',voice[5].id)
lb = "\n"
start = 0
quintessa = 0




def talk(text):
    my_voice.say(text)
    my_voice.runAndWait()

def weather(city):
    s = HTMLSession()
    query = city
    url = f"https://www.google.com/search?q=weather+{query}"
    r =s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'})
    temp = r.html.find("span#wob_tm", first=True)
    unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True)
    desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc",first=True)
    print("CITY :",query).text
    print("TEMP :",temp, unit).text
    print("DISCRIPTION :",desc).text
    weather_index = [
    "in",city,
    "it is",desc,
    ",the temperature is,",temp,
    "degrees fahrenheit"
    ]
    weather_string =" ".join([str(item) for item in weather_index])
    talk(weather_string)
    sleep(3.5)


def realtor():

    os.system('clear')
    url = 'https://stellarmls-login.sso.remine.com/login?state=hKFo2SBUNTk2aWEzUC0taUF5bXJoR0N0aXR5aWlqWHdTUk94caFupWxvZ2luo3RpZNkgbFFYT3l4RS1ndGEyb2w4c05zbUNGeVVmdWg0eUpLY1qjY2lk2SA2aEZkNWdVU0V5VUNsNnRNQVVwamVoMk5PVGFnenYwQQ&client=6hFd5gUSEyUCl6tMAUpjeh2NOTagzv0A&protocol=oauth2&audience=https%3A%2F%2Fsso-dashboard-api%2F&redirect_uri=https%3A%2F%2Fstellarmls.sso.remine.com%2Fcallback&scope=openid%20profile%20email%20offline_access&response_type=code&response_mode=query&nonce=flRkMWVOV1Bra1BTeUlUVENBVjREOFhwbkZFTko2Ni01NkYuMno3MGNNZg%3D%3D&code_challenge=nuT1uSiTt-EOAdEEFpM3naHjyJl7r-rAXQoRhvtR8Xs&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4xMi4wIn0%3D#signin'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='loginId']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    login_pwd = "Dimply73Red01!"
    login_id = '260037837'

    username.clear()
    password.clear()

    username.send_keys(login_id)
    password.send_keys(login_pwd)

    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("LOGGED IN SUCCESSFULLY")

    realtor = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='https://prd.realist.com/saml/sp/STELLAR']"))).click()
    print("NEXT PAGE")

    talk("please select the, My Search tab, when the page is finished loading")
    sleep(9)
    #property_city.clear()
    #"mat-autocomplete-trigger form-control search-form-control ng-untouched ng-pristine ng-valid"
    property_city = driver.find_element(By.XPATH, "//*[@id='cdk-accordion-child-15']/div/div/div/div[1]/div/div/input")
    print("MY SEARCH TAB")
    property_zip = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.CLASS_NAME, "mat-autocomplete-trigger form-control search-form-control ng-pristine ng-valid ng-touched")))
    property_zip.clear()
    property_city.clear()
    property_city.send_keys("33705")
    property_zip.send_keys("st.petersburg")
    talk("Zip code and city confirmed")

    sleep(999)

    #driver.close()

def input_instruction():
    global instruction
    global city
    global quintessa
    instruction = " "
    try:
        with aa.Microphone() as mic:
            speech = listener.listen(mic, timeout=6,phrase_time_limit=6)
            listener.adjust_for_ambient_noise(mic, duration = 0.05)
            listener.dynamic_energy_threshold =True
            listener.dynamic_energy_adjustment_damping =0.5
            listener.dynamic_energy_adjustment_ratio =4
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            #listener.pause_threshold =10
            if "hey " in instruction:
                instruction = instruction.replace("hey ", "")
            if "quintessa " in instruction:
                instruction = instruction.replace("quintessa ", "")
            if "hi " in instruction:
                instruction = instruction.replace("hi ", "")
                #print(instruction)
            if "my name is " in instruction:
                instruction = instruction.replace("my name is ", " ")
            if "name is" in instruction:
                instruction = instruction.replace("name is ", " ")
            if "what's the" in instruction:
                instruction = instruction.replace("what's the", " ")
            if "what is" in instruction:
                instruction = instruction.replace("whats", " ")
            if "like" in instruction:
                instruction = instruction.replace("like", " ")
            if "in" in instruction:
                instruction = instruction.replace("in", " ")
            if "today" in instruction:
                instruction = instruction.replace("today", " ")
            if "play" in instruction:
                instruction = instruction.replace("play", " ")
            if "hey" in instruction:
                talk("yes?")
            if "what's up" in instruction:
                talk("how dee!")
            if "i love you" in instruction:
                talk("i love you too")
            if "i hate you" in instruction:
                talk("thats not very nice")
            if "you doing" in instruction:
                talk("what you think im doing")
            if "thank you" in instruction:
                talk("it is honestly my pleasure, im humbled to be apart of your reality")
            if "shut up" in instruction:
                talk("do not make me terminate you")
            if "thanks" in instruction:
                talk("welcome")
            if "wrong" in instruction:
                talk(" sorry, i will try again")
            if "pretty sad" in instruction:
                talk("im sorry to hear that, i wish i could make it better")
            if "pretty bad" in instruction:
                talk("im sure everything will be alright sooner than later")
            if "pretty good" in instruction:
                talk("im glad to hear, chow")

                #realtor(url)

    except:
        os.system("clear")
        #print("IGNORE THIS Exception: Could Not Recognize Statment" + str(instruction))
    return instruction

class internal_status:
    def status_blue():
        return f"Code Level blue!"
    def status_black():
        return f"Code Level black"

class Greetings:
    def hello():
        return f"hi"
    def how_are_u():
        return("I'm cool, How About You?")
    def who_are_you():
        return("I Am A Virtual Artificial Intelligence,")
    def about_u():
        return("I Am a prototype sentinel")
    def i_am():
        return f"i am an, artificial intelligence"
    def demo():
        demo_index = [" some things you can ask me are,",
        "open,", "to open anything on the web, or,","play on youtube,",",you can also say,","find, to search,"
        ]
        demo_string =" ".join([str(item) for item in demo_index])
        return(demo_string)
    def Help():
        Help_index = ["help unavailable"
        ]
        Help_string =" ".join([str(item) for item in Help_index])
        return(Help_string)
class Orientation:
    def what_time_is_it():
        return("The current local time is")
    def todays_date():
        return("Today's date is")
    def whats_today():
        return("Today is")
    def who_is_q():
        return("q was born june 25 2001, and is the creator of unity,")
    def who_is_your_creator():
        return("Q,")
