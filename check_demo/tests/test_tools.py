from odoo.tests import TransactionCase

from odoo.addons.check_demo.tools import compute_total


class TestTools(TransactionCase):

    def test_total_passes(self):
        self.assertEqual(compute_total([40, 60]), 100)

    def test_total_with_discount_fails(self):
        # Wrong on purpose: 10% off 100 is 90, not 100. Shows up as FAIL.
        self.assertEqual(compute_total([40, 60], discount=10), 100)

    def test_missing_price_errors(self):
        # Raises on purpose: KeyError, not an assertion. Shows up as ERROR.
        prices = {'apple': 40}
        compute_total([prices['pear']])
