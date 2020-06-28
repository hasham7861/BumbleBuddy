from bumbleSwiper import instantiate_browser, sigin_bumble, get_action_buttons, download_candidate_image, quit_browser
from bumbleAI import crop_face, similar_face


def start_script():
    browser_driver = instantiate_browser()
    is_signed_in = sigin_bumble(browser_driver)
    if not is_signed_in:
        return "login_err: input in the right captcha code and rerun script"

    dislike_button, like_button = get_action_buttons(browser_driver)
    candidate_img_path = download_candidate_image(browser_driver)
    print(candidate_img_path)
    candidate_img_cropped_path = crop_face(candidate_img_path)
    # your_type_img_path = "your_type/marinda.png"

    # total_swipes = 10
    # for i in (0, total_swipes, 1):
    #     is_my_type = similar_face(
    #         your_type_img_path, candidate_img_cropped_path)
    #     if is_my_type:
    #         like_button.click()
    #     else:
    #         dislike_button.click()

    # quit_browser(browser_driver)

    # return "swiped {total_swipes} times"


start_script()
