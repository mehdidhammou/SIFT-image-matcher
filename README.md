# SIFT image matcher

This is a simple image matcher using SIFT (Scale-Invariant Feature Transform) algorithm. implemented in Python using OpenCV library.

## Requirements

```bash
pip install -r requirements.txt
```

## Explanation

1. Split your image into two parts. `dataset/train` part will be used as the reference image, where for each image, `keypoints` and `descriptors`.

2. `dataset/test` part will be used as the search space for the closest target image.

## Usage

```bash
python src/main.py
```
