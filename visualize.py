import numpy as np
import matplotlib.pyplot as plt


def visualize(meal):
    elementList = ["CARB", "PROT", "FATS", "MINs", "WAT"]
    
    average_daily_values = [300, 50, 70, 1000, 2500]
# [Carbohydrates (g), Protein (g), Fats (g), Minerals (mg), Water (ml)]


    # A PIE CHART OF ALL THE VARIOUS QUANTITY OF EACH COMPONENT
    plt.subplot(221)
    plt.pie(meal, labels=elementList, startangle=90, labeldistance=1.1, autopct='%1.1f%%')
    plt.title("COMPONENT QUANTITY - Pie Chart")

    # A BAR CHART OF ALL THE VARIOUS QUANTITY OF EACH COMPONENT
    plt.subplot(222)
    plt.bar(elementList, meal)
    plt.title("COMPONENT QUANTITY - Bar Chart")

    # A HORIZONTAL BAR CHART SHOWING DAILY AVERAGE CONSUMPTION
    plt.subplot(223)
    plt.barh(elementList, meal)
    plt.axvline(np.mean(meal), color='red', linestyle='dashed', linewidth=2, label='Daily Average')
    plt.title("DAILY AVERAGE CONSUMPTION")
    plt.legend()

    # A HORIZONTAL BAR CHART COMPARING WITH AVERAGE DAILY VALUES
    plt.subplot(224)
    plt.barh(elementList, meal, label='Meal')
    plt.barh(elementList, average_daily_values, alpha=0.25, label='Daily Average')
    plt.axvline(np.mean(meal), color='red', linestyle='dashed', linewidth=2, label='Meal Average')
    plt.title("NUTRITIONAL PROFILE COMPARISON")
    plt.legend()

    plt.tight_layout()
    plt.show()

