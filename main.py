import json
import requests
import time
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

urlFile = "image_urls.txt"

urlList = [
    "https://i.pinimg.com/originals/1b/72/f9/1b72f91427ded7ed909066c499fedca7.jpg",
    "https://www.occasionsmessages.com/wp-content/uploads/2018/03/Motivational-Good-Morning-Messages.jpg",
    "https://i.stack.imgur.com/i1Abv.png",
    "https://www.wishesquotes.com/wp-content/uploads/2022/01/Good-morning-sweetie.jpg",
    "https://www.wishafriend.com/goodmorning/uploads/8467-inspirational-good-morning-messages.jpg",
    "https://www.ratikantasingh.com/wp-content/uploads/2021/07/good-morning-wishes.jpg",
    "https://www.bestmessage.org/wp-content/uploads/2015/01/parents-good-morning-messages.jpg",
    "https://www.ourmindfullife.com/wp-content/uploads/2021/01/Good-morning-quotes-3.jpg",
    "https://freefontsfamily.com/wp-content/uploads/2019/06/Morning-Wishes-Font.jpg",

]

wordList = [

"Good Morning... Be Happy not because everything is good, but because you see good in everything",
"Good Morning Have a nice day! OccasionsMessages.com",
"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
'So many of my smiles start because of you. You are my sunshine. Good morning sweetie! "Wishes Quotes',
'Look outside the window, A lovely morning is here, Go out there and have your say, Go out there and find a way, Coz today is a new day! Good morning! Wishafriend.com',
'Good Morning! Have a good day ahead!',
'Good Morning Messages for Parents',
'Be willing to be a beginner every single morning -Meister Eckhart OurMindfulLife.com',
'wake up and be awesome',


]

words=["hi", "hi"]





for x in range(len(urlList)):
    endpoint = "https://azurefund1.cognitiveservices.azure.com/vision/v3.2/read/analyze"
    key = "949bf77c0b44497088ac2be677c29f54"

    endpointResults = "https://azurefund1.cognitiveservices.azure.com/vision/v3.2/read/analyzeResults/"


    image_url = urlList[x]


    features = "objects,tags,description"


    headers = {
        "Ocp-Apim-Subscription-Key": "949bf77c0b44497088ac2be677c29f54",
        "Content-Type": "application/json"
    }

    data = {
        "url": image_url,
        "features": [
            {"type": feature} for feature in features.split(',')
        ]
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 202:
        data = response

        operation_location = (data.headers["Operation-Location"])
        operation_id = operation_location.split("/")[-1]
        # print(operation_id)
    else:
        print("Error: " + response.text)

    time.sleep(1)

    response = requests.get(endpointResults + operation_id, headers=headers)
    if response.status_code == 200:

        data = response.json()

        data = response.json()
        lines = (data["analyzeResult"]["readResults"][0]["lines"])
        text = ""
        for line in lines:
            print(line['text'])
            text += line['text'] + " "
        print("AZURE RESULT TEXT IS " + text)
        print(similar(text, wordList[x]))

    else:
        print("Error: " + response.text)
