# --- selenium imports
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# # --- webdriver_manager
# from webdriver_manager.chrome import ChromeDriverManager
# chrome_driver_manager = ChromeDriverManager()
# chrome_driver_path = chrome_driver_manager.install()
# --- django imports
from django.test import LiveServerTestCase


class UserInterfaceTests(LiveServerTestCase):

    screenshot_folder: str = "screenshots/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)
        cls.browser.set_window_size(1920,1080) 

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()


    def WaitForLoadingBrowser(self):
        WebDriverWait(self.browser, 10).until(lambda driver: driver.find_element(By.TAG_NAME, "body"))

    def OpenBrowser(self, url: str):
        self.browser.get(f"{url}")

    def CloseBrowser(self):
        self.browser.quit()

    def SaveScreenshot(self, png: str):
        self.browser.save_screenshot(f"{self.screenshot_folder}{png}");

    def test_PokemonListUI(self):
        
        self.OpenBrowser(f"{self.live_server_url}/?page=56")
        self.WaitForLoadingBrowser()

        
        ## ----------------- check opened list
        pokemon_elements = self.browser.find_elements(By.CLASS_NAME, "card-title.text-uppercase")
        pokemon_names = [element.text.lower() for element in pokemon_elements]
        print(pokemon_names)
        container = ['cacnea', 'cacturne', 'swablu', 'altaria', 'zangoose', 'seviper']
        self.assertTrue(pokemon_names == container)
        self.SaveScreenshot("ListUI-page56.png")

        ## ----------------- click next button
        next_button = self.browser.find_element(By.CLASS_NAME, "btn.btn-info.next")
        next_button.click()

        self.WaitForLoadingBrowser()
        pokemon_elements = self.browser.find_elements(By.CLASS_NAME, "card-title.text-uppercase")
        pokemon_names = [element.text.lower() for element in pokemon_elements]

        next_container = ['lunatone', 'solrock', 'barboach', 'whiscash', 'corphish', 'crawdaunt']
        self.assertTrue(pokemon_names == next_container)
        self.SaveScreenshot("ListUI-page57.png")

    
    def test_PokemonSearchUI(self):
        self.OpenBrowser(f"{self.live_server_url}/?search=pika")
        self.WaitForLoadingBrowser()
        pokemon_elements = self.browser.find_elements(By.CLASS_NAME, "card-title.text-uppercase")
        pokemon_names = [element.text.lower() for element in pokemon_elements]
        print(pokemon_names)
        container = ['pikachu', 'pikachu-rock-star', 'pikachu-belle', 'pikachu-pop-star', 'pikachu-phd', 'pikachu-libre']
        self.assertTrue(pokemon_names == container)
        self.SaveScreenshot("SearchUI-pika.png")

    def test_PokemonUI(self):
        self.OpenBrowser(f"{self.live_server_url}//pokemon/charmander")
        self.WaitForLoadingBrowser()
        self.SaveScreenshot("PokemonUI-charmander.png")


    def test_BattleTurn(self):
        self.OpenBrowser(f"{self.live_server_url}/battle/pikachu")
        self.WaitForLoadingBrowser()

        enemy_pokemon = self.browser.find_element(By.ID, "enemy_name_id")
        user_pokemon = self.browser.find_element(By.ID, "user_name_id")
        enemy_pokemon = str.split(enemy_pokemon.text, ":")[1]
        user_pokemon = str.split(user_pokemon.text, ":")[1]
        self.assertTrue(enemy_pokemon != user_pokemon)

        self.SaveScreenshot("Battle-pikachu.png")



