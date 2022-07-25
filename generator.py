
# Add to the database 

import pandas as pd
import os 
#df = pd.read_csv('questions.csv')

#print(df)

book = input('Book:')
chapter = input('Chapter:')
num_questions = input('Number questoins:')

columns = ['book', 'chapter', 'question_number', 'reviewed']

# Make df2 
data = []
for i in range(int(num_questions)):
    print(i)
    data.append([book, chapter, i+1, 0])

df2 = pd.DataFrame(data=data, columns=columns)

if os.path.exists('questions.csv'):
    df = pd.read_csv('questions.csv')
    df2 = df2.append(df, ignore_index = True)

df2.to_csv('questions.csv', index = False)