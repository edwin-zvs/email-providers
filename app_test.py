import unittest
import app

class TestProviderList(unittest.TestCase):
    def test_duplicated_entry(self):
        dup = False
        for key, value in app.providers.items():
            if value > 1:
                dup = True
                print(key + " is duplicated")

        self.assertFalse(dup)

    def test_check(self):
        self.assertEquals(404, app.check("non_exist_domain.com")[1])
        self.assertEquals(404, app.check("foo@non_exist_domain.com")[1])
        self.assertEquals(200, app.check("foo@gmail.com")[1])
        self.assertEquals(200, app.check("gmail.com")[1])

if __name__ == '__main__':
    unittest.main()
