from bumbleSwiper import get_candidate, quit_browser
from bumbleAI import similar_face


def start_script():
    candidate_img_path, dislike_btn, like_btn, browser_driver = get_candidate()
    your_type_img_path = "images/your-type/marinda.png"
    total_swipes = 10
    for i in (0, total_swipes, 1):
        is_my_type = similar_face(
            your_type_img_path, candidate_img_path)
        if is_my_type:
            like_btn.click()
        else:
            dislike_btn.click()

    quit_browser(browser_driver)

    return "swiped {total_swipes} times"


start_script()
