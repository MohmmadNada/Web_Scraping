import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(inputURL):
    '''
    get_citations_needed takes in a url ,record which passages need citations and returns an integer(count citations needed)
    '''
    URL=inputURL
    page=requests.get(URL)
    soup =BeautifulSoup(page.content,'html.parser')# all html content
    allParagraphWithSpan=soup.find_all('span',text='citation needed')
    citations_needed_count=len(allParagraphWithSpan)
    return citations_needed_count

def get_citations_needed_report(url):
    '''identify those  AND include the relevant passage
    '''
    page=requests.get(url)
    soup =BeautifulSoup(page.content,'html.parser')# all html content
    allSpan=soup.find_all('span',text='citation needed')
    paragraphs=[]
    for paragraph in allSpan:
        # paragraph.parent.parent.parent.parent.text
        paragraphs.append(paragraph.parent.parent.parent.parent.text.strip())    
    return paragraphs
    
# print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))
print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
