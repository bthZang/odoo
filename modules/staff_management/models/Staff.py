from odoo import models, fields


class Staff(models.Model):
    _name = "human_resource.staff"
    _description = "Staff information"

    name = fields.Char(string="Tên nhân viên")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    address = fields.Char(string="Địa chỉ")
    job_position = fields.Char(string="Chức vụ")
    role = fields.Selection([('admin', 'Quản lý'), ('hr_staff', 'Nhân viên quản lý nhân sự'), ('customer_service_staff', 'Nhân viên chăm sóc khách hàng'), ('staff', 'Nhân viên')], string="Loại nhân viên")
    image = fields.Char(String="Ảnh")

    password = fields.Char(string="Mật khẩu")

    department = fields.Many2one('human_resource.department', string="Phòng ban")