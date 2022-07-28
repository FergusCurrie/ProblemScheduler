
# Add to the database 

import pandas as pd
import os 
#df = pd.read_csv('questions.csv')

#print(df)

book = input('Book:')
chapter = input('Chapter:')
num_questions = input('Number questoins:')

columns = ['book', 'chapter', 'question_number', 'reviewed', 'review_date']

# Add a check on book name 
if os.path.exists('questions.csv'):
    df = pd.read_csv('questions.csv')

create = True
if not book in pd.unique(df.book):
    create = False
    ans = input("This is a new book, create (y/n)? ")
    if ans == 'y':
        create = True
    if not create:
        print("Ok not creating a new book")

if create:

    # Make df2 
    data = []
    for i in range(int(num_questions)):
        print(i)
        data.append([book, chapter, i+1, 0, None])

    df2 = pd.DataFrame(data=data, columns=columns)

    # Append columns
    df2 = df2.append(df, ignore_index = True)

    print(df.columns == columns)
    df2.to_csv('questions.csv', index = False)