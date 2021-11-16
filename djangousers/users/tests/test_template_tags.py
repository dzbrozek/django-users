import datetime

from django.test import TestCase
from freezegun import freeze_time
from users.templatetags.user_extras import bizz_fuzz, is_allowed


class TemplateTagsTest(TestCase):
    @freeze_time("2021-11-16")
    def test_is_allowed(self):
        self.assertEqual(is_allowed(datetime.date(2008, 11, 16)), 'blocked')
        self.assertEqual(is_allowed(datetime.date(2008, 1, 1)), 'blocked')
        self.assertEqual(is_allowed(datetime.date(2007, 11, 16)), 'allowed')

    def test_bizz_fuzz(self):
        self.assertEqual(bizz_fuzz(9), "Bizz")
        self.assertEqual(bizz_fuzz(20), "Fuzz")
        self.assertEqual(bizz_fuzz(15), "BizzFuzz")
        self.assertEqual(bizz_fuzz(7), "7")
