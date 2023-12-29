from odoo import models, fields, _, api


class InterviewResultList(models.TransientModel):
    _name = "human_resource.interview_result_list_wizard"
    _description = "Interview result list wizard"

    results = fields.Many2many('human_resource.interview_result', 'interview_result_relation', string="Danh sách")

    @api.model
    def default_get(self, fields):
        defaults = super(InterviewResultList, self).default_get(fields)

        appointment_id = self.env.context.get('appointment_id')
        appointment_staff = self.env['human_resource.interview_result'].search([('appointment.id', '=', appointment_id)])

        defaults['results'] = appointment_staff

        return defaults

    def send_result_to_applicant(self):
        print("Send mail")