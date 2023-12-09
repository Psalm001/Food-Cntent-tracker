import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as  sns
#plt.style("dark background")
def visualize(meal):
    elementList=["CARBOHYDRATE","PROTEIN","FATS","MINERALS","WATER"]
    
    #A PIE CHART OF ALL THE VARIOUS QUANTITY OF EACH COMPONENET
    plt.subplot(221)
    plt.pie(meal,labels=elementList,startangle=90,labeldistance=True)
    plt.title("COMPONENT QUANTITY")
    plt.show()
    
    #plt.subplot(222)
    
    