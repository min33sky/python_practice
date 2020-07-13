import unittest
"""
replace space with %20
ex)"hey how are you    "
return hey%20how%20are%20you
"""

def encode_space(str,length):
    # strip() : 끝에 공백 제거
    return str.strip().replace(" ", "%20")

class encode_space_test(unittest.TestCase):
    def test(self):
        self.assertEqual("hey%20how%20are%20you",encode_space("hey how are you   ",18))