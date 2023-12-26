from odoo import models, fields


class Work(models.Model):
    _name = "human_resource.work"
    _description = "detail information of work"

    title = fields.Char(string="Tiêu đề")
    description = fields.Char(string="Mô tả công việc")
    deadline = fields.Datetime(string="Hạn chót")
    state = fields.Selection([('todo', 'Chưa phân công'), ('in_progress', 'Đang thực hiện'), ('reviewed', 'Đang được kiểm tra '), ('done', 'Hoàn thành'), ('canceled', "Bị hủy")], string='Trạng thái', default_value='todo')
    reviewer = fields.Many2one('human_resource.staff', string='Người kiểm duyệt')
    assignee = fields.Many2one('human_resource.staff', string='Người thực hiện')
