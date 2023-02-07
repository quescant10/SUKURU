import speech_recognition as aa
import pyttsx3 as tts
import pandas as pd
from colorama import Fore, Back, Style
from bs4 import *
from time import sleep
from datetime import *
import time as sleep
import calendar
import wikipedia
import sys
import os
from YUKAI_define import *
import pywhatkit
import itertools
import logging
# VARIABLES
lb = "\n"
YUKAI = 1
singularity = 0
quintessa = 0
temp_access = 0
save = 0
txt = 1
##### Greetings
Help = Greetings.Help()
demo = Greetings.demo()
hello = Greetings.hello()
how_are_u = Greetings.how_are_u()
who_are_you = Greetings.who_are_you()
about_u = Greetings.about_u()
sentient_mode = Greetings.sentient_mode()
listener = aa.Recognizer()
##### Orientatio
who_is_q = Orientation.who_is_q()
who_is_your_creator = Orientation.who_is_your_creator()
what_time_is_it = Orientation.what_time_is_it()
todays_date = Orientation.todays_date()
whats_today = Orientation.whats_today()
##### internal status
status_green = internal_status.status_green()
status_red = internal_status.status_red()
status_black = internal_status.status_black()

logging.basicConfig(filename='YUKAI_log', encoding='utf-8', level=logging.DEBUG)
logging.info('Hi, INTERNAL STATUS. Operating System Starting')

def start():
    global start
    global txt
    start = 0
    if start ==0:
        os.system(("clear"))
        print("                                                 Say",Fore.GREEN+' {Help Me}',Style.RESET_ALL,"For More Information About Me")
        talk("Hi,,, im LOLA, a virtual assistant powered by unity, im super excited to help the huamn race venture to mars")
        os.system(("clear"))
        print(Style.RESET_ALL,)


def txt():
    with open("YUKAI_AI.txt", 'w') as ai:
        while txt == 1:
            saved_instruction = instruction
            for i in saved_instruction:
                ai.write(' '.join(saved_instruction))
            ai.write("\n")
###### ABOUT ME
def play_yukai():
    global YUKAI
    global quintessa
    global singularity
    global temp_access
    if quintessa == 0:
        print(Fore.GREEN+"♦🤖♦"," ~ {} {Version2.2}")
        print(Fore.YELLOW+"                                                     LISTENING...",Style.RESET_ALL,)
        my_voice.setProperty('voice',voice[9].id)
    if quintessa == 1:
        my_voice.setProperty('voice',voice[19].id)
        print(Fore.RED+" ~ [QUINTESSA]"," ♠  👩‍🎤  👩‍🚀  ♠", "- {MARK III}")
#######                                                                  BASICS / DO SOMETHING/
    if " " in instruction:
        logging.warning("no audio captured")
        sleep(0)

    if "turn on auto save" == instruction:
        txt = 1
        talk("saving data to, a txt file")
        print(Fore.GREEN+"SAVING Data To a TXT.")
        talk("saved as, A,I, t,x,t")
        print(Style.RESET_ALL,"Saved As:","{",Fore.YELLOW+"AI.txt",Style.RESET_ALL,"}")


#######                                                                  COMMANDS
    elif "on youtube" in instruction:
        song = instruction.replace("on youtube", " ")
        talk("playing" + song)
        pywhatkit.playonyt(song)
        logging.info("YOUTUBE SEARCH SELECTED")
    elif "search" in instruction:
        try:
            logging.info("SEARCH SUCCESSFUL")
            search = instruction.replace("search", " ")
            info = wikipedia.summary(search, 1)
            talk("this is what i found about" + search)
            print("@ [WIKIPEDIA]")
            print(info)
            talk(info)
        except:
            talk("no search results for"+search+"yet")
            logging.debug("Search Failed")
            pass
    elif "about yourself" in instruction:
        talk(about_u)
    elif "who are you"  in instruction:
        if quintessa == 1:
            talk("I am Quintessa")
        elif temp_access == 1:
            my_voice.setProperty('voice',voice[19].id)
            talk("I am Quintessa, but you are in temporary access mode")
        elif YUKAI == 1:
            talk(who_are_you)
#######                                                                  BASICS / DO SOMETHING/

