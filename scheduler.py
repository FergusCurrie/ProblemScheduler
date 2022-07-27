# code to schedule non
from enum import unique
import pandas as pd
import numpy as np


# Setup 
df = pd.read_csv('questions.csv')
unique_books = pd.unique(df.book)

# Algorithm to find which chapter to
f = [] # total data store mxn
n = [] # total name store
for book in unique_books:
    ff = [] # one column of total score
    nn = [] # one colum of name store
    bookdf = df[df.book == book]
    unique_chapters = pd.unique(bookdf.chapter)
    for chapter in sorted(unique_chapters):
        chapterbookdf = bookdf[bookdf.chapter == chapter].reset_index()
        x = chapterbookdf.loc[:, 'reviewed'].to_numpy()
        ff.append(np.sum(x))
        nn.append(f"{book}_{chapter}")
    f.append(ff)
    n.append(nn)

# Find target chapter (the one with minimum reviews )
m = np.max(np.array([len(x) for x in f])) # largest column size 
F = np.ones((len(unique_books), m)) * 9999
z = np.argmin(F, axis=1)
target_book, target_chapter = n[z[0]][z[1]].split('_')

# Get the question number using chapter and book target 
bookdf = df[df.book == target_book]
chapterbookdf = bookdf[bookdf.chapter == float(target_chapter)].reset_index()
x = chapterbookdf.loc[:, 'reviewed'].to_numpy()
ind = x.tolist().index(0) + 1

# Print 
print(f'The next practice question is : {target_book}, Chapter {target_chapter}, Question {ind}')


