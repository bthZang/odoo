from odoo import models, fields, api


class ReportFile(models.Model):
    _name = 'report.report_file'
    _description = 'file'

    name = fields.Char(string="Tiêu đề")
    description = fields.Char(string="Miêu tả")
    file = fields.Binary(string='File', attachment=True)
    
    report = fields.Many2one('report.report', string="Báo cáo")
