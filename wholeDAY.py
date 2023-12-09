from singleDay import *
from promptSingle import *
from visualize import *


def daily():
    count=[]
    counter=1
    for i in range(0,3):
        print("CHOOSE METHOD FOR MEAL {counter}")
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
    for elements in count:       
        count_df=pd.DataFrame(elements)
        visualize(count_df)
    
    

    
    
"""         
count=[]
    
a=inputMethod()
print(a)
if a == "1":
    a=food_prompt()
    count.append(a)
    
print(count)
#count.append(food_prompt())




 
for i in range(0,2):
    
    elif inputMethod() == "2":
        read_prompt=read_file()
        count.append(read_prompt)
        
print(count)     

count=[]
inputMethod()
if inputMethod == "1":
    food_prompt()
    count.append(food_prompt())
    
print(count)
"""
