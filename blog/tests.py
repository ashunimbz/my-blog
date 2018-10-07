from django.test import TestCase
import unittest
from django.test import Client
from django.urls import reverse
from .models import Post
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
# Create your tests here.

class SimpleLinksWorking(TestCase):

    def test_simple_link(self):
        response =  self.client.get('/')
        self.assertEquals(response.status_code , 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('blog:blog_url'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Ashish Nimbalkar</title>')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:blog_url'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogintro.html')

    def test_blog_simple_link(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)


class IsDataBaseWorking(TestCase):
    def setUp(self):
        obj  =  Post.objects.create(author =  "test_author" ,title = "test_title",text = "test_text" , desc = "test_desc",verified = False )

    def test_info(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response , "test_text")


class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("CHECK OUT MY BLOG").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ashu the great'])[1]/following::footer[1]").click()
        driver.find_element_by_link_text("WRITE FOR ME").click()
        driver.find_element_by_id("id_author").click()
        driver.find_element_by_id("id_author").clear()
        driver.find_element_by_id("id_author").send_keys("test_author")
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_title | ]]
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("test_titile")
        driver.find_element_by_id("id_text").click()
        driver.find_element_by_id("id_text").clear()
        driver.find_element_by_id("id_text").send_keys("This is to check if everything works correctly  ?")
        driver.find_element_by_id("id_desc").click()
        driver.find_element_by_id("id_desc").clear()
        driver.find_element_by_id("id_desc").send_keys("does it ?")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::input[2]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)







