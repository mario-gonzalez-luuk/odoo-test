# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    status = fields.Selection(
        [('available', 'Available'), ('busy', 'Busy'), ('offline', 'Offline')], string="Employee Status")
    sale_order_ids = fields.One2many(comodel_name="sale.order", inverse_name="employee_id")
    sale_order_assigned_qty = fields.Integer(compute="_compute_sale_order_assigned_qty",
                                             string="Sale Order Assigned Quantity")

    @api.depends("sale_order_ids")
    def _compute_sale_order_assigned_qty(self):
        for record in self:
            record.sale_order_assigned_qty = len(record.sale_order_ids)