from .image import Image
from cv2 import KeyPoint


class TrainedImage(Image):
    def __init__(self, path: str, des: list, kps: list[KeyPoint], matches: list = None):
        super().__init__(path)
        self.des = des
        self.kps = kps
        self.matches = matches
