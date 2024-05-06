import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from annoy import AnnoyIndex

def load_model():
    # Load the pre-trained ResNet50 model for feature extraction
    return ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(model, img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_array_expanded)
    # Extract features
    features = model.predict(img_preprocessed)
    return features.flatten()

def load_index(index_path, feature_length):
    # Load the Annoy index
    index = AnnoyIndex(feature_length, 'euclidean')
    index.load(index_path)
    return index

def find_similar_images(target_image_path, model, index, n_neighbors=5):
    # Extract features from the target image
    target_features = extract_features(model, target_image_path)
    
    # Find the nearest neighbors
    neighbors = index.get_nns_by_vector(target_features, n_neighbors, include_distances=True)
    return neighbors

def main():
    model = load_model()
    index_path = 'thumbnail_index.ann'
    feature_length = 2048  # Should match the feature length used in building the index
    index = load_index(index_path, feature_length)
    
    target_image_path = './thumbnails/(m=qU5WO7XbeafTGgaaaa)(mh=kIWhRaJVkXVhtyzm)0.jpg'  # Update with your target image path
    neighbors = find_similar_images(target_image_path, model, index)
    
    print("Nearest Neighbors (IDs and distances):", neighbors)

if __name__ == "__main__":
    main()
