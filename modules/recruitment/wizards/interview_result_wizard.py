from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class InterviewResult(models.Model):
    _name = "human_resource.interview_result_wizard"
    _description = "Interview result wizard"

    score = fields.Float(string="Điểm")
    comment = fields.Char(string="Nhận xét")

    def action_add_result(self):
        pass
