from odoo import models, fields, api


class ReplyContact(models.TransientModel):
    _name = 'customer_service.reply'
    _description = 'Reply'

    contact = fields.Many2one('customer_service.contact')
    title = fields.Char(string="Tiêu đề")
    content = fields.Text(string="Nội dung")

    def reply_contact(self):
        contact_id = self.env.context.get('contact_id')

        for response in self:
            reply = self.env['customer_service.reply'].create({
                'title': response.title,
                'content': response.content,
                'contact': contact_id
            })