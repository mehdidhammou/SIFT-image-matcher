import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseEvent
from config import DISPLAY_COLUMNS, DISPLAY_WIDTH
from classes.image import Image
from classes.trained_image import TrainedImage


def display_images(images: list[Image]) -> Image:
    # display images in a grid
    num_rows = (len(images) + DISPLAY_COLUMNS - 1) // DISPLAY_COLUMNS

    # capture the selected image
    selected_image_idx = None

    def on_click(event: MouseEvent):
        nonlocal selected_image_idx
        selected_image_idx = int(event.inaxes.get_title())
        plt.close()

    fig, axes = plt.subplots(num_rows, DISPLAY_COLUMNS, figsize=(20, 10))

    for idx, ax in enumerate(axes.ravel()):
        if idx < len(images):
            image = plt.imread(images[idx].path)
            ax.imshow(image)
            ax.axis("off")
            ax.set_title(idx)

            ax.figure.canvas.mpl_connect("button_press_event", on_click)
        else:
            ax.axis("off")

    plt.tight_layout()
    plt.show()

    return images[selected_image_idx]


def display_result(selected_image: TrainedImage, best_matches: list[TrainedImage]):
    image1 = cv.imread(selected_image.path)
    
    cv.namedWindow("Matches", cv.WINDOW_NORMAL)

    for image in best_matches:
        match_img = cv.imread(image.path)
        matching_result = cv.drawMatches(
            image1,
            selected_image.kps,
            match_img,
            image.kps,
            image.matches[:10],
            None,
            flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        )

        DISPLAY_HEIGHT = int(
            (DISPLAY_WIDTH / matching_result.shape[1]) * matching_result.shape[0]
        )

        matching_result_resized = cv.resize(
            matching_result, (DISPLAY_WIDTH, DISPLAY_HEIGHT)
        )

        cv.resizeWindow("Matches", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        cv.imshow("Matches", matching_result_resized)
        cv.waitKey(0)

    cv.destroyAllWindows()
