import pickle
import streamlit as st
import requests

st.header('Book Recommender System')
books = pickle.load(open('book_list2.pkl','rb'))
similarity = pickle.load(open('similarity2.pkl','rb'))

book_list = books['title'].values

selected_book = st.selectbox("Select a Book",book_list)

def fetch_poster(book_id):
    poster_path = "http://covers.openlibrary.org/b/isbn/{}-L.jpg".format(book_id)
    return poster_path

def recommender(x):
    index = books[books['title']== x ].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommend_book_names = []
    recommend_book_poster = []
    for i in distances[1:6]:
        book_id = books.iloc[i[0]].isbn
        recommend_book_poster.append(fetch_poster(book_id))
        recommend_book_names.append(books.iloc[i[0]].title)
    return recommend_book_names,recommend_book_poster

if st.button('Show Recommendation'):
    recommend_book_names,recommend_book_poster = recommender(selected_book)
    col1,col2,col3,col4,col5 = st.beta_columns(5)
    with col1:
        st.text(recommend_book_names[0])
        st.image(recommend_book_poster[0])
    with col2:
        st.text(recommend_book_names[1])
        st.image(recommend_book_poster[1])
    with col3:
        st.text(recommend_book_names[2])
        st.image(recommend_book_poster[2])
    with col4:
        st.text(recommend_book_names[3])
        st.image(recommend_book_poster[3])
    with col5:
        st.text(recommend_book_names[4])
        st.image(recommend_book_poster[4])
