import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:/Users/440G1/chromedriver.exe")
        self.driver.get("http://www.python.org")

    # TestCase class the name test_ will auto run
    # def test_example(self):
    #     print("Test")
    #
    # def not_a_test(self):
    #     print("compare to test_example")
    #
    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert  mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()