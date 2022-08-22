import pandas as pd 
import numpy as np
import datetime


def edit(b, c, q):
    """
    params:
        b (str) : book
        c (str) : chapter
        q (str) : question
    Load dataframe and edit
    """
    x = datetime.datetime.now()
    df = pd.read_csv('questions.csv')

    # Find index 
    dff = df[df.book == b]
    dff = dff[dff.chapter == float(c)]
    dff = dff[dff.question_number == float(q)]
    index = dff.index[0]

    df.loc[index, 'reviewed'] = 1
    df.loc[index, 'review_date'] = x
    df.to_csv('questions.csv', index = False) 

book = input("Reviewed Book: ")
chapter = input("Reviewed Chapter: ")
questions = input("Reviewed Question (e.g. '1 2 3 4'): ")

for quest in questions.split():
    edit(book, chapter, quest)


