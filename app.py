import streamlit as st
import pickle
import pandas as pd
import base64
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

cv = CountVectorizer(max_features=5000, stop_words='english')
op = pickle.load(open('movies.pkl', 'rb'))
op2 = pd.DataFrame(op)
vec = cv.fit_transform(op2['tag']).toarray()
similarity = cosine_similarity(vec)

movies = pd.DataFrame(movies_dict)

cv=CountVectorizer(max_features=5000,stop_words='english')
vec = cv.fit_transform(['tag']).toarray()


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


add_bg_from_local('BACKGROUND.jpg')


def recommend(movie):
    movie_index = movies[movie == movies['title']].index[0]
    dist = similarity[movie_index]
    dist = list(enumerate(dist))  # to make a list of tuples to retain indices after sorting
    rt = sorted(dist, reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in rt:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies




st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select a movie : ', movies['title'].values
)

st.text('  ')
st.text('  ')
st.text('  ')

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Recommend')

if center_button:
    recommendations = recommend(selected_movie_name)
    st.text('  ')
    st.text('  ')
    for i in recommendations:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            pass
        with col2:
            pass
        with col4:
            pass
        with col5:
            pass
        with col3:
            st.write(i)

