#the authors names are Mac and Gwyneth


def too_long(char):
    if len(char) > 140:
        return "The message is too long to be sent in SMS."
    else:
        return "The message fits the SMS character limit."
test_message_1 = "this fits the SMS character limit"
test_message_2= "this will not fit sms character limit due to the overall length of the message and I wish this message would end but it does not want too, so i shall keep going until it does!"
print(too_long(test_message_1))
print(too_long(test_message_2))

import unicodedata
print(unicodedata.lookup("cat"))
print(unicodedata.lookup("snake"))
print(unicodedata.lookup("sun"))
print(unicodedata.lookup("two hearts"))
print(len(unicodedata.lookup("snake")))
print(len("🐍🐍🐍"))
print(len("🐈🐈🐈"))
print(len("☉🐍💕"))

unicodedata.name("@")

