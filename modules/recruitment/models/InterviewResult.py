from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InterviewResult(models.Model):
    _name = "human_resource.interview_result"
    _description = "Interview result information"

    appointment = fields.Many2one('human_resource.interview_appointment', required=True, string="Lịch hẹn")
    staff = fields.Many2one('human_resource.staff', required=True, string="Nhân viên")

    score = fields.Float(string="Điểm", default=0)
    comment = fields.Char(string="Nhận xét")

    @api.constrains('score')
    def _check_integer_range(self):
        for record in self:
            if not (0 <= record.score <= 10):
                raise ValidationError("The value of 'score' must be between 0 and 10.")