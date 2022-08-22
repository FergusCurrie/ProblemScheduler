# code to schedule non
from enum import unique
import pandas as pd
import numpy as np

WEIGHT_BOYD = 2

n_reviews = input("How many reviews: ")

# Setup 
df = pd.read_csv('questions.csv')
unique_books = pd.unique(df.book)

# Review matrix
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
        sum = np.sum(x) + 1
        if book == "Boyd":
            sum = WEIGHT_BOYD * sum

        ff.append(sum)
        nn.append(f"{book}_{chapter}")
    f.append(ff)
    n.append(nn)

# Find target chapter (the one with minimum reviews )
m = np.max(np.array([len(x) for x in f])) # largest column size 
F = np.ones((len(unique_books), m)) * 9999

for gi, g in enumerate(f):
    for qi, q in enumerate(g):
        F[gi, qi] = q

# Loop through n_reviews, taking argmin and then setting value to 9999
for _ in range(int(n_reviews)):
    # Find argmin 
    z = np.unravel_index(np.argmin(F), F.shape)
    target_book, target_chapter = n[z[0]][z[1]].split('_')

    # Get the question number using chapter and book target 
    bookdf = df[df.book == target_book]
    chapterbookdf = bookdf[bookdf.chapter == float(target_chapter)]#.reset_index()
    x = chapterbookdf.loc[:, 'reviewed'].to_numpy()
    ind = x.tolist().index(0) + 1
    dataframe_index = chapterbookdf.index[ind-1] 
    df.loc[dataframe_index, "reviewed"] = 1

    # Set this question to 9999 to prevent it being selected again
    F[z[0], z[1]] += 1

    # Print 
    print(f'The next practice question is : {target_book}, Chapter {target_chapter}, Question {ind}')
    #break

# DO NOT USE DF TO SAVE, MAKE A FRESH COPY, WE OVERWRITE THE REVIEWS 
