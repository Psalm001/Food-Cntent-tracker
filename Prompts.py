from dataclasses import dataclass
from visualize import *
import pandas as pd


@dataclass
class quantity :
    #measurement variables
    CARBORHYDRATE= int
    PROTEIN = int
    FATS=int
    MINERALS=int
    WATER=int
    FOODNAME = str
    
    
#ACTION PROMPT
def prompt():
    action="""
    WELCOME TO MY MEAL TESTER
    PLEASE ENTER THE ACTION YOU WANT TO PERFORM
    
    "1" : "VISUALIZE A DAY MEAL",
    "2" : "VISUALIZE A WHOLE DAY MEAL",
    "3" : "CREATE / USE an EXISTING FILE TO TRACK YOUR MEAL",
    "4" : "VISUALIZE TRACKED FILE"
    "q" : "QUIT"
    """
    ACTION =input(action)
    
    return ACTION
#FOOD PROMPT
def food_prompt():
    #prompt the user
    foodname=input("ENTER FOOD NAME: ")
    foodname_col=[]
    foodname_col.append(foodname)
    
    
    print("\n")
    
    carbohydrate=input("CARBORHYDRATE LEVEL: ")
    protein=input("PROTEIN LEVEL: ")
    fats=input("FATS LEVEL: ")
    minerals=input("MINERALS LEVEL: ")
    water=input("WATER LEVEL: ")
    
    food_data = {
    #'foodname' : foodname,
    'Carbohydrate (g)': carbohydrate,
    'Protein (g)': protein,
    'Fats (g)': fats,
    'Minerals (g)': minerals,
    'Water (g)': water
    }
    
    print("\n")
    
    foodClassArray_Sr=pd.Series(food_data)
    foodClassArray_pd=pd.DataFrame(foodClassArray_Sr,columns=foodname_col)
    
    
    
    return foodClassArray_pd

# INPUT METHOD1 PROMPT
def inputMethod ():
    #CREATING A LIST FOR THE MEAl TO BE VISUALIZED
    
    action="""
    PLEASE ENTER THE ACTION YOU WANT TO PERFORM
    PRESS 1 : INPUT CLASS OF FOOD LEVELS
    PRESS 2 : INPUT FOOD AND WE SPLIT TO ITS QUANTITY
    PRESS q : QUIT
    """
    ACTION =input(action)
    return ACTION

# read file from data
def read_file ():
    foodname=input("ENTER FOOD NAME : ")
    file=pd.read_csv("food.csv")

    file.set_index("Food" , inplace=True)
    
    if foodname in file.index:
        foodContent=file.loc[foodname]
        return foodContent
    else:
       print ("SORRY!! WE DO NOT HAVE INFO ABOUT THE FOOD")
    
#print(food_prompt())