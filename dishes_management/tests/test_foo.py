# -*- coding: utf-8 -*-.
from odoo.tests.common import TransactionCase


class MyTestCase1(TransactionCase):

    def setUp(self):
        super(MyTestCase1, self).setUp()
        self.dishes = self.env['dishes_management.dishes_management']
        self.dish1 = self.dishes.create({
            'dish_name': 'dish 1',
            'dish_description': 'dish 11'
        })

    def test_dishes_management1(self):
        # self.assertEqual(self.dish1.dish_name, 'dish 1')
        self.assertEqual(self.dish1.dish_name, 'dish 2221')
