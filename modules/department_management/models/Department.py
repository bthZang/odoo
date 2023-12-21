from odoo import models, fields


class Department(models.Model):
    _name = "human_resource.department"
    _description = "Department information"

    name = fields.Char(string="Tên phòng ban")
    description = fields.Char(string="Mô tả")