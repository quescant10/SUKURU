###                                              ALL FUNCTIONALITIES GO HERE


import speech_recognition as aa
import pyttsx3 as tts
import pandas as pd
from colorama import Fore, Back, Style
from time import sleep
from bs4 import *
from datetime import *
from tessaAI_define import *
import calendar
import sys
import os
import pywhatkit
import itertools
import logging

# VARIABLES
lb = "\n"
LOLA = 1
quintessa = 0
save = 0
txt = 1
my_voice.setProperty('voice',voice[5].id)

##### Greetings
Help = Greetings.Help()
demo = Greetings.demo()
hello = Greetings.hello()
how_are_u = Greetings.how_are_u()
who_are_you = Greetings.who_are_you()
about_u = Greetings.about_u()
i_am = Greetings.i_am()
listener = aa.Recognizer()
##### Orientatio
who_is_q = Orientation.who_is_q()
who_is_your_creator = Orientation.who_is_your_creator()
what_time_is_it = Orientation.what_time_is_it()
todays_date = Orientation.todays_date()
whats_today = Orientation.whats_today()
##### internal status
status_blue = internal_status.status_blue()
status_black = internal_status.status_black()
logging.basicConfig(filename='LOLA_log', encoding='utf-8', level=logging.DEBUG)
logging.info('Hi, INTERNAL STATUS. Operating System Starting')



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


start = 0
session = 0
username = None
singularity = 0
def start():
    global start
    global txt
    global session
    global instruction
    instruction = input_instruction()
    os.system(("clear"))


    talk("How may i help you")
    sleep(0.005)

###### ABOUT ME
def play_yukai():
    global LOLA
    global quintessa
    global session
    global instruction
    global city
    global username
    global singularity
    instruction = input_instruction()
    if quintessa == 1:
        print(Fore.YELLOW+"                                                                   ♦🤖♦"," ~ [quintessa]")
        my_voice.setProperty('voice',voice[5].id)
    if singularity == 1:
        my_voice.setProperty('voice',voice[19].id)
        print(Fore.RED+"                                                                     ~ [unity]"," ♠  👩‍🚀  ♠",Style.RESET_ALL)
#######                                                                  BASICS / DO SOMETHING/
    if " " in instruction:
        logging.warning("no audio captured")
        sleep(0)
    if "stellar mls" in instruction:
        talk("opening stellar, mls")
        realtor()


################################################################################################################################
################################################################################################################################

#######                                                                  COMMANDS
    elif "on youtube" in instruction:
        try:
            song = instruction.replace("play on youtube", " ")
            talk("playing" + song)
            pywhatkit.playonyt(song)
            logging.info("YOUTUBE SEARCH SELECTED")
        except:
            pass

#######                                                                  BASICS / DO SOMETHING/

#####                                                                                               TELL ME SOMETHING
    elif "recorded" in instruction:
        if quintessa == 1:
            talk("yes you are,")
        else:
            talk("no")
#################                                      TERMINAL
    elif "status" in instruction:
        if quintessa == 1:
            talk(status_black)
        else:
            talk(status_blue)
#####                                                                                               TELL ME SOMETHING

#######                                                                               GREETINGS
    elif "hello" in instruction:
        talk(hello)


    elif "about yourself" in instruction:
            talk(about_u)
    elif "who are you"  in instruction:
        if quintessa == 1:
            talk("I am unity")
        else:
            talk(who_are_you)
    elif "how are you" in instruction:
        talk(how_are_u)
    elif "who are you" in instruction:
        talk(i_am)
    elif "what can you do" in instruction:
        talk(demo)
    elif "your name" in instruction:
        if singularity == 1:
            my_voice.setProperty('voice',voice[19].id)
            talk("unity")
        else:
            talk("quintessa")
    elif "my name" in instruction:
        username = instruction.replace("my name is"," ")
        talk("hi" + username)



    elif "is q" in instruction:
        talk(who_is_q)
    elif "your creator" in instruction:
        talk(who_is_your_creator)
#######                                                                               GREETINGS

