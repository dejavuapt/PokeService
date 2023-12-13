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

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10) 

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

    def test_PokemonListUI(self):
        
        self.OpenBrowser(f"{self.live_server_url}/?page=56")
        self.WaitForLoadingBrowser()

        ## ----------------- check opened list
        pokemon_elements = self.browser.find_elements_by_class_name("card-title.text-uppercase")
        pokemon_names = [element.text for element in pokemon_elements]
        print(pokemon_names)
        container = ['cacnea', 'cacturne', 'swablu', 'altaria', 'zangoose', 'sviper']
        self.assertTrue(pokemon_names == container)

        ## ----------------- click next button
        next_button = self.browser.find_elements_by_class_name("btn.btn-info.next")
        next_button.click()

        self.WaitForLoadingBrowser()
        pokemon_elements = self.browser.find_elements_by_class_name("card-title.text-uppercase")
        pokemon_names = [element.text for element in pokemon_elements]

        next_container = ['lunatone', 'solrock', 'barboach', 'whiscash', 'corphish', 'crawdaunt']
        self.assertTrue(pokemon_names == next_container)


    
    def test_PokemonSearchUI():
        pass

    def test_PokemonFindUI():
        pass

    def test_BattleTurn():
        pass


