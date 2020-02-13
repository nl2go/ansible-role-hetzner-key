import unittest

from filter_plugins.hetzner_key import *


class HetznerKeyTest(unittest.TestCase):

    def test_init(self):
        module = FilterModule()
        filters = module.filters()

        self.assertEqual(filters.get('hetzner_key_form_urlencode'), form_urlencode.form_urlencode)
        self.assertEqual(filters.get('hetzner_key_change_set'), change_set.change_set)
