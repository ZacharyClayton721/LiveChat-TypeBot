## Simple code that shows how to automate website functions with Selenium

## Selenum Imports
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,SessionNotCreatedException
from selenium.webdriver.chrome.options import Options

## Creates a Chrome session with custom options
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation", "enable-logging"])
## Disables functions related to passwords
prefs = {"credentials_enable_service" : False,
                    "profile.password_manager_enabled" : False}
## Adds options to the chrome profile
options.add_experimental_option("prefs", prefs)
## Create the Chrome session with custom options
driver = webdriver.Chrome('chromedriver',options=options)

## Navigate to the website
driver.get('https://www.livechat.com/typing-speed-test/#/')
## Maximize the Chrome window (For aesthetic purposes)
driver.maximize_window()
## Xpath that stores the words to type
xpath = '/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span'
words = []
## Only 5 words are loaded in advance at the xpath
for x in range(1,6):
    words.append(driver.find_element_by_xpath(xpath+'['+str(x)+']').text)

## Find the element to submit words to     
submission = driver.find_element_by_id('test-input')
driver.implicitly_wait(.1)
while True:
    ## Sends the first word in the list to the submission box
    submission.send_keys(words[0]+ ' ')
    ## Word has already been typed so it gets removed
    words.pop(0)
    ## Eventually the website will run out of words to give the program
    try:
        ## 5th word gets added to end of word list
        ## if the element exists
        words.append(driver.find_element_by_xpath(xpath+'[5]').text)
    except:
        ## This signals that no more new words are present
        ## So the remaining words get sent to finish out execution
        for x in words:
            submission.send_keys(x+' ')
        break

## Uses the number in the countdown timer to signal
## how long it took for the website to run out of new words
print('Completed in '+str(60-int(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[1]/div/div[1]/div/div[1]').text))+' seconds')

## Allows user to exit the program
exit_showcase = input('Press enter to close the browser and end the program ')
## Closes the Chrome session made and ends the process
driver.quit()
       
        
    

