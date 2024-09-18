# Fashion Product Recommender System

This is a content-based fashion product recommender system built using **k-Nearest Neighbors (k-NN)** with **Euclidean distance**. The system recommends similar fashion products based on image features.

The app is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/zafermbilen/fashion-recommendation-systems) using **Streamlit**, allowing users to easily interact with the model and get product recommendations.

## Dataset

The dataset used for this project is from [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small). It contains images of fashion products, and the system utilizes pre-extracted image features from this dataset for product recommendation.

## Model

- **Algorithm**: k-Nearest Neighbors (k-NN)
- **n_neighbors**: 6
- **Distance Metric**: Euclidean

## Files

- `app.py`: The main Streamlit application.
- `Images_features.pkl`: Pre-extracted image features used for similarity calculation.
- `filenames.pkl`: List of image file paths corresponding to the images in the dataset.

## Hugging Face Space

The application is live and can be accessed on Hugging Face Spaces here: [Fashion Product Recommendation System](https://huggingface.co/spaces/zafermbilen/fashion-recommendation-systems).

This interactive app allows users to explore and receive recommendations for similar fashion products based on the input product's image.
