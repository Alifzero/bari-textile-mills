# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderAuthentication(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approve_cost', 'Approve Cost'),
        ('sent', 'Sent'),
        ('sale', 'Sale Order'),
        ('done', 'Lock')],
        default='draft', required=True)
    # merchandiser

    yarn_price_available = fields.Boolean(string='Yarn Price Available')
    lab_test = fields.Boolean(string='Lab Test Required')

    cost_discussion = fields.Text(string='Discuss Yarm Cost')

    sample_required = fields.Boolean(string='Sample Required')

    # LAB
    lab_vendor = fields.Many2one('res.partner')
    time_required = fields.Date(string='Delivery Date')

    def GenRFQ(self):
        print('RFQ')
    def CostApprove(self):
        self.write({"state": "approve_cost"})

    def quotation_send(self):
        self.action_quotation_send()
        self.write({"state": "sent"})


    # check yarn price

    yarn_vendor = fields.Many2one(related='lab_vendor', string='Yarn Vendor')

    # management
    # cost_price = fields.Float()


class SaleOrderLineAuthentication(models.Model):
    _inherit = 'sale.order.line'

    cost_price = fields.Float(string='Cost Price')
    yarn_price = fields.Float(string='Yarn price')
    vendor_price = fields.Float(string='Vendor Price')


