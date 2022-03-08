# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one(compute="_compute_employee_id", comodel_name="res.users", string="Employee")

    @api.depends("state")
    def _compute_employee_id(self):
        for record in self:
            if record.state == "sale":
                record.employee_id = _assign_sale_order()

    def _assign_sale_order(self):
        # TODO
        pass
