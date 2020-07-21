from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#create python script called fbinfo which will contain your facebook username and password as shown in comment below.
"""login_username = '<username>'
    login_password = '<password>'
"""
from fbinfo import login_username, login_password


#in the string/Quotation marks enter the path to where you downloaded the chromedriver.
browser = webdriver.Chrome('<enter path here>')

"""replace www. in the facebook url with mbasic then get the link for the newly loaded facebook page"""
#navigates you to the facebook page.
fb_post = 'https://mbasic.facebook.com/story.php?story_fbid=3150247355095338&id=203462316440538&p=0&av=100001425321832&eav=AfbpuftXAXesYMn96wky2mHCNSjgXG10wGekXE7Zvij29NVkSq5rEHJPxRusEAE0qr8&refid=52'
browser.get(fb_post)
log_in = browser.find_element_by_link_text('Log In').click()

#find the username field and enter the facebook username.
username = browser.find_elements_by_css_selector('input[name=email]')
username[0].send_keys(login_username)
#find the password field and enter the password.
password = browser.find_elements_by_css_selector('input[name=pass]')
password[0].send_keys(login_password)
#find the login button and click it.
loginButton = browser.find_elements_by_css_selector('input[type=submit]')
loginButton[0].click()

"""
HTML class where the comments on the first page are located.
class can be found by using Chrome developer mode
"""
in_class = '<put class here. eg "ec">'
#for loop to get all comment text from the firts page.
for comments in browser.find_elements_by_class_name(in_class):
    with open('mwebantu_scraped_.commentstxt', 'w+') as f:
        print(comments.text, file=f)

#HTML class where comments are located for every other comments page.
in_class = '<put class here>'
#find the button to view more comments then click.
more_comments = browser.find_element_by_partial_link_text('more comments').click()
#for loop to loop through the process of clicking the view more comments button for every available page for comment, in this case 450.
for see_more in range(4):
    more_comments = browser.find_element_by_partial_link_text('more comments')
    for comments in browser.find_elements_by_class_name(in_class):
        with open('mwebantu_scraped_comments.txt', 'a') as f:
            print(comments.text, file=f)
    more_comments.click()
