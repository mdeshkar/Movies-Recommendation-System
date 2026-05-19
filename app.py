import streamlit as st
import nltk
import sklearn
import pandas as pd
import pickle
import joblib

st.title("Movie Recommendation System")

with open("movies.pickle", 'rb') as m:
    movies = pickle.load(m)

similarity = joblib.load("similarity.joblib")

movie_names = movies['title'].values

def recommend(name_movie, top_n=5):

    movie = name_movie.lower()

    if movie not in movies['title'].values:
        print(f"Movie '{movie}' not found!")
        return

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:top_n+1]

    recommendations = []

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

name_movie = st.selectbox("Enter the Movie Name", movie_names)

if st.button("Recommend"):
    r = recommend(name_movie)

    st.write("Recommended Movies are :")

    for i in r:
        st.write(i)



