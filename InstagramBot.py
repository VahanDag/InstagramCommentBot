from selenium.webdriver.common import keys
from InstagramDemo import username, password
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagram():
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def SıgnIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        
        emailInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(7)
        
    def GoPost(self):
        self.browser.get("https://www.instagram.com/ 'Enter the post you want to go' ")
        time.sleep(5)
        
        x=0
        while x<100:
            clickComment=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            clickComment.click()
            time.sleep(2)
        
            addComment=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            addComment.send_keys("Enter your comment")
            addComment.send_keys(Keys.ENTER)
            time.sleep(2)
    
            share=self.browser.find_element_by_css_selector(".sqdOP.yWX7d.y3zKF")
            share.click()
            time.sleep(60)
            x+=1

insta=Instagram(username,password)
insta.SıgnIn()
insta.GoPost()
