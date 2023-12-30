from odoo import models, fields, api


class Contact(models.Model):
    _name = 'customer_service.contact'
    _description = 'Contact'

    email = fields.Char(string="Email")
    title = fields.Char(string="Tiêu đề")
    content = fields.Text(string="Nội dung")

    customer = fields.Many2one('customer_service.customer', string='Tên khách hàng')
    responses = fields.One2many('customer_service.reply', inverse_name='contact')