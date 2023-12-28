from odoo import models, fields


class Department(models.Model):
    _name = "human_resource.department"
    _description = "Department information"

    name = fields.Char(string="Tên phòng ban")
    description = fields.Char(string="Mô tả")

    manager = fields.Many2one('human_resource.staff', string="Trưởng phòng")

    staffs = fields.One2many('human_resource.staff', string="Danh sách nhân viên")

    total_employee = fields.Integer(compute='_compute_total_staff', string='Total Employee')

    def _compute_total_staff(self):
        emp_data = self.env['human_resource.staff']._read_group([('department', 'in', self.ids)], ['department'],
                                                                ['department'])
        result = dict((data['department'][0], data['department_count']) for data in emp_data)
        for department in self:
            department.total_employee = result.get(department.id, 0)
