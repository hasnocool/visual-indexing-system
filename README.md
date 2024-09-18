# Visual Indexing System
=====================================

Hey there, fellow developer! I'm super excited to share my latest project - the **Visual Indexing System** (VIS). This project is a showcase of how computer vision and indexing can be used together to create an efficient way to search for similar images.

## Project Title
---------------

The Visual Indexing System is an open-source Python library that uses deep learning models to extract features from images and then indexes them using the Annoy library. This allows for fast and efficient retrieval of similar images based on their visual content.

## Description
-------------

I built this to create a system where I could quickly find similar images in my photo library, but it can be used for any type of image collection. The VIS uses a pre-trained ResNet50 model to extract features from images, which are then indexed using Annoy. This allows for fast and efficient retrieval of similar images based on their visual content.

One cool feature is the ability to search for similar images in parallel using multi-threading, making it possible to index thousands of images quickly.

## Features
------------

* **Deep Learning-based Feature Extraction**: Uses a pre-trained ResNet50 model to extract features from images.
* **Annoy Indexing**: Indexes the extracted features using Annoy, allowing for fast and efficient retrieval of similar images.
* **Multi-threading Support**: Allows for parallel search and indexing of images.

## Installation
--------------

To install the VIS, simply run the following command:

```bash
pip install tensorflow annoy pillow
```

Then clone this repository and navigate to the `visual-indexing-system` directory. You can then run the code using Python 3.x.

## Usage
---------

To use the VIS, you'll need to create a directory of thumbnails and then build an index using the `build_index.py` script. Once the index is built, you can search for similar images using the `search_similiarity_index.py` script.

Here's some example code:

```python
# Build an index on a directory of thumbnails
python build_index.py --thumbnails_dir './thumbnails' --num_trees 10

# Search for similar images in the index
python search_similiarity_index.py --target_image_path './thumbnails/(m=qU5WO7XbeafTGgaaaa)(mh=kIWhRaJVkXVhtyzm)0.jpg'
```

## Contributing
--------------

Contributions are more than welcome! If you'd like to contribute to the VIS, please fork this repository and submit a pull request.

## License
--------

The Visual Indexing System is released under the MIT license. See `LICENSE.md` for details.

## Tags/Keywords
----------------

[Computer Vision], [Indexing], [Deep Learning], [Multi-threading], [Python]

---

This README was written by yours truly, hasnocool. I hope you find it helpful!