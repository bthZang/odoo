from odoo import models, fields, api


class Message(models.Model):
    _name = 'customer_service.message'
    _description = 'Message'

    customer = fields.Many2one('customer_service.customer', string='Tên khách hàng')
    title = fields.Char(string="Tiêu đề")
    content = fields.Char(string="Nội dung")