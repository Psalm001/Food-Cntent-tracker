from Prompts import *
from visualize import *
import os
import numpy as np


def prompt_file():
    user_input=input("ENTER FILE NAME: ").strip()
    filename= f"{user_input}.csv"
    if  os.path.exists(filename):
        food=pd.read_csv(filename)
        foods=food[["Carbohydrate (g)" ,  "Protein (g)" , "Fats (g)" , "Minerals (g)" , "Water (g)"]]
        food_mean=foods.mean(axis=0)
        visualized=visualize(food_mean)
        return (visualized,food_mean)
    else: 
        return    "FILENAME DOES NOT EXIST"
    
#print(prompt_file())
