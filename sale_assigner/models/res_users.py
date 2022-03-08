# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    status = fields.Selection(
        [('available', 'Available'), ('busy', 'Busy'), ('offline', 'Offline')],
        required=True, string="Status")
    sale_order_ids = fields.One2many(comodel_name="sale.order", inverse_name="employee_id")
    sale_order_assigned_qty = fields.Integer(string="Sale Order Assigned Quantity")

