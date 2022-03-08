# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    status = fields.Selection(
        [('available', 'Available'), ('busy', 'Busy'), ('offline', 'Offline')],
        required=True, string="Status")
    sale_order_assigned_qty = fields.Integer(string="Sale Order Assigned Quantity")
