from odoo import models, fields


class Timekeeping(models.Model):
    _name = 'human_resource.timekeeping'
    _description = 'All timekeeping list'

    checkin_date = fields.Datetime(string="Thời gian vào")
    checkout_date = fields.Datetime(string="Thời gian ra")
    staff = fields.Many2one('human_resource.staff', string='Nhân viên')
