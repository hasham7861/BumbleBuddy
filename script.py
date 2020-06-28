from bumbleSwiper import get_candidate, quit_browser, instantiate_browser, sigin_bumble, delete_folder_images
from bumbleAI import similar_face


def start_script():
    driver = instantiate_browser()
    is_signed_in = sigin_bumble(driver)
    your_type_img_path = "images/your-type/marinda.png"
    total_swipes = 10
    for i in (0, total_swipes, 1):

        candidate_img_path, dislike_button, like_button = get_candidate(
            driver, is_signed_in)

        # only when image is cropped properly
        if candidate_img_path and dislike_button and like_button:
            is_my_type = similar_face(
                your_type_img_path, candidate_img_path)

            if is_my_type:
                like_button.click()
            else:
                dislike_button.click()

    quit_browser(driver)

    return "swiped {total_swipes} times"


start_script()
delete_folder_images("images/crop")
delete_folder_images("images/download")
