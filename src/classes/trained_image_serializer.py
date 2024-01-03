from cv2 import KeyPoint
from classes.trained_image import TrainedImage


class TrainedImageSerializer:
    @staticmethod
    def serialize(image: TrainedImage) -> dict:
        return {
            "path": image.path,
            "des": image.des,
            "kps": [TrainedImageSerializer.serialize_keypoint(kp) for kp in image.kps],
        }

    @staticmethod
    def serialize_keypoint(kp: KeyPoint) -> dict:
        return {
            "x": kp.pt[0],
            "y": kp.pt[1],
            "angle": kp.angle,
            "class_id": kp.class_id,
            "octave": kp.octave,
            "pt": kp.pt,
            "response": kp.response,
            "size": kp.size,
        }
