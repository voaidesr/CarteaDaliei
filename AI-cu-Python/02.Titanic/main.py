from mlforkidsnumbers import MLforKidsNumbers

project = MLforKidsNumbers(
    key="29ece340-47d6-11f1-8076-ef68cee77436abf9520f-0a06-4628-94b1-a7ba09bcf919",
    modelurl="https://mlforkids-newnumbers.j8ayd8ayn23.eu-de.codeengine.appdomain.cloud/saved-models/7d8a1930-47d3-11f1-8076-ef68cee77436/status"
)

# CHANGE THIS to something you want your
# machine learning model to classify
testvalue = {
    "ticket class" : 1,
    "gender" : "male", # female
    "age" : 35,
    "sibl. sp." : 1,
    "par. ch." : 2,
    "ticket fare" : 450,
    "embarked" : "Cherbourg",
}

response = project.classify(testvalue)
top_match = response[0]

label = top_match["class_name"]
confidence = top_match["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))