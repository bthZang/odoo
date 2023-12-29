from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

from datetime import datetime


class InterviewResult(models.TransientModel):
    _name = "human_resource.interview_result.wizard"
    _description = "Interview result wizard"

    score = fields.Float(string="Điểm")
    comment = fields.Char(string="Nhận xét")

    def action_add_result(self):
        appointment_id = self.env.context.get('appointment_id')
        user_id = self.env.user.id

        staff_id = self.env['human_resource.staff'].search([('user_id', '=', user_id)]).id

        for record in self:
            result = self.env['human_resource.interview_result'].search(
                [('appointment', '!=', False), ('appointment.id', '=', appointment_id),
                 ('staff.id', '=', staff_id)], limit=1)
            if result is not None:
                print("Result existed")
                result.write({
                    'score': record.score,
                    'comment': record.comment
                })
            else:
                print("Result not existed")
                self.env['human_resource.interview_result'].create(dict({
                    'score': record.score,
                    'comment': record.comment,
                    'staff': staff_id,
                    'appointment': appointment_id
                }))
