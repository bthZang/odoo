from odoo import models, fields


class InterviewAppointment(models.Model):
    _name = "human_resource.interview_appointment"
    _description = "Appointment information"

    time = fields.Datetime(string="Thời gian phỏng vấn")

    staffs = fields.Many2many('human_resource.staff', 'human_resource_appointment_staff', 'appointment',
                              'staff', string="Người phỏng vấn")

    applicant = fields.Many2one('human_resource.applicant', string="Ứng viên")
    location = fields.Char(string="Địa điểm")

    state = fields.Selection([('pending', 'Chờ xử lý'), ('approved', 'Chấp nhận'), ('rejected', 'Bị từ chối')], default='pending')

    def unlink(self):
        for appointment in self:
            relation = self.env['human_resource.interview_appointment'].browse(appointment.id)

            relation.write({
                'staffs': [(5, 0, 0)]
            })

        return super(InterviewAppointment, self).unlink()