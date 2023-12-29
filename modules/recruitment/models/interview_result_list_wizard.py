from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class InterviewResultList(models.TransientModel):
    _name = "human_resource.interview_result_list_wizard"
    _description = "Interview result list wizard"



    def action_add_result(self):
        appointment_id = self.env.context.get('appointment_id')
        user_id = self.env.user.id

        staff_id = self.env['human_resource.staff'].search([('user_id', '=', user_id)])

        for record in self:
            appointment_staff = self.env['human_resource_appointment_staff'].search([('appointment', '=', appointment_id)])

            appointment_staff.write({
                'score': record.score,
                'comment': record.comment,
                'staff': staff_id
            })
