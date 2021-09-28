from urllib.parse import quote
from selenium import webdriver
import json

browser = webdriver.Chrome()

file = open("conf.json")
content = file.read()
data = json.loads(content)
file.close()

quotesText = []
quotesTag = []
authorinf = []
save = False
authorLink = ""

def exportInformation(quotesText, quotesTag, authorinf):
    for i in range(0, len(quotesText)):
        print(quotesText[i])
        print(quotesTag[i])
    
    for x in authorinf:
        print(x)

def verifyAuthor(name, tag):
    tagInArray = tag.split()
    for t in tagInArray:
        if (name == data["author"]):
            return True

    if (name == data["author"]):
        return True
    else:
        return False

def saveQuote(thisIsAuthor, text, tag):
    if (thisIsAuthor):
        quotesText.append(text)
        quotesTag.append(tag)

def saveAuthor(a):
    browser.get(a)
    authorinf.append(browser.find_element_by_class_name('author-title'))
    authorinf.append(browser.find_element_by_class_name('author-born-date').text)
    authorinf.append(browser.find_element_by_class_name('author-born-location').text)
    authorinf.append(browser.find_element_by_class_name('author-description').text)

browser.get(data["url"])

for x in range(0, int(data["pages_number"]) - 1):
    names = browser.find_elements_by_class_name('author')
    texts = browser.find_elements_by_class_name('text')
    tags = browser.find_elements_by_class_name('tags')
    links = browser.find_elements_by_xpath("//*[contains(text(),'(about)')]")

    for n in range(0, len(names)):
        name = names[n].text
        text = texts[n].text
        tag = tags[n].text
        

        thisIsAuthor = verifyAuthor(name, tag)

        if (thisIsAuthor and not save):
            save = True
            authorLink = links[n].get_attribute('href')

        saveQuote(thisIsAuthor, text, tag)

    if (x < int(data["pages_number"]) - 1):
        next = browser.find_element_by_xpath("//*[contains(text(),'→')]")
        next.click()


saveAuthor(authorLink)

browser.quit()

exportInformation(quotesText, quotesTag, authorinf)