# SIFT Image matcher

## Overview
A Python-based image matching application using OpenCV's SIFT (Scale-Invariant Feature Transform) algorithm to find similar images in a training dataset.

## Features
- SIFT feature detection and description
- Brute-force matching of image features
- Serialization of trained image data
- Configurable SIFT parameters
- Interactive image selection and matching

## Requirements
- Python 3.8+
- OpenCV
- Pickle

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Modify `config.py` to set:
- `TRAIN_DATASET_PATH`: Path to training images
- `TEST_DATASET_PATH`: Path to test images
- `MAX_MATCH_DISTANCE`: Maximum distance for feature matching
- `ACCEPTED_EXTENSIONS`: Supported image file types

## Usage
```bash
python main.py [--clean] [--contrastThreshold VALUE] [--edgeThreshold VALUE]
```

### Command Line Arguments
- `--clean`: Force retraining of images
- `--contrastThreshold`: SIFT contrast threshold
- `--edgeThreshold`: SIFT edge threshold

## How It Works
1. Load and train images from training dataset
2. Detect SIFT keypoints and descriptors
3. Display test images for selection
4. Match selected image against trained images
5. Display top matching results

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License
