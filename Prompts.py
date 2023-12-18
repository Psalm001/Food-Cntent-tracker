import pandas as pd

# ACTION PROMPT
def prompt():
    try:
        action = input("""
        WELCOME TO MY MEAL TESTER
        PLEASE ENTER THE ACTION YOU WANT TO PERFORM

        "1" : "VISUALIZE A DAY MEAL",
        "2" : "VISUALIZE A WHOLE DAY MEAL",
        "3" : "CREATE / USE an EXISTING FILE TO TRACK YOUR MEAL",
        "4" : "VISUALIZE TRACKED FILE"
        "q" : "QUIT"
        """)
        return action
    except Exception as e:
        print(f"Error during prompt: {e}")
        return None

# FOOD PROMPT
def food_prompt():
    try:
        # Prompt the user
        foodname = input("ENTER FOOD NAME: ")

        carbohydrate = int(input("CARBOHYDRATE LEVEL: "))
        protein = int(input("PROTEIN LEVEL: "))
        fats = int(input("FATS LEVEL: "))
        minerals = int(input("MINERALS LEVEL: "))
        water = int(input("WATER LEVEL: "))

        food_data = {
            'Carbohydrate (g)': carbohydrate,
            'Protein (g)': protein,
            'Fats (g)': fats,
            'Minerals (g)': minerals,
            'Water (g)': water
        }

        # Create a Pandas Series
        foodClassArray_Sr = pd.Series(food_data, name=foodname)

        return foodClassArray_Sr
    except ValueError as ve:
        print(f"ValueError during food_prompt: {ve}")
        return None
    except Exception as e:
        print(f"Error during food_prompt: {e}")
        return None

# INPUT METHOD1 PROMPT
def inputMethod():
    try:
        action = input("""
        PLEASE ENTER THE ACTION YOU WANT TO PERFORM
        PRESS 1 : INPUT CLASS OF FOOD LEVELS
        PRESS 2 : INPUT FOOD AND WE SPLIT TO ITS QUANTITY
        PRESS q : QUIT
        """)
        return action
    except Exception as e:
        print(f"Error during inputMethod: {e}")
        return None

# read file from data
def read_file():
    try:
        foodname = input("ENTER FOOD NAME : ")
        file = pd.read_csv("food.csv")

        file.set_index("Food", inplace=True)

        if foodname in file.index:
            foodContent = file.loc[foodname]
            return foodContent
        else:
            print("SORRY!! WE DO NOT HAVE INFO ABOUT THE FOOD")
            return None
    except Exception as e:
        print(f"Error during read_file: {e}")
        return None
