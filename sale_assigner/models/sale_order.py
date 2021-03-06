# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one(compute="_compute_employee_id", comodel_name="hr.employee", string="Employee",
                                  store=True)

    @api.depends("state")
    def _compute_employee_id(self):
        for record in self:
            if record.state == "sale":
                record.employee_id = self._assign_sale_order()

    def _assign_sale_order(self):
        # Finds the employee id with less assigned sale orders, the order will be: available -> busy -> offline
        # If no employees are found with any of the status a validation error will be raised

        available_employees = self.env["hr.employee"].search([["status", "=", "available"]])
        if available_employees:
            return available_employees.sorted(key=lambda employee: employee.sale_order_assigned_qty)[0].id
        busy_employees = self.env["hr.employee"].search([["status", "=", "busy"]])
        if busy_employees:
            return busy_employees.sorted(key=lambda employee: employee.sale_order_assigned_qty)[0].id
        all_employees = self.env["hr.employee"].search([["status", "!=", False]])
        if all_employees:
            return all_employees.sorted(key=lambda employee: employee.sale_order_assigned_qty)[0].id
        else:
            raise ValidationError(_("No employees found to handle the sale order"))
