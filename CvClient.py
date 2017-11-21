# -*- coding: utf-8 -*-

from selenium import webdriver

# Client Campus virtual UdL
class CvClient:

    def __init__(self, webpage, username, password):
        self.webpage = webpage
        self.driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
        self.password = password
        self.username = username

    # Connectar-se al campus virtual
    def connect(self):
        self.driver.set_window_size(1280, 1024)
        self.driver.get(self.webpage)

    # Login al campus
    def login(self):
        user_field = self.driver.find_element_by_id("eid")
        user_field.send_keys(self.username)

        pw_field = self.driver.find_element_by_id("pw")
        pw_field.send_keys(self.password)

        button = self.driver.find_element_by_id("submit")
        button.click()

    # Obtenir many([1 .. 10]) anuncis
    def get_news(self, many):
        if many < 1:
            print "Ḿinim 1 anunci."
            return

        if many > 10:
            print "Màxim 10 anuncis."
            return

        # Frame de anuncis
        news_frame = self.driver.find_element_by_id("Mainc4e08c21x9db1x40cbx9f53xdd1af50aafd4")
        self.driver.switch_to_frame(news_frame)

        # Obtenir taula d anuncis
        news_table = self.driver.find_element_by_name("announcementListForm")

        # Obtenir anuncis
        news = news_table.find_elements_by_tag_name("h4")
        if many > len(news):
            many = len(news)

        news_list = []

        # Omplir la llista d'anuncis
        # Retorna una llista de diccionaris amb les claus 'subject' i 'link'
        for n in news[:many]:
            new = {}
            new["subject"] = n.find_element_by_tag_name("a").text
            new["link"] = n.find_element_by_tag_name("a").get_attribute("href")

            news_list.append(new)

        return news_list
