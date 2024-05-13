from telnetlib import EC
import pyttsx3 as p
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from YT_audio import *
from selenium_web import infow, webdriver
from News import *
import randfacts
from jokes import *
from weather import *
import datetime

def open_wikipedia(url):
    # Create a Chrome driver instance
    driver = webdriver.Chrome()

    # Set implicit wait time
    driver.implicitly_wait(10)

    # Open the provided URL
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))

    # Close the browser window
    driver.quit()


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

dif wishme():
hour=int(datetime.datetime.now().hour)
if hour>0 and hour<16
elif hour>=12 and hour<16:
    return("afternoon")
else:
    return("evening")

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir, i am Alpha.")
speak("today is " + today_date.starftime("%d") + " of " + today_date.strftime("%B") + " And its currently " + (today_date.strftime("%I")) +(today_date.strftime("%M")) + (today_date.strftime("%P")))
speak(" temperature in now delhi is " + str(temp())+"degree celsius" + " and with " + str(des()))
speak("what can i do for you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    # if "what" and "about" and "you" in text:
    speak("i am having a good day sir")
    speak("What can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

# wikipedia search function:
if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        topic = r.recognize_google(audio)
        # Build Wikipedia URL
        wikipedia_url = f"https://en.wikipedia.org/wiki/{topic}"

        # Open Wikipedia and handle information retrieval
        open_wikipedia(wikipedia_url)
    speak("searching {} in wikipedia".format(infow))
    print("searching {} in wikipedia".format(infow))
    assist = infow()
    assist.get_info(infow)

# youtube play function:
elif "play" and "video" in text2:
    speak("you want me to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        video = r.recognize_google(audio)
        speak("playing {} an youtube".formate(vid))
        print("playing {} an youtube" .formate(vid))
    assist = music()
    assist.play(vid)

# news Api function
elif "news" in text2:
    print("Sure sir, Now i will read news for you.")
    speak("Sure sir, Now i will read news for you.")
  arr=news()
  for i in range(len(arr)):
      print(arr[i])
      speak(arr[i])

elif "fact" or "fact" in text2:
   x=randfacts.getFact()
   print(x)
   speak("Did you know that, "+x)

elif "joke" or "joke" in text2:
   arr=joke()
   print(arr[0])
   speak(arr[0])
   print(arr[1])
   speak(arr[1])