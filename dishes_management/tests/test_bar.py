# -*- coding: utf-8 -*-.
from odoo.tests.common import TransactionCase


class MyTestCase2(TransactionCase):

    def setUp(self):
        super(MyTestCase2, self).setUp()
        self.dishes = self.env['dishes_management.dishes_management']
        self.dish1 = self.dishes.create({
            'dish_name': 'dish 1',
            'dish_description': 'dish 11'
        })

    def test_dishes_management2(self):
        self.assertEqual(self.dish1.dish_name, 'dish 1')
        # self.assertEqual(self.dish1.dish_name, 'dish 2221')

























# from odoo.tests.common import TransactionCase
#
#
# class ShopManagementTest(TransactionCase):
#
#     def setUp(self):
#         super(ShopManagementTest, self).setUp()
#         self.shops = self.env['shops_management.shops_management']
#         self.shop1 = self.shops.create({
#             'name': 'shop 1',
#             'value': '11'
#         })
#
#     def test_shop_management(self):
#         self.assertEqual(self.shop1.name, 'shop 12')
