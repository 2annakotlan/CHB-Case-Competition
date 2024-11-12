# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page


# Example usage with two image URLs
image_url_1 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 1.png"
image_url_2 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 2.png"
get_login_signup_page(image_url_1, image_url_2)

get_login_signup_page("https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 2.png")
#get_friend_swiping_page(friend_swiping_df)
