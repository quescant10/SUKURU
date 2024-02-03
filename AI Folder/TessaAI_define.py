###                                                   ANY DEFINITION GOES HERE
import speech_recognition as aa
import pyttsx3 as tts
import os
import wikipedia
import logging
from requests_html import HTMLSession
from time import sleep
import openai


openai.api_key ='sk-########################################'
my_voice = tts.init()
voice = my_voice.getProperty('voices')
listener = aa.Recognizer()
my_voice.setProperty('voice',voice[11].id)
lb = "\n"
start = 0
session = 0
quintessa = 0

def auto_log(instruction):
    global session
    with open("AI.TXT", "a+") as ai:
        if instruction == instruction:
            ai.write("\n"+"SAVED SENTENCE: #" + str(session)+"\n")
            ai.write("Sentence {"+instruction+"}"+"\n")
        else:
            ai.write("\n"+"FAILED SENTENCE: #" + str(session)+"\n")
            ai.write("Sentence {"+instruction+"}"+"\n")
            pass
def Shiva():
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
        
        sleep(0)

        break

def talk(text):

    my_voice.say(text)
    my_voice.runAndWait()

    


    #driver.close()

def input_instruction():
    global instruction
    global quintessa
    instruction = " "
    try:
        with aa.Microphone() as mic:
            speech = listener.listen(mic, timeout=3,phrase_time_limit=3)
            listener.adjust_for_ambient_noise(mic, duration = 0.005)
            listener.dynamic_energy_threshold =True
            listener.dynamic_energy_adjustment_damping =0.5
            listener.dynamic_energy_adjustment_ratio =3
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            #listener.pause_threshold =10
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
                talk("im glad to hear,")

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
        return("I Am a prototype sentinel, I am your virtual assistant for this experience, ask me anything")
    def i_am():
        return f"i am an, artificial intelligence,"
    def demo():
        demo_index = [" some things you can ask me are,",
        "open,", "to open anything on the web, or say,","play on youtube, to play a video or song",",you can also say,","show me,or, what's the weather like in your city, i also have a deep mind, ask q for authorization"
        ]
        demo_string =" ".join([str(item) for item in demo_index])
        return(demo_string)
    def Help():
        Help_index = ["help unavailable"
        ]
        Help_string =" ".join([str(item) for item in Help_index])
        return(Help_string)
