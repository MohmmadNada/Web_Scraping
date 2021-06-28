from web_scraper import __version__
from web_scraper.scraper import * 
# import pytest
# import requests
# from bs4 import BeautifulSoup

def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count(): 
    # verify that correct count of citations needed is calculated
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    axcepted = 5
    assert actual ==axcepted 

def test_get_citations_needed_report():
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')
    axcepted = 'The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.'
    assert actual[0]  == axcepted