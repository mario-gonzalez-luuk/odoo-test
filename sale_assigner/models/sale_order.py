# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one(comodel_name="res.users", string="Employee")
