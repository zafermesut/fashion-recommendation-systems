import streamlit as st
from sklearn.neighbors import NearestNeighbors
import pickle
from PIL import Image
import os

image_features = pickle.load(open('Images_features.pkl', 'rb'))
filenames = pickle.load(open('filenames.pkl', 'rb'))



model = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='euclidean')
model.fit(image_features)


st.title("Fashion Product Recommender")

selected_image = st.selectbox('Pick an image', filenames)

selected_index = filenames.index(selected_image)

distances, indices = model.kneighbors([image_features[selected_index]])

st.write("Here are similar products:")
for idx in indices[0]:
    st.image(filenames[idx], caption=filenames[idx])

