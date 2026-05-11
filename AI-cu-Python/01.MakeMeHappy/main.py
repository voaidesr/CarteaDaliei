import requests
# PIL - Python Image Library
from PIL import Image

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "59303bf0-4256-11f1-9d27-07f379cf2ee52a9c93e0-928b-4d47-8270-e0eadcd01556"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

# citesc text tastatura: input("mesaj")
to_classify = input("What do you want to say?\n") # text
demo = classify(to_classify)
label = demo["class_name"] # class name -> valoare detectata
confidence = demo["confidence"] # confidence -> valoarea de incredere

if label == "kind_words":
    img = Image.open("./imgs/happy.png")
    img.show()
else:
    img = Image.open("./imgs/sad.png")
    img.show()




# dictionar cheie -> valoare
# dictionar[1] = "hello"

