from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def load_website(self):
        self.driver.get(settings['url']
        self.driver.get(settings['scroll1'])


    def goto_page(self, page):
        self.driver.find_element_by_xpath(self.driver.get(settings['lastVideo'])).click()

    def explore_show_more(self):
        self.driver.find_element_by_xpath(self.driver.get(settings['exploretheshow'])).click()
        self.driver.get(settings['scroll2'])
        self.driver.find_element_by_xpath(self.driver.get(settings['showMore'])).click()
        self.driver.get(settings['scroll1'])
        self.driver.find_element_by_xpath(self.driver.get(settings['showMore'])).click()

    def create_file(self, component):
        # Simple implementation
       # assert component in self.driver.find_element_by_tag_name('body').text, \
        #    "Component {} not found on page".format(component)
        with open("showTitlesNdurations.txt", "w") as file:
            t1 = self.driver.find_element_by_xpath(self.driver.get(settings['title1'])).getText()
            d1 = self.driver.find_element_by_xpath(self.driver.get(settings['duration1'])).getText()
            t2 = self.driver.find_element_by_xpath(self.driver.get(settings['title2'])).getText()
            d2 = self.driver.find_element_by_xpath(self.driver.get(settings['duration2'])).getText()
            t3 = self.driver.find_element_by_xpath(self.driver.get(settings['title3'])).getText()
            d3 = self.driver.find_element_by_xpath(self.driver.get(settings['duration3'])).getText()
            t4 = self.driver.find_element_by_xpath(self.driver.get(settings['title4'])).getText()
            d4 = self.driver.find_element_by_xpath(self.driver.get(settings['duration4'])).getText()
            t5 = self.driver.find_element_by_xpath(self.driver.get(settings['title5'])).getText()
            d5 = self.driver.find_element_by_xpath(self.driver.get(settings['duration5'])).getText()
            t6 = self.driver.find_element_by_xpath(self.driver.get(settings['title6'])).getText()
            d6 = self.driver.find_element_by_xpath(self.driver.get(settings['duration6'])).getText()
            t7 = self.driver.find_element_by_xpath(self.driver.get(settings['title7'])).getText()
            d7 = self.driver.find_element_by_xpath(self.driver.get(settings['duration7'])).getText()
            t8 = self.driver.find_element_by_xpath(self.driver.get(settings['title8'])).getText()
            d8 = self.driver.find_element_by_xpath(self.driver.get(settings['duration8'])).getText()
            t9 = self.driver.find_element_by_xpath(self.driver.get(settings['title9'])).getText()
            d9= self.driver.find_element_by_xpath(self.driver.get(settings['duration9'])).getText()
            t10= self.driver.find_element_by_xpath(self.driver.get(settings['title10'])).getText()
            d10 = self.driver.find_element_by_xpath(self.driver.get(settings['duration10'])).getText()
            t11 = self.driver.find_element_by_xpath(self.driver.get(settings['title11'])).getText()
            d11 = self.driver.find_element_by_xpath(self.driver.get(settings['duration11'])).getText()
            t12 = self.driver.find_element_by_xpath(self.driver.get(settings['title12'])).getText()
            d12 = self.driver.find_element_by_xpath(self.driver.get(settings['duration12'])).getText()
            t13 = self.driver.find_element_by_xpath(self.driver.get(settings['title13'])).getText()
            d13 = self.driver.find_element_by_xpath(self.driver.get(settings['duration13'])).getText()
            file.write((t1,d1)+'\n'+(t1,d1)+'\n'(t1,d1)+'\n'(t2,d2)+'\n'(t3,d3)+'\n'(t4,d4)+'\n'(t5,d5)+'\n'(t6,d6)+'\n'(t7,d7)+'\n' /
                (t8, d8) + '\n'(t9,d9)+'\n'(t10,d10)+'\n'(t11,d11)+'\n'(t12,d12)+'\n'(t13,d13))
            file.close()



webapp = WebApp.get_instance()
