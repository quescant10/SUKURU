###                                              ALL FUNCTIONALITIES GO HERE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
from time import sleep
from bs4 import *
from datetime import *
from tessaAI_define import *

import speech_recognition as aa
import sys
import os
import pywhatkit
import itertools
import logging


cmd = "pipreqs ."
os.system(cmd)

def download():
    cmd = "pip install -r requirements.txt"
    os.system(cmd)

# VARIABLES
lb = "\n"
quintessa = 0
save = 0
tv= 11
sv = 19
shiva = 0
ai = 0
my_voice.setProperty('voice',voice[tv].id)
my_voice.setProperty('rate', 170)
options= webdriver.ChromeOptions()



##### Greetings
Help = Greetings.Help()
demo = Greetings.demo()
hello = Greetings.hello()
how_are_u = Greetings.how_are_u()
who_are_you = Greetings.who_are_you()
about_u = Greetings.about_u()
i_am = Greetings.i_am()
listener = aa.Recognizer()
##### internal status
status_blue = internal_status.status_blue()
status_black = internal_status.status_black()
logging.basicConfig(filename='Tessa_log', encoding='utf-8', level=logging.DEBUG)
logging.info('Hi, INTERNAL STATUS. Operating System Starting')


def weather(city):
    print(city)
    s = HTMLSession()
    query = city
    try:
        url = f"https://www.google.com/search?q=weather+{query}"
        r =s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'})
        temp = r.html.find("span#wob_tm", first=True).text
        unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
        desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc",first=True).text
        print("CITY :",query)
        print("TEMP :",temp, unit)
        print("DISCRIPTION :",desc)
        weather_index = ["in",query,
        "it is",desc,
        ",the temperature is,",temp,"degrees fahrenheit"
        ]
        weather_string =" ".join([str(item) for item in weather_index])
        talk(weather_string)
        sleep(4)
    except:
        talk("no search results for "+weather_string+" yet")
        logging.debug("Weather Search Failed")
        pass

def Search(search):
    search = instruction.replace("open", " ")
    info = wikipedia.summary(search,1)
    try:
        logging.info("SEARCH SUCCESSFUL")
        print("this is what i found about" + search,"from wikipedia")
        print("@ [WIKIPEDIA]")
        print(info)
        talk(info)
    except:
        talk("no search results for "+search+" yet")
        logging.debug("Search Failed")
        pass




