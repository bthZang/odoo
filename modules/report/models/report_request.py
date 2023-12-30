from odoo import models, fields, api


class ReportRequest(models.Model):
    _name = 'report.report_request'
    _description = 'report.report_request'
    _rec_name = 'title'

    deadline = fields.Datetime(string="Hạn nộp")
    state = fields.Selection(
        [('created', 'Đang chờ phản hồi từ người thực hiện'), ('in_progress', 'Đang xử lý'), ('done', 'Hoàn thành'), ('rejected', 'Bị từ chối')],
        string="Trạng thái", default="created")

    title = fields.Char(string="Tiêu đề")
    description = fields.Char(string="Mô tả")

    report = fields.One2many('report.report', string="Báo cáo", inverse_name="request")
    assignee = fields.Many2one('human_resource.staff', string="Người thực hiện")
    department = fields.Many2one('human_resource.department', string="Phòng ban thực hiện")
