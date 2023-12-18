from singleDay import *
from Prompts import *
from visualize import *
import pandas as pd


def daily():
    count=[]
    counter=1
    for i in range(0,3):
        print(f"CHOOSE METHOD FOR MEAL {counter} ")
        actionValue=inputMethod()
        print(f"ENTER YOUR MEAL {counter}")
        if actionValue == "1":
            a=food_prompt()
            count.append(a)
        elif actionValue == "2":
            b=read_file()
            count.append(b)
        elif actionValue == "q":
            break
        else :
            print("incorrect value")
            continue
        
        counter+=1
    food_df = pd.concat(count, axis=1)
    food_mean=food_df.mean(axis=1)
    visualize(food_mean)  
        
    
    

#daily()   
    