def play_yukai():
    global quintessa
    global instruction
    global username
    global shiva
    global ai
    instruction = input_instruction()
    if "shiva" in instruction:
        if shiva ==1:
            ai = 1
            print("Source : ChatGPT")
            messages = [
            {"role": "system", "content": "You are an aware helpful assistant that keeps conversations brief."},
        ]
            while True:

                message = instruction
                if message:
                    messages.append(
                        {"role": "user", "content": message},
                    )
                    chat = openai.chat.completions.create(
                        model="gpt-3.5-turbo", messages=messages
                    )
                reply = chat.choices[0].message.content
                print(f"{reply}")
                talk(f"{reply}")
                messages.append({"role": "assistant", "content": reply})
                logging.warning("chatgpt")
                ai = 0
                sleep(0)

                break
        else:
            talk("oh, no you dont")
    if ai ==0:

        if "on youtube" in instruction:
            try:
                song = instruction.replace("play on youtube", " ")
                talk("playing" + song)
                pywhatkit.playonyt(song)
                logging.info("YOUTUBE SEARCH SELECTED")
            except:
                pass

        if "status" in instruction:
            if quintessa == 1:
                talk(status_black)
            else:
                talk(status_blue)

        if "hello" in instruction:
            talk(hello)

        if "about yourself" in instruction:
                talk(about_u)
        if "who are you"  in instruction:
            if shiva == 1:
                talk("I am unity")
            else:
                talk(who_are_you)
        if "how are you" in instruction:
            talk(how_are_u)
        if "what can you do" in instruction:
            talk(demo)
        if "your name" in instruction:
            if shiva == 1:
                my_voice.setProperty('voice',voice[sv].id)
                talk("Shiva")
            else:
                talk("quintessa, what about you")

        if "my name is" in instruction:
            username = instruction.replace("my name is"," ")
            talk("hi"+username)
        if "what's my name" in instruction:
            if username:
                print(username)
                talk(username)
            else:
                talk("i don't know, tell me your name")
        if "your creator" in instruction:
            talk("Q,")

        if "what time is it" in instruction:
            time = datetime.now().strftime('%I:%M %p')
            talk("The current local time is"+ time)
        if "today's date" in instruction:
            date = datetime.now().strftime('%d /%m /%Y')
            talk("Today's date is"+ date)
            day = datetime.today().strftime('%A')
            talk("Today is" + day)

        if "unity" in instruction:
            if shiva:
                talk("no need")
            logging.info('QUINTESSA EASY ACCESS ACTIVE')
            print("UNITY PASSWORD")
            talk("enter the password on the screen please ")
            password = input('@')
            if password == '369':
                my_voice.setProperty('voice',voice[sv].id)
                sleep(1)
                os.system("clear")
                print("                                                             {{ ADMIN ACCESS GRANTED }}")
                talk("Access granted,")
                sleep(.5)
                os.system("clear")
                shiva = 1
                quintessa = 0
            else:
                os.system("clear")
                my_voice.setProperty('voice',voice[sv].id)
                print("          Access DENIED!")
                talk("Access Denied, fuck up outta hea, mutha foka")
                my_voice.setProperty('voice',voice[tv].id)
                sleep(1)
                os.system("clear")



        if "see you later" in instruction:
            if shiva == 1:
                talk("OK")
                sleep(0)
                my_voice.setProperty('voice',voice[tv].id)
                talk("this is farewell,from quintessa")
                logging.info('QUINTESSA SHUTTING DOWN')
                sys.exit(0)
            else:
                talk("OK, till we meet again")
                sleep(0)
                talk("Goodbye ")
                logging.info('YU-KAI SHUTTING DOWN')
                sys.exit(0)
        if "reboot" in instruction:
            talk("rebooting the operating system")
            print("REBOOTING...")
            sleep(2)
            quintessa = 0
            shiva = 0
            my_voice.setProperty('voice',voice[tv].id)
            os.system("clear")
            sleep(3)
            talk("rebooting process complete, ram erased, how may i help you ")
            logging.error("Error Rebooting")
            logging.warning('Warning error detected rebooting')

        if "help" in instruction:
            logging.info('HELP DETECTED')
            talk(Help)
        if "where am i" in instruction:
            try:
                cmd = "CoreLocationCLI -f%%address"
                os.system(cmd)
                print(cmd)
                talk(cmd)
            except:
                talk("i am not sure, yet")
        if "weather" in instruction:
            city = instruction.replace("weather ", "")
            weather(city)
        if "search" in instruction:
            logging.info("find")
            info=" "
            imfo = instruction.replace("search", " ")
            Search(info)

        if "open" in instruction:
            app = instruction.replace("open ", " ")
            cmd = f"open{app}"
            os.system(cmd)
        
        if "quit" in instruction:
            cmd = instruction.replace("close", "")
            # txt = cmd
            # x = txt.capitalize()
            # print (x)

            # cmd = f"pkill{x}"
            # print(cmd)
            # os.system(cmd)
            talk(f"cant close {cmd}, sorry ")

        if "show me" in instruction:
            logging.info("open")
            Open = instruction.replace("open", " ")
            url = f"https://www.google.com/search?q={Open}"
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            driver.maximize_window()
            options.add_experimental_option("detach", True)

        if "close the window" in instruction:
            cmd = "pkill Google Chrome"
            os.system(cmd)
            talk("sure")

    

    if"" in instruction:
        print(Fore.RED+"Unregistered Command","\n","{",instruction,"}",Fore.GREEN)




os.system(("clear"))
sleep(0.005)
###
###FIRST TIME USERS MUST RUN DOWNLOAD 
###download()
if __name__ == "__main__":
    for i in itertools.count():
        play_yukai()
        auto_log(instruction)
        my_voice.runAndWait()
        logging.info("Run Value: " + str(i))
        sleep(0.0000)
