from odoo import models, fields

class InterviewResult(models.Model):
    _name = "human_resource.interview_result"
    _description = "Applicant information"

    name = fields.Char(string="Tên ứng viên")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    address = fields.Char(string="Địa chỉ")

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

