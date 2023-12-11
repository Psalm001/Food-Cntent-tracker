import os
import pandas as pd
from Prompts import *

def file_prompt():
    user_prompt = """
    1 : CREATE A NEW FILE
    2 : ADD TO AN EXISTING FILE
    """
    # variable for user prompt
    user_method = input(user_prompt)
    
    if user_method == "1":
        filename = input("ENTER FILENAME: ").strip()

        if not os.path.exists(f"{filename}.csv"):
            # Create an empty file if it doesn't exist
            with open(f"{filename}.csv", 'w'):
                pass
            
            a = inputMethod()
            # checks the input method
            if a == "1":
                food_ate = food_prompt()
                food_ateDF = pd.DataFrame([food_ate])  # Create DataFrame with one row
                food_ateDF.to_csv(f"{filename}.csv", index_label="FOODNAME")
        
        
                
            elif a == "2":
                # Using read_file function
                food_ate = read_file()
                
                # Check if read_file returned a valid result
                if isinstance(food_ate, pd.Series):
                    # Create DataFrame with the same column names as the existing file
                    food_ateDF = pd.DataFrame([food_ate], columns=food_ate.index.tolist())
                    food_ateDF.to_csv(f"{filename}.csv", index_label="FOODNAME")
            
                    #print("SORRY!! WE DO NOT HAVE INFO ABOUT THE FOOD")
                
            elif a == "q":
                print("quitted")
            else:
                print("invalid input")
        else:
            print("FILE EXISTS")
            
    elif user_method == "2":
        filename = input("ENTER FILENAME: ").strip()
        filepathName = f"{filename}.csv"

        if os.path.exists(filepathName):
            a = inputMethod()
            if a == "1":
                food_ate = food_prompt()
                food_ateDF = pd.DataFrame([food_ate])  # Create DataFrame with one row
                food_ateDF.to_csv(filepathName, mode='a', header=False, index_label="FOODNAME")
            elif a == "2":
                food_ate = read_file()
                food_ateDF = pd.DataFrame([food_ate])  # Create DataFrame with one row
                food_ateDF.to_csv(filepathName, mode='a', header=False, index_label="FOODNAME")
            elif a == "q":
                print("quitted")
            else:
                print("invalid input")
        else:
            print("FILE DOES NOT EXIST")
