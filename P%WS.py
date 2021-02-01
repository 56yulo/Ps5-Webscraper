from selenium import webdriver
from pynput.keyboard import Controller
from time import sleep
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

keyboard = Controller()



ELE = False


class Dis :
    def __init__(self, PW, UN) :
        self.driver = webdriver.Chrome()
        #self.url = "https://www.bestbuy.ca/en-ca/product/dji-mavic-mini-quadcopter-drone-fly-more-combo/13985755"
        sleep(50)
        self.url = "https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184"
        self.xpath = "//button[@class='button_2Xgu4 primary_oeAKs addToCartButton_1op0t addToCartButton regular_cDhX6']"

    def run(self):
        self.driver.get(self.url)
        sleep(0.5)
        try :
            element = self.driver.find_element_by_xpath(self.xpath)
        except :
            print("None")
            self.driver.close()
            Dis(PW, UN).run()
            return



        if (element.is_enabled() == True) :
            print("Working")
            self.driver.get('https://www.instagram.com/')
            sleep(3)
            self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
                .send_keys(UN)
            sleep(.5)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
                .send_keys(PW)
            sleep(.5)
            self.driver.find_element_by_xpath('//button[@type="submit"]') \
                .click()
            sleep(4)
            self.driver.find_element_by_xpath('//button[@type="button"]') \
                .click()
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
                .click()
            sleep(2)

            #spacer

            self.driver.get('https://www.instagram.com/canadazi/')
            sleep(.5)
            self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
            sleep(2)
            mbox = self.driver.find_element_by_tag_name('textarea')
            mbox.send_keys('PS5 is back in stock at bestbuy: https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184')
            sleep(1)
            mbox.send_keys(Keys.RETURN)
            sleep(1)

            #spacer

            self.driver.get('https://www.instagram.com/dev0n56/')
            sleep(.5)
            self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
            sleep(2)
            mbox = self.driver.find_element_by_tag_name('textarea')
            mbox.send_keys(
                'PS5 is back in stock at bestbuy: https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184')
            sleep(1)
            mbox.send_keys(Keys.RETURN)
            sleep(1)

            #Spacer

            self.driver.get('https://www.instagram.com/connor.corkill/')
            sleep(.5)
            self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
            sleep(2)
            mbox = self.driver.find_element_by_tag_name('textarea')
            mbox.send_keys(
                'PS5 is back in stock at bestbuy: https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184')
            sleep(1)
            mbox.send_keys(Keys.RETURN)
            sleep(1)

            # Spacer

            self.driver.get('https://www.instagram.com/logan_flash06/')
            sleep(.5)
            self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
            sleep(2)
            mbox = self.driver.find_element_by_tag_name('textarea')
            mbox.send_keys(
                'PS5 is back in stock at bestbuy: https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184')
            sleep(1)
            mbox.send_keys(Keys.RETURN)
            sleep(1)

            self.driver.close()
            Dis(PW, UN).run()


if __name__ == '__main__' :
    dis = Dis(PW, UN)
    dis.run()