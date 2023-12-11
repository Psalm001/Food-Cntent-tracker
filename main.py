
from singleDay import *
from wholeDAY import *
from Prompts import *


repetition=True
while repetition:
    a= prompt()
    if a == "1":
        singleMEAL()
    elif a == "2":
        daily()
    elif a == "3":
        file_prompt()
    elif a == "q":
        break
    else:
        print("invalid input")
        continue