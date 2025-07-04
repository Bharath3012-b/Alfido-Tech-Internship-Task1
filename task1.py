import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   
import seaborn as sns             
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier       
from sklearn.metrics import accuracy_score            

df = pd.read_csv('C:/Users/DELL/Desktop/IRIS.csv')

plt.figure(figsize=(12, 4))

for i, col in enumerate(df.columns[:-1]):  
    plt.subplot(1, 4, i + 1)
    df[col].plot(kind='hist', bins=10, edgecolor='black')
    plt.title(col)
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
