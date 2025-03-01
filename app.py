import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)

    if response.status_code != 200:
        return "https://via.placeholder.com/500"  # Placeholder image if API fails

    data = response.json()
    poster_path = data.get('poster_path')

    if not poster_path:
        return "https://via.placeholder.com/500"  # Placeholder image if no poster is found

    return f"https://image.tmdb.org/t/p/w500/{poster_path}"

def recommend(movie):
    if movie not in movies['title'].values:
        return [], []  # Handle cases where the movie is not found

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Top 5 similar movies
        try:
            movie_id = movies.iloc[i[0]]['id']  # Ensure 'id' is the correct column name
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]]['title'])
        except KeyError:
            continue  # Skip if 'id' column is missing

    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.header("Movie Recommendation System using Machine Learning")

# Load the data
try:
    movies = pickle.load(open('../movie_list.pkl', 'rb'))  # Ensure correct path
    similarity = pickle.load(open('../similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Required files not found. Please check 'movie_list.pkl' and 'similarity.pkl'.")

# Check if movies data is loaded correctly
if 'movies' in locals() and 'title' in movies.columns:
    movie_list = movies['title'].values
    selected_movie = st.selectbox('Type or select a movie to get recommendations', movie_list)

    if st.button('Show Movie Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        
        if recommended_movie_names:
            cols = st.columns(5)  # Create 5 columns dynamically
            for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
                with col:
                    st.text(name)
                    st.image(poster)
        else:
            st.error("No recommendations found. Try another movie.")

else:
    st.error("Movie data not loaded properly. Check your dataset.")
