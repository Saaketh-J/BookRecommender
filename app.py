import streamlit as st
import pandas as pd
from ipynb.fs.full.main import pred_books, get_info

books = pd.read_csv('./Data/books.csv')
titles = list(books['title'])


options = st.multiselect('What are your favorite books?', titles)

if st.button('Give Me Recommendations'):
    pred_ids = pred_books(options)
    extra_info = {x: [] for x in pred_ids}
    for i in pred_ids:
        extra_info[i] += ([get_info(i).title.item()])
        extra_info[i] += ([get_info(i).average_rating.item()])
        extra_info[i] += ([get_info(i).authors.item()])
    cols = st.columns(3)
    cols[0].write('Title')
    cols[1].write('Average Rating')
    cols[2].write('Author')
    for i in pred_ids:
        cols = st.columns(3)
        cols[0].write(extra_info.get(i)[0])
        cols[1].write(extra_info.get(i)[1])
        cols[2].write(extra_info.get(i)[2])
