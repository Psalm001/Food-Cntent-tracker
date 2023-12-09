from dataclasses import dataclass
from visualize import *


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
    FOODNAME=input("ENTER FOOD NAME: ")
    print("\n")
    CARBORHYDRATE=input("CARBORHYDRATE LEVEL: ")
    PROTEIN=input("PROTEIN LEVEL: ")
    FATS=input("FATS LEVEL: ")
    MINERALS=input("MINERALS LEVEL: ")
    WATER=input("WATER LEVEL: ")
    food_data = {
    'Carbohydrate (g)': CARBORHYDRATE,
    'Protein (g)': PROTEIN,
    'Fats (g)': FATS,
    'Minerals (g)': MINERALS,
    'Water (g)': WATER
    }
    
    print("\n")
    
    foodClassArray_df=pd.Series(food_data)
    return foodClassArray_df 

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
    FOODNAME=input("ENTER FOOD NAME : ")
    file=pd.read_csv("food.csv")

    file.set_index("Food" , inplace=True)
    
    if FOODNAME in file.index:
        foodContent=file.loc[FOODNAME]
        return foodContent
    else:
       print ("SORRY!! WE DO NOT HAVE INFO ABOUT THE FOOD")
    
