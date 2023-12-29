from odoo import models, fields

class Applicant(models.Model):
    _name = "human_resource.applicant"
    _description = "Applicant information"

    name = fields.Char(string="Tên ứng viên")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    address = fields.Char(string="Địa chỉ")
    birth = fields.Date(string="Ngày sinh")
    apply_position = fields.Char(string="Vị trí ứng tuyển")

    image = fields.Char(string="Ảnh")
    cv = fields.Binary(string='File', attachment=True)
    portfolio = fields.Binary(string='File', attachment=True)

    state = fields.Selection([('pending', 'Chờ xử lý'), ('approved', 'Chấp nhận'), ('rejected', 'Bị từ chối')])
    reason = fields.Char(string="Lý do")

    def approve_applicant(self):
        for applicant in self:
            applicant.state = 'approved'

    def reject_applicant(self):
        pass

