from string_utils import StringUtils
from Page import SearchHelper
from metadriver import driver_single

def test_1(browser):
    steam_main_page = SearchHelper()
    assert steam_main_page.search_main_page_locator().text
        
def test_2(browser):
    steam_main_page = SearchHelper()
    steam_main_page.click_on_about_button()
    assert steam_main_page.search_about_page_locator() != None
        
def test_3(browser):
    steam_main_page = SearchHelper()
    string_data = steam_main_page.count_player()
    data =  StringUtils.get_regular(string_data.text) #data[0] - число игроков онлайн, data[1] - число игроков сеййчас
    for i in range (2):
        data[i] = StringUtils.get_replace(data[i])
    assert data[0] > data[1]
        
def test_4(browser):
    steam_main_page = SearchHelper()
    steam_main_page.click_on_store()
    assert len(steam_main_page.search_main_page_locator().text) > 0
