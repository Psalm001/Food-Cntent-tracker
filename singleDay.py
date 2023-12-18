from Prompts import *
from visualize import *



def singleMEAL ():
    
    a=inputMethod()
    
    #INSERTING THE VARIOUS QUANTITY OF EACH CLASS OF FOODS
    
    if a == "1":
        c=food_prompt()
        print(c)
        visualized=visualize(c)
        return visualized
    
    #SPLITTING THE FOOD INTO IT'S VARIOUS QUANTITY AND VISUALIZING IT
    elif a == "2":
        a=read_file()
        print(a)
        visualized=visualize(a)
        return(visualized)
        
    elif a == "q":
        return "quit"
    
    else :
        return "incorrect input"
    

            
