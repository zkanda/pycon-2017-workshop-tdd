from selenium import webdriver
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_the_page(self):

        # JayR went to the website, he notice the title as "Surveyor".
        self.browser.get('http://localhost:8000')
        self.assertIn('Surveyor', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('header').text
        self.assertIn('Surveyor', header_text)

        # He saw a button that invites him to send an SMS and clicked the button
        send_sms_page_button = self.browser.find_element_by_id('id_send_sms_page')
        self.assertEqual(
            send_sms_page_button.text,
            "Want to send SMS, click here!"
        )

        send_sms_page_button.click()
        time.sleep(1)
        send_sms_page = self.browser.current_url
        self.assertEqual(send_sms_page, "http://localhost:8000/send_sms/")


        # On the next page, there's header that says:
        # Fill this information to send an SMS
        header_text = self.browser.find_element_by_tag_name('header').text

        self.assertIn('Fill this information to send an SMS', header_text)

        # He notice that there are 2 fields and a button.
        # The first field is for adding contact information.

        input_contact = self.browser.find_element_by_id('id_contact')
        self.assertEqual(
            input_contact.get_attribute('placeholder'),
            'Enter phone number'
        )

        # The second field is for adding the message.
        input_message = self.browser.find_element_by_id('id_message')
        self.assertEqual(
            input_message.get_attribute('placeholder'),
            'Enter your message'
        )
        # Lastly a button to submit the form.
        send_sms_button = self.browser.find_element_by_id('id_send_sms')
        self.assertEqual(
            send_sms_button.get_attribute('value'),
            "Send SMS"
        )


        # So he add his contact number on the first field. 09152087801
        input_contact.send_keys("09152087801")

        # And added message on the second.
        # What is your Full Name?
        input_message.send_keys("What is your Full Name?")

        # Lastly he clicked the submit button!
        send_sms_button.click()
        time.sleep(1)

        # After clicking the button he is immediately redirected to the home page.
        # With a notification that says, "Message sent, please wait for reply!"
        message_notification = self.browser.find_element_by_css_selector('.messages li:first-child').text()

        # He still didn't see any reply.
        table_replies = self.browser.find_element_by_id("id_table_replies")
        rows = table_replies.find_element_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "" for row in rows)
        )

        # He got a notification from his phone, check and recieve the message
        # that he sent earlier. He immediately replied:
        # Elpedio Adoptante

        # He tries to refresh the page and saw the message like this.
        # Number        Name
        # 09152087801   JayR
        self.browser.refresh()
        table_replies = self.browser.find_element_by_id("id_table_replies")
        rows = table_replies.find_element_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "09152087801   JayR" for row in rows)
        )


        # He is now happy and closes the browser.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
