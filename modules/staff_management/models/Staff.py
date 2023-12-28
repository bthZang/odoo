from odoo import models, fields, _
from odoo.exceptions import ValidationError


class Staff(models.Model):
    _name = "human_resource.staff"
    _description = "Staff information"

    name = fields.Char(string="Tên nhân viên")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email", required=True)
    address = fields.Char(string="Địa chỉ")
    job_position = fields.Char(string="Chức vụ")
    role = fields.Selection([('admin', 'Quản lý'), ('hr_staff', 'Nhân viên quản lý nhân sự'),
                             ('customer_service_staff', 'Nhân viên chăm sóc khách hàng'), ('staff', 'Nhân viên')],
                            string="Loại nhân viên")
    image = fields.Char(String="Ảnh")

    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False)
    create_user = fields.Boolean(store=False, default=True, copy=False, string="Technical field, whether to create an user")

    department = fields.Many2one('human_resource.department', string="Phòng ban")

    def action_create_user(self):
        self.ensure_one()
        if self.user_id:
            raise ValidationError(_("This employee already has an user."))
            # 'default_create_employee_id': self.id,
        self.user_id = self.env['res.users'].create(dict(
            name=self.name,
            mobile_phone=self.phone,
            login=self.email,
        ))
