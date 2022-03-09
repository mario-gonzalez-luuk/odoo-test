# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one(compute="_compute_employee_id", comodel_name="res.users", string="Employee",
                                  store=True)

    @api.depends("state")
    def _compute_employee_id(self):
        for record in self:
            if record.state == "sale":
                record.employee_id = self._assign_sale_order()

    def _assign_sale_order(self):
        available_employees = self.env["res.users"].search([["status", "=", "available"]])
        if available_employees:
            return available_employees.sorted(key=lambda employee: employee.sale_order_assigned_qty)[0].id
        busy_employees = self.env["res.users"].search([["status", "=", "busy"]])
        if busy_employees:
            return busy_employees.sorted(key=lambda employee: employee.sale_order_assigned_qty)[0].id
        offline_employees = self.env["res.users"].search(["status", "=", "offline"])
        if offline_employees:
            return offline_employees.sorted(key=lambda employee: employee.sale_order_assigned_qty)[0].id
