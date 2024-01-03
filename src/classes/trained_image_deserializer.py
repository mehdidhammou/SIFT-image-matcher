from cv2 import KeyPoint
from classes.trained_image import TrainedImage


class TrainedImageDeserializer:
    @staticmethod
    def deserialize(data: dict) -> TrainedImage:
        return TrainedImage(
            path=data["path"],
            des=data["des"],
            kps=[
                TrainedImageDeserializer.deserialize_keypoint(kp) for kp in data["kps"]
            ],
        )

    @staticmethod
    def deserialize_keypoint(data: dict) -> KeyPoint:
        # deserialize the dictionary to a KeyPoint object
        return KeyPoint(
            x=data["x"],
            y=data["y"],
            angle=data["angle"],
            class_id=data["class_id"],
            octave=data["octave"],
            response=data["response"],
            size=data["size"],
        )
