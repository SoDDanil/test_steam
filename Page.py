from BasePage import BasePage
from SteamLocators import SteamLocators

class SearchHelper(BasePage):
    
    def click_on_about_button(self):
        return self.find_element(SteamLocators.STEAM_ABOUT_CLICK_LOCATOR).click()
    def count_player(self):
        return self.find_element(SteamLocators.STEAM_GAMERS_IN_GAME_LOCATOR)
    def click_on_store(self):
        return self.find_element(SteamLocators.STEAM_SHOP_PAGE_CLICK_LOCATOR).click()
    def search_main_page_locator(self):
        return  self.find_element(SteamLocators.STEAM_MAIN_PAGE_LOCATOR)
    def search_about_page_locator(self):
        return  self.find_element(SteamLocators.STEAM_ABOUT_PAGE_LOCATOR)
