import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from annoy import AnnoyIndex
import concurrent.futures
from PIL import Image

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

def build_index(thumbnails_dir, model, index_path='thumbnail_index.ann', num_trees=10):
    # Initialize Annoy index
    feature_length = 2048  # This depends on the model output
    index = AnnoyIndex(feature_length, 'euclidean')
    
    # Prepare list of image paths
    image_paths = [os.path.join(thumbnails_dir, filename) for filename in os.listdir(thumbnails_dir)
                   if filename.lower().endswith(('png', 'jpg', 'jpeg'))]
    
    # Function to process a single image
    def process_image(path):
        features = extract_features(model, path)
        return (image_paths.index(path), features)

    # Use ThreadPoolExecutor to parallelize feature extraction
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_feature = {executor.submit(process_image, path): path for path in image_paths}
        for future in concurrent.futures.as_completed(future_to_feature):
            i, features = future.result()
            index.add_item(i, features)

    # Build the index
    index.build(num_trees)
    index.save(index_path)
    print(f"Index built and saved to {index_path}")

def main():
    thumbnails_dir = './thumbnails'
    model = load_model()
    build_index(thumbnails_dir, model)

if __name__ == "__main__":
    main()
