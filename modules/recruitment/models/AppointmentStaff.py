from odoo import models, fields


class AppointmentStaff(models.Model):
    _name = "human_resource_appointment_staff"
    _description = "Appointment Staff"

    appointment = fields.Many2one('human_resource.interview_appointment', required=True, string="Lịch hẹn")
    staff = fields.Many2one('human_resource.staff', required=True, string="Nhân viên")

    score = fields.Float(string="Điểm")
    comment = fields.Char(string="Nhận xét")

