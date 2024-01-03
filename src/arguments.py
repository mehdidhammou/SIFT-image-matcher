import argparse

import config

parser = argparse.ArgumentParser(description="Object Detection using SIFT")

parser.add_argument(
    "-c",
    "--clean",
    action="store_true",
    help="Do a clean train",
)
parser.add_argument(
    "-ct",
    "--contrastThreshold",
    type=float,
    default=0.04,
    help="Contrast threshold for keypoint detection (default: 0.04, recommended: 0.03-0.06)",
)
parser.add_argument(
    "-et",
    "--edgeThreshold",
    type=float,
    default=10,
    help="Edge threshold for keypoint detection (default: 10, recommended: 10-20)",
)

args = parser.parse_args()
