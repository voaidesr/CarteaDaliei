import requests


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "36d9d770-4d4e-11f1-a325-b317a8444454651fb608-3f17-474a-8955-0eefbc04e9b9"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


def answer_question():
    question = input("> ")

    if question == "exit":
        return 1

    answer = classify(question)
    answerclass = answer["class_name"]  # label = clasa in care apare textul meu
    confidence = answer["confidence"]  # 65. 76.6

    # The worksheet uses a threshold of 75 to handle unexpected input[cite: 458, 486].
    if confidence < 65:
        print(
            "NPC: I have no idea what you're blabbering about, traveler. Speak plainly!"
        )
    # else if
    elif answerclass == "buy_items":
        print(
            "NPC: I've got the finest steel in all the realm! Swords, shields, and armor. What'll it be?"
        )

    elif answerclass == "ask_for_quest":
        print(
            "NPC: Actually, yes. Goblins have been raiding my iron shipments in the Eastern Woods. Clear them out, and I'll forge you a custom blade."
        )

    elif answerclass == "game_lore":
        print(
            "NPC: You're in Oakhaven, stranger. But keep your voice down—the King's guards are everywhere, and they don't take kindly to nosy adventurers."
        )

    elif answerclass == "threaten_npc":
        print(
            "NPC: *Draws a glowing, enchanted warhammer* You picked the wrong shop, scrub. I was slaying dragons before you were born. Get out!"
        )

    elif answerclass == "want_to_buy":
        print("NPC: Give how much gold you can spare. It's yours")

    return 0


while answer_question() != 1:
    pass
