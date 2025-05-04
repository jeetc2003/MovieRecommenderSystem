import streamlit as st
import pickle
import requests
import pandas as pd


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZWRmZTM5ODRmOGVjMWY1M2JiMmQ4NDU0ZmI0MWQ3MSIsIm5iZiI6MTc0NjExOTMwNC4wNzcsInN1YiI6IjY4MTNhYTg4YzI3YTQwMmFkN2U4MWYzMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JD5UitN2Y9yvet-9pAmJrjBrvc7Qp_hCCBumOUQTQvI"
    }

    response = requests.get(url, headers=headers)

    # print(response.text)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]



def recommend(selected):
    index = int(movies[movies["title"] == selected].index[0])
    recoMovies = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )[1:9]

    recommend_movies_posters = []
    recommend_movies = []
    for i in recoMovies:
        movie_id = movies.iloc[i[0]].id

        recommend_movies.append(movies.iloc[i[0]].title)
        # Fetch poster From API
        recommend_movies_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_posters


movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

import gzip
with gzip.open("similarity.pkl.gz", "rb") as f:
    similarity = pickle.load(f)

# similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movies = st.selectbox("Select any movie", movies["title"].values)

if st.button("Recommend"):
    recommendations,posters = recommend(selected_movies)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(recommendations[0])
    with col2:
        st.image(posters[1])
        st.text(recommendations[1])
    with col3:
        st.image(posters[2])
        st.text(recommendations[2])
    with col4:
        st.image(posters[3])
        st.text(recommendations[3])
    with col5:
        st.image(posters[4])
        st.text(recommendations[4])
    # with col6:
    #     st.text(recommendations[5])
    #     st.image(posters[5])
    # with col7:
    #     st.text(recommendations[6])
    #     st.image(posters[6])
    # with col8:
    #     st.text(recommendations[7])
    #     st.image(posters[7])
    
# For gzip

