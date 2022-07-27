import pandas as pd 
import numpy as np

book = input("Reviewed Book: ")
chapter = input("Reviewed Chapter: ")
question = input("Reviewed Question: ")


df = pd.read_csv('questions.csv')

# Find index 
dff = df[df.book == book]
dff = dff[dff.chapter == float(chapter)]
dff = dff[dff.question_number == float(question)]
index = dff.index[0]

df.loc[index, 'reviewed'] = 1
df.to_csv('questions.csv', index = False)