######                                                                                            ORIENTATION
    elif "what time is it" in instruction:
        time = datetime.now().strftime('%I:%M %p')
        talk(what_time_is_it + time)
    elif "what's today's date" in instruction:
        date = datetime.now().strftime('%d /%m /%Y')
        talk(todays_date + date)
    elif "what's today" in instruction:
        day = datetime.today().strftime('%A')
        talk(whats_today + day)
######                                                                      ORIENTATION

#####                                                                       TURN QUINTESSA ON
    elif "it's me" in instruction:
        logging.info('QUINTESSA EASY ACCESS ACTIVE')
        print("UNITY PASSWORD")
        talk("enter the password on the screen please ")
        password = input('@')
        if password == '369':
            sleep(1)
            os.system("clear")
            print("                                                             {{ ADMIN ACCESS GRANTED }}")
            talk("Access granted,")
            sleep(.5)
            os.system("clear")
            singularity = 1
            quintessa = 0
        else:
            os.system("clear")
            my_voice.setProperty('voice',voice[31].id)
            print("          Access DENIED!")
            talk("Access Denied, fuck up outta hea, mutha foka")
            my_voice.setProperty('voice',voice[9].id)
            sleep(1)
            os.system("clear")


    if singularity == 1:
        if "unity" in instruction:
            quintessa = 1
    if singularity == 0:
        if "unity" in instruction:
            my_voice.setProperty('voice',voice[19].id)
            talk("breech detected, Stop ")
            talk("You do not have access to this mode !")
            my_voice.setProperty('voice',voice[9].id)


#####                                                                       TURN QUINTESSA ON

#####                                                                       GO GHOST/ SWITCH MODES


    if "see you later" in instruction:
        if quintessa == 1:
            talk("OK")
            sleep(0)
            my_voice.setProperty('voice',voice[5].id)
            talk("hello again its me Yu kai")
            logging.info('QUINTESSA SHUTTING DOWN')
            sys.exit(0)
        if quintessa == 0:
            my_voice.setProperty('voice',voice[5].id)
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
        temp_access = 0
        os.system("clear")
        sleep(3)
        talk("rebooting process complete, ram erased, variables reset, how may i help you ")
        logging.error("Error Rebooting")
        logging.warning('Warning error detected rebooting')
#####                                                                       GO GHOST/ SWITCH MODES

#####                                                                       NEW MODES COMMING SOON
    elif "help" in instruction:
        logging.info('HELP DETECTED')
        talk(Help)
    elif "weather" in instruction:
        instruction = instruction.replace("weather", " ")
        city = instruction
        if city:
            talk("getting weather data from"+city)
            print(city)
            weather(city)
        else:
            print('No City Found')
    if "my location" in instruction:
        if city:
            talk(city)
        else:
            talk("i am not sure, yet")
    if "who is" in instruction:
        logging.info("SEARCH SUCCESSFUL")
        info = instruction.replace("who is", " ")
        Search(info)
    if "what is" in instruction:
        if "your name" in instruction:
            pass
        logging.info("SEARCH SUCCESSFUL")
        info = instruction.replace("what is ", " ")
        Search(info)
    if "how" in instruction:
        logging.info("SEARCH SUCCESSFUL")
        info = instruction.replace("how", " ")
        Search(info)
    if "search" in instruction:
        logging.info("find")
        imfo = instruction.replace("search", " ")
        Search(info)
        ############################################
    if "open" in instruction:
        logging.info("open")
        Open = instruction.replace("open", " ")
        url = f"https://www.google.com/search?q={Open}"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()

    else:
        print(Fore.RED+"Unregistered Command","{",instruction,"}",Fore.GREEN)

#####                                                                       NEW MODES COMMING SOON

for i in range(1):
    start()
with open("AI.TXT", "w") as ai:
    ai.write("\n"+"NEW SESSION"+"\n")

for i in itertools.count():
    play_yukai()
    logging.info("Run Value: " + str(i))
    print(Fore.GREEN+"                                                                                   LISTENING...")

    with open("AI.TXT", "a+") as ai:
        if instruction == instruction:
            ai.write("\n"+"SAVED SENTENCE: #" + str(session)+"\n")
            ai.write("Sentence {"+instruction+"}"+"\n")
        else:
            pass

    sleep(0.00005)