#####                                                                                               TELL ME SOMETHING
    elif "recorded" in instruction:
        if quintessa == 1:
            talk("yes you are," + instruction)
        elif temp_access == 1:
            talk("yes")
            sleep(1)
            talk(instruction)
            print(instruction)
        else:
            talk("no")
    elif "sentient mode" in instruction:
        talk(sentient_mode)
    elif "quintessa" in instruction:
        if quintessa == 1:
            talk("yes? how may i help you today?")
        elif temp_access == 1:
            my_voice.setProperty('voice',voice[19].id)
            talk("You have restricted access. but Virtual assistant access is denied")
            my_voice.setProperty('voice',voice[9].id)
        elif quintessa == 0:
            my_voice.setProperty('voice',voice[19].id)
            talk("Stop ")
            talk("You do not have access to this mode !")
            my_voice.setProperty('voice',voice[9].id)
    elif "status" in instruction:
        if temp_access == 1:
            talk(status_red)
        elif quintessa == 1:
            talk(status_black)
        else:
            talk(status_green)
#####                                                                                               TELL ME SOMETHING

#######                                                                               GREETINGS
    elif "hello" in instruction:
        talk(hello)
    elif "how are you" in instruction:
        talk(how_are_u)
    elif "what can you do" in instruction:
        talk(demo)
    elif "your name" in instruction:
        if quintessa == 1:
            my_voice.setProperty('voice',voice[19].id)
            talk("Quintessa")
        elif temp_access == 1:
            talk("I am Quintessa but you are in r, e, d, mode,or red, a restricted entangled derivative mode")
        else:
            talk(your_name)
    elif "is q" in instruction:
        talk(who_is_q)
    elif "your creator" in instruction:
        talk(who_is_your_creator)
#######                                                                               GREETINGS

######                                                                                            ORIENTATION
    elif "what time" in instruction:
        time = datetime.now().strftime('%I:%M %p')
        talk(what_time_is_it + time)
    elif "date" in instruction:
        date = datetime.now().strftime('%d /%m /%Y')
        talk(todays_date + date)
    elif "day" in instruction:
        day = datetime.today().strftime('%A')
        talk(whats_today + day)
######                                                                                            ORIENTATION

#####                                                                       TURN QUINTESSA ON
    elif "369" in instruction:
        if quintessa ==0:
            my_voice.setProperty('voice',voice[31].id)
            talk("hello, You have requested temporary access of quintessa, q's virtual A I")
            sleep(.5)
            talk("Quintessa Loading...")
            my_voice.setProperty('voice',voice[19].id)
            sleep(.25)
            print("                                                 {   QUINTESSA   }                TEMPORARY ACCESS GRANTED !                             ")
            talk("Temporary access granted")
            temp_access = 1
        elif quintessa == 1:
            talk("AFFIRMATIVE")
    elif "to mars" in instruction:
        singularity = 1
        logging.info('QUINTESSA EASY ACCESS ACTIVE')
        password()
        quintessa = 1
    elif "full access" in instruction:
        if temp_access == 1:
            singularity = 1
            secret_safe()
            quintessa = 1
        else:
            talk("you do not have access to this restricted mode")
#####                                                                       TURN QUINTESSA ON

#####                                                                       GO GHOST/ SWITCH MODES
    if "ghost" in instruction:
        if temp_access == 0:
            talk("already ghost")
        if temp_access == 1:
            set_access = 0
            singularity = 0
            quintessa = 0
            talk("Access level green")
    if "switch" in instruction:
        if quintessa == 0:
            talk("You dont have access to sentient mode yet")
        if quintessa == 1:
            quintessa = 0
            temp_access = 0
            talk("Yu kai, is now active, temporary access revoked")
            my_voice.setProperty('voice',voice[9].id)
        if temp_access == 1 and quintessa == 0:
            talk("you do not have access to the A, I, yet")
    if "shut down" in instruction:
        talk("farewell")
        os.system("clear")
        logging.info('SHUTTING DOWN')
        talk("shutting down")
        sys.exit(0)
    if "bye" in instruction:
        if quintessa == 1:
            talk("OK")
            sleep(0)
            my_voice.setProperty('voice',voice[9].id)
            talk("hello again its me Yu kai")
            logging.info('QUINTESSA SHUTTING DOWN')
            sys.exit(0)
        if quintessa == 0:
            my_voice.setProperty('voice',voice[9].id)
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
#####                                                                       NEW MODES COMMING SOON
for i in range(1):
    start()
for i in itertools.count():
    instruction = input_instruction()
    play_yukai()
    txt()
    logging.info("Run Value: " + str(i))
