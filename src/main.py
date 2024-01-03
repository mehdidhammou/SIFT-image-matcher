import arguments
from config import TEST_DATASET_PATH
from lib.display import display_images, display_result
from lib.utils import init, load_images, search, train


def main():
    # load images from test dataset
    trained_images = init()

    # load images from test dataset
    test_images = load_images(path=TEST_DATASET_PATH)

    # display images from test dataset and capture the selected image and train it
    selected_image = train(display_images(test_images))

    # search through the train dataset for the selected image
    best_matches = search(selected_image, trained_images)

    # display the selected image and the top 5 matches
    display_result(selected_image, best_matches)


if __name__ == "__main__":
    main()
