from odoo import models, fields, api


class InterviewResult(models.Model):
    _name = "human_resource.interview_result"
    _description = "Interview result information"

    appointment = fields.Many2one('human_resource.interview_appointment', required=True, string="Lịch hẹn")
    staff = fields.Many2one('human_resource.staff', required=True, string="Nhân viên")

    score = fields.Float(string="Điểm")
    comment = fields.Char(string="Nhận xét")
