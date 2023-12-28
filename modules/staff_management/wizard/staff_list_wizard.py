from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class Staff(models.Model):
    _name = "human_resource.staff.wizard"
    _description = "Staff list wizard"

    staff = fields.Many2one('human_resource.staff', string="Chọn nhân viên", inverse_name="department")

    def action_add_staff_to_department(self):
        department_id = self.env.context.get('department_id')

        department = self.env['human_resource.department'].browse(department_id)

        department.write({
            'staffs': [(4, self.staff.id, 0)]
        })
