import unittest
import re

class TestHTMLForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("index.html", "r", encoding="utf-8") as file:
            cls.html = file.read()

    def test_form_exists(self):
        self.assertRegex(self.html, r"<form\b")

    def test_name_field(self):
        self.assertRegex(
            self.html, r'<input[^>]*id="name"[^>]*>'
        )

    def test_email_field(self):
        self.assertRegex(
            self.html, r'<input[^>]*type="email"[^>]*>'
        )

    def test_contact_field(self):
        self.assertRegex(
            self.html, r'<input[^>]*id="contact"[^>]*>'
        )

    def test_submit_button(self):
        self.assertRegex(
            self.html, r'<button[^>]*type="submit"[^>]*>'
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)