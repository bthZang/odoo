from odoo import models, fields, api


class Timekeeping(models.Model):
    _name = 'human_resource.timekeeping'
    _description = 'All timekeeping list'

    name = fields.Char(compute='_compute_name')

    checkin_date = fields.Datetime(string="Thời gian vào", required=True)
    checkout_date = fields.Datetime(string="Thời gian ra", required=True)
    staff = fields.Many2one('human_resource.staff', string='Nhân viên', required=True)

    @api.depends('checkin_date', 'checkout_date', 'staff')
    def _compute_name(self):
        for record in self:
            if record.checkin_date:
                record.name = f"{record.staff.name} - {record.checkin_date.strftime('%d/%m/%Y')}"
            else:
                record.name = "New timekeeping"
