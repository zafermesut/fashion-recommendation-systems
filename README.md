# Fashion Product Recommender System

A content-based fashion product recommender system built using **k-Nearest Neighbors (k-NN)** with **Euclidean distance**. The app is developed in **Streamlit** and recommends similar products based on image features.

## Dataset

The dataset used is from [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small). The model uses pre-extracted image features to recommend similar products.

## Model

- **Algorithm**: k-Nearest Neighbors (k-NN)
- **n_neighbors**: 6
- **Distance Metric**: Euclidean

## Files

- `app.py`: The Streamlit app.
- `Images_features.pkl`: Pre-extracted image features.
- `filenames.pkl`: List of image file paths.
