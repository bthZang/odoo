from odoo import models, fields, api


class Customer(models.Model):
    _name = 'customer_service.customer'
    _description = 'Customer'

    name = fields.Char(string="Tên khách hàng")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    address = fields.Char(string="Địa chỉ")
    potentialPoint = fields.Integer(string="Điểm uy tín", default=0)
