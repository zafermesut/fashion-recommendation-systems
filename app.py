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

image_path = os.path.join(selected_image)
st.write(f"Image path: {image_path}")  
image = Image.open(image_path)
st.image(image, caption=selected_image, use_column_width=True)


selected_index = filenames.index(selected_image)

distances, indices = model.kneighbors([image_features[selected_index]])

st.write("Here are similar products:")
for idx in indices[0]:
    st.image(filenames[idx], caption=filenames[idx])

