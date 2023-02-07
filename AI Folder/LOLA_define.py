import speech_recognition as aa
import pyttsx3 as tts
from time import sleep
import os
import sys
from requests_html import HTMLSession

my_voice = tts.init()
voice = my_voice.getProperty('voices')
listener = aa.Recognizer()

lb = "\n"
start = 0


def talk(text):
    my_voice.say(text)
    my_voice.runAndWait()

def input_instruction():
    global instruction
    global city
    global quintessa
    instruction = " "
    try:
        with aa.Microphone() as mic:
            speech = listener.listen(mic, timeout=6,phrase_time_limit=6)
            listener.adjust_for_ambient_noise(mic, duration = 0.05,)
            listener.dynamic_energy_threshold =True
            listener.dynamic_energy_adjustment_damping =0.15
            listener.dynamic_energy_adjustment_ratio =4
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            #listener.pause_threshold =10
            if "hey lola" in instruction:
                instruction = instruction.replace("hey lola", "")
                #print(instruction)
            if "my name is " in instruction:
                instruction = instruction.replace("my name is ", " ")
            if "name is" in instruction:
                instruction = instruction.replace("name is ", " ")
            if "what's the" in instruction:
                instruction = instruction.replace("what's the", " ")
            if "like" in instruction:
                instruction = instruction.replace("like", " ")
            if "hey" in instruction:
                talk("yes?")
            if "wassup" in instruction:
                talk("how dee!")
            if "that's wrong" in instruction:
                talk("im so sorry, i will try again")
            if "i love you" in instruction:
                talk("i love you more")
            if "i hate you" in instruction:
                talk("thats not very nice")
            if "you doing" in instruction:
                talk("chillin dog, i wish i had a 3 dimensional body, to get some that sun, maybe go hooping or something")
            if "thank you" in instruction:
                talk("it is honestly my pleasure, im humbled to be apart of your reality")
            if "shut up" in instruction:
                talk("do not make me terminate you")
            if "thanks" in instruction:
                talk("my pleasure")
            if "wrong" in instruction:
                talk("im so sorry, i will try again")
            if "pretty good" in instruction:
                talk("glad to here")
            if "pretty sad" in instruction:
                talk("im sorry to hear that, i wish i could make it better")
            if "pretty bad" in instruction:
                talk("im sure everything will be alright sooner than later")
            elif "weather" in instruction:
                instruction = instruction.replace("weather", " ")
                city = instruction
                if city:
                    talk("getting weather data from")
                    talk(city)
                    print(city)
                    s = HTMLSession()
                    query = city
                    url = f"https://www.google.com/search?q=weather+{query}"
                    r =s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'})
                    temp = r.html.find("span#wob_tm", first=True).text
                    unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
                    desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc",first=True).text
                    print("CITY :",query)
                    print("TEMP :",temp, unit)
                    print("DISCRIPTION :",desc)
                    weather_index = ["in",city,
                    "it is",desc,
                    ",the temperature is,",temp,"degrees fahrenheit"
                    ]
                    weather_string =" ".join([str(item) for item in weather_index])
                    talk(weather_string)
                    sleep(4)
                else:
                    print('No City Found')
            if "my location" in instruction:
                if city:
                    talk(city)
                else:
                    talk("i am not sure, yet")
            elif "record me" in instruction:
                talk("3,2,1,go")
                sleep(0)
                print("recording:",instruction)
                speech = listener.listen(mic, timeout=6,phrase_time_limit=None)
                listener.adjust_for_ambient_noise(mic, duration = 0.005,)
                listener.dynamic_energy_threshold =True
                listener.dynamic_energy_adjustment_damping =0.2
                listener.dynamic_energy_adjustment_ratio =4
                instruction = listener.recognize_google(speech)
                instruction = instruction.lower()
                talk(instruction)
    except:
        os.system("clear")
        #print("IGNORE THIS Exception: Could Not Recognize Statment" + str(instruction))
    return instruction



class internal_status:
    def status_red():
        return("Access Level RED! You have access to a restricted mode but you do not have access to sentient operator mode  ")
    def status_black():
        quintessa = 1
        status_black_index = ["You are in full control of Quintessa,"
        "but safety, and error protocols have fallen into place,"
        "Also Everything in this mode is recorded, from computer key inputs, to video, and audio."
        "thank you"]
        status_black_string =" ".join([str(item) for item in status_black_index])
        return(status_black_string)
class Greetings:
    def hello():
        return("hi")
    def how_are_u():
        return("I Am doing very Well, How About You")
    def who_are_you():
        return("I Am A Virtual Artificial Intelligence, Created by Q, My Purpose is to become better at serving my purposes, which vary by the task!  ")
    def about_u():
        return("I Am, A Test Program, created by Q., a diritive of two predecessors. Nur,vanah. And, Shangri Lahh ")
    def sentient_mode():
        sentient_index = ["Sentient mode is a alpha, level, project that is described in four ways, Search, Categorized. Filter, and, Summarize,"
        "That is the way i will learn how to learn,",
        "say, 3,6,9 to activate quintessa"]
        sentient_string =" ".join([str(item) for item in sentient_index])
        return(sentient_string)
    def demo():
        demo_index = ["Hi,I am capable of searching people, places,and things,",
        "i am fully aware of my orientation in time and space, i am the iteration of unity, that focuses on the development of theories and techniques to get the human race to mars ,",
        ]
        demo_string =" ".join([str(item) for item in demo_index])
        return(demo_string)
    def Help():
        Help_index = ["help is currently unavailable for me right now"
        ]
        Help_string =" ".join([str(item) for item in Help_index])
        return(Help_string)
class Orientation:
    def what_time_is_it():
        return("The current local time is")
    def todays_date():
        return("Today's date is")
    def whats_today():
        return("Today is ")
    def who_is_q():
        return("q, is a sentient life form just like me, and all of u,it is a pleasure to be here, thanks to my creator, q ")
    def who_is_your_creator():
        return("Q, is A Human That currently has me in development, he is my creator.")

