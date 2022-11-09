# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_sales_person = fields.Boolean(string='Sales Person')