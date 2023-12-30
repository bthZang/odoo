from odoo import models, fields, api


class Report(models.Model):
    _name = 'report.report'
    _description = 'report.report'
    _rec_name = 'title'

    title = fields.Char(string="Tiêu đề")
    content = fields.Char(string="Nội dung")

    state = fields.Selection(
        [('pending', 'Đang chờ'), ('approved', 'Được chấp nhận'), ('rejected', 'Bị từ chối')],
        string="Trạng thái")

    files = fields.One2many('report.report_file', string='Danh sách file', inverse_name="report")
    request = fields.Many2one('report.report_request')