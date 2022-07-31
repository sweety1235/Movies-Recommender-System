import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

st.title('Movie Recommender System !!!')

movie_dict = pickle.load(open('movie_dict.pkl','rb'))

movies = pd.DataFrame(movie_dict)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
     recommended_movie_names = []
     recommended_movie_posters = []
     for i in distances[1:11]:
          # fetch the movie poster
          movie_id = movies.iloc[i[0]].movie_id
          recommended_movie_posters.append(fetch_poster(movie_id))
          recommended_movie_names.append(movies.iloc[i[0]].title)

     return recommended_movie_names, recommended_movie_posters

similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie = st.selectbox(
     'Would you like to Search Similar Movies',
     movies['title'].values)
st.write('You selected: ', selected_movie)

if st.button('Show Movies Recommendations -->'):
     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
          st.image(recommended_movie_posters[0])
          st.caption(recommended_movie_names[0])
     with col2:
          st.image(recommended_movie_posters[1])
          st.caption(recommended_movie_names[1])
     with col3:
          st.image(recommended_movie_posters[2])
          st.caption(recommended_movie_names[2])
     with col4:
          st.image(recommended_movie_posters[3])
          st.caption(recommended_movie_names[3])
     with col5:
          st.image(recommended_movie_posters[4])
          st.caption(recommended_movie_names[4])