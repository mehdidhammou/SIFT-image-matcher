import os
import pickle
from typing import Sequence

import cv2 as cv
from cv2 import DMatch

from arguments import args
from classes import (
    Image,
    TrainedImage,
    TrainedImageDeserializer,
    TrainedImageSerializer,
)
from config import (
    ACCEPTED_EXTENSIONS,
    MAX_MATCH_DISTANCE,
    TRAIN_DATASET_PATH,
    TRAINED_IMAGES_PATH,
)


def init() -> list[TrainedImage]:
    if args.clean or not os.path.exists(TRAINED_IMAGES_PATH):
        trained_images = [train(image) for image in load_images(TRAIN_DATASET_PATH)]

        with open(TRAINED_IMAGES_PATH, "wb") as f:
            serialized_images = [
                TrainedImageSerializer.serialize(image=image)
                for image in trained_images
            ]
            pickle.dump(serialized_images, f)

        return trained_images
    else:
        with open(TRAINED_IMAGES_PATH, "rb") as f:
            serialized_images = pickle.load(f)
            return [
                TrainedImageDeserializer.deserialize(data=image)
                for image in serialized_images
            ]


def train(image: Image) -> TrainedImage:
    img = cv.imread(image.path, cv.IMREAD_GRAYSCALE)
    sift = cv.SIFT_create(contrastThreshold=args.contrastThreshold)
    sift.setEdgeThreshold(args.edgeThreshold)
    
    print(f"Training {image.path}")
    print(f"Edge threshold: {sift.getEdgeThreshold()}")
    print(f"Contrast threshold: {sift.getContrastThreshold()}")
    
    kps, des = sift.detectAndCompute(img, None)
    return TrainedImage(path=image.path, des=des, kps=kps)


def load_images(path: str) -> list[Image]:
    if path is None:
        raise ValueError("Path cannot be None")
    images: list[Image] = []
    # iterate through all images in the test dataset and add them to the list
    for file in os.listdir(path):
        if os.path.splitext(file)[1] in ACCEPTED_EXTENSIONS:
            image_path = os.path.join(path, file)
            images.append(Image(image_path))

    return images


def search(
    selected_image: TrainedImage, trained_images: list[TrainedImage]
) -> list[TrainedImage]:
    bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)
    best_matches: list[TrainedImage] = []

    for image in trained_images:
        matches: Sequence[DMatch] = bf.match(selected_image.des, image.des)
        matches = sorted(matches, key=lambda x: x.distance)

        image.matches = [m for m in matches if m.distance < MAX_MATCH_DISTANCE]
        best_matches.append(image)

    return best_matches
