from selenium.webdriver.common.by import By

class SteamLocators:
    STEAM_MAIN_PAGE_LOCATOR = (By.XPATH,"//*[contains(@class, 'home_page_content_title')]")
    STEAM_ABOUT_CLICK_LOCATOR = (By.XPATH,"//*[contains(@class,'menuitem') and contains(@href,'/about/')]")
    STEAM_ABOUT_PAGE_LOCATOR = (By.XPATH,"//*[@id='about_games_hero']")
    STEAM_GAMERS_IN_GAME_LOCATOR = (By.XPATH,"//*[@id='about_greeting']")
    STEAM_SHOP_PAGE_CLICK_LOCATOR = (By.XPATH,"//*[contains(@class, 'menuitem supernav') and @data-tooltip-content='.submenu_store' and contains(@href,'he')]")        
