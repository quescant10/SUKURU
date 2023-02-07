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
from LOLA_define import *
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
sentient_mode = Greetings.sentient_mode()
listener = aa.Recognizer()
##### Orientatio
who_is_q = Orientation.who_is_q()
who_is_your_creator = Orientation.who_is_your_creator()
what_time_is_it = Orientation.what_time_is_it()
todays_date = Orientation.todays_date()
whats_today = Orientation.whats_today()
##### internal status
status_red = internal_status.status_red()
status_black = internal_status.status_black()

logging.basicConfig(filename='LOLA_log', encoding='utf-8', level=logging.DEBUG)
logging.info('Hi, INTERNAL STATUS. Operating System Starting')

def start():
    global start
    global txt
    start = 0
    session = 0
    if start ==0:
        os.system(("clear"))
        print("                                                 Say",Fore.RED+' {Help Me}',Style.RESET_ALL,"For More Information About Me")
        os.system(("clear"))
        print(Style.RESET_ALL,)



def txt():
    with open("LOLA_AI.txt", 'w') as ai:
        session = 0
        while txt == 1:
            saved_instruction = instruction
            for instruction in saved_instruction:
                ai.write("SAVED SENTENCE: #",session)
                ai.write(' '.join(saved_instruction))
            ai.write("\n")
            session += 1

###### ABOUT ME
def play_yukai():
    global LOLA
    global quintessa
    global session
    if quintessa == 0:
        print(Fore.YELLOW+"                                                ♦🤖♦"," ~ [LOLA]-[Version2]")
        my_voice.setProperty('voice',voice[5].id)
    if quintessa == 1:
        my_voice.setProperty('voice',voice[19].id)
        print(Fore.RED+"                                                  ~ [QUINTESSA]"," ♠  👩‍🚀  ♠",Style.RESET_ALL)
#######                                                                  BASICS / DO SOMETHING/
    if " " in instruction:
        logging.warning("no audio captured")
        sleep(0)

    if "turn on auto save" == instruction:
        session = 1
        talk("saving data to, a txt file")
        print(Fore.GREEN+"SAVING Data To a TXT.")
        talk("saved as, A,I, t,x,t")
        print(Style.RESET_ALL,"Saved As:","{",Fore.YELLOW+"AI.txt",Style.RESET_ALL,"}")


#######                                                                  COMMANDS
    elif "on youtube" in instruction:
        try:
            song = instruction.replace("on youtube", " ")
            talk("playing" + song)
            pywhatkit.playonyt(song)
            logging.info("YOUTUBE SEARCH SELECTED")
        except:
            pass
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
        elif LOLA == 1:
            talk(who_are_you)
#######                                                                  BASICS / DO SOMETHING/

#####                                                                                               TELL ME SOMETHING
    elif "recorded" in instruction:
        if quintessa == 1:
            talk("yes you are," + instruction)
        else:
            talk("no")
    elif "quintessa" in instruction:
        if quintessa == 1:
            talk("yes? how may i help you today?")
        elif quintessa == 0:
            my_voice.setProperty('voice',voice[19].id)
            talk("Stop ")
            talk("You do not have access to this mode !")
            my_voice.setProperty('voice',voice[5].id)
    elif "status" in instruction:
        if quintessa == 1:
            talk(status_black)
        else:
            talk(status_red)
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
            talk("LOLA")
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
    elif "to mars" in instruction:
        singularity = 1
        logging.info('QUINTESSA EASY ACCESS ACTIVE')
        password()
        quintessa = 1
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
            my_voice.setProperty('voice',voice[5].id)
        if temp_access == 1 and quintessa == 0:
            talk("you do not have access to the A, I, yet")
    if "shut down" in instruction:
        if quintessa == 1:
            talk("ok,")
            os.system("clear")
            logging.info('SHUTTING DOWN')
            talk("goodbye human")
            sys.exit(0)
        else:
            talk("disengaging the o s")
            os.system("clear")
            logging.info('SHUTTING DOWN')
            talk("shutting down")
            sys.exit(0)
    if "bye" in instruction:
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
    else:
        print(Fore.RED+"Unregistered Command","{",instruction,"}",Fore.GREEN)
#####                                                                       NEW MODES COMMING SOON


for i in range(1):
    start()

for i in itertools.count():
    instruction = input_instruction()
    play_yukai()
    logging.info("Run Value: " + str(i))
    print(Fore.GREEN+"                                                     LISTENING...")
    sleep(0)
with open("LOLA_AI.txt", 'w') as ai:
    for word in instruction:
        ai.write("SAVED SENTENCE: #",session)
        ai.write(word)
        ai.write("\n")
        session += 1
        sleep(4)
        print("clear",Style.RESET_ALL)
        os.system("clear")

