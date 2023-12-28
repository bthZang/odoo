from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class Staff(models.Model):
    _name = "human_resource.staff"
    _description = "Staff information"

    name = fields.Char(string="Tên nhân viên", required=True)
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email", required=True)
    address = fields.Char(string="Địa chỉ")
    job_position = fields.Char(string="Chức vụ")
    role = fields.Selection([('admin', 'Quản lý'), ('hr_staff', 'Nhân viên quản lý nhân sự'),
                             ('customer_service_staff', 'Nhân viên chăm sóc khách hàng'), ('staff', 'Nhân viên')],
                            string="Loại nhân viên")
    image = fields.Char(String="Ảnh")

    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False)
    create_user = fields.Boolean(store=False, default=True, copy=False, string="Technical field, whether to create an user")

    department = fields.Many2one('human_resource.department', string="Phòng ban")
    # department_role = fields.Selection([('manager', 'Trưởng phòng'), ('employee', 'Nhân viên')], compute='_compute_staff_role', string='Chức vụ')
    #
    # def _compute_staff_role(self):
    #     for staff in self:
    #         for department_staff in staff.department:
    #             if department_staff.id == staff.department.manager.id:
    #                 staff.department_role = 'manager'
    #                 return
    #         staff.department_role = 'employee'

    def action_create_user(self):
        self.ensure_one()
        if self.user_id:
            raise ValidationError(_("This employee already has an user."))
            # 'default_create_employee_id': self.id,
        self.user_id = self.env['res.users'].create(dict(
            name=self.name,
            mobile_phone=self.phone,
            work_email=self.email,
            email=self.email,
            login=self.email,
            image_1920=self.image,
        ))

        template = self.env.ref('auth_signup.set_password_email', raise_if_not_found=False)

        if not template:
            template = self.env.ref('auth_signup.reset_password_email')

        assert template._name == 'mail.template'

        email_values = {'email_cc': False, 'auto_delete': True, 'message_type': 'user_notification',
                        'recipient_ids': [], 'partner_ids': [], 'scheduled_date': False, 'email_to': self.email}

        mail_id = template.send_mail(self.user_id.id, force_send=True, raise_exception=True, email_values=email_values)
        print(f"Mail id: {mail_id}")
        print(email_values)

    @api.onchange('role')
    def onchange(self, values, field_name, field_onchange):
        global group
        user = self.env['res.users'].browse(self.user_id.id)

        internal_user = self.env.ref('base.group_user')
        if values.get('role') == 'admin':
            group = self.env.ref('base.group_erp_manager')
        elif values.get('role') == 'hr_staff':
            group = self.env.ref('staff_management.hr_triple_c_group')
        elif values.get('role') == 'customer_service_staff':
            group = self.env.ref('staff_management.customer_service_triple_c_group')
        else:
            group = self.env.ref('base.group_user')

        user.write({
            'groups_id': [(6, 0, [group.id, internal_user.id])]
        })

        return values


    def send_email_to_selected_employees(self):
        # Get the selected employees
        selected_employees = self.filtered(lambda emp: emp)  # Replace with your actual field

        # Prepare email content and recipients
        email_subject = "Your Email Subject"
        email_body = "Your Email Body"
        recipients = selected_employees.mapped('email')

        for email in recipients:
            sent_mail = self.env['mail.mail'].create({
                'subject': email_subject,
                'body_html': email_body,
                'email_to': email,
            }).send()

            print(sent_mail)

        # Optional: Update a field to mark that the email has been sent
        # selected_employees.write({'email_sent_field': True})  # Replace with your actual field

    # def action_verify_password(self):
    #     template = False
    #     try:
    #         template = self.env.ref('auth_signup.set_password_email', raise_if_not_found=False)
    #     except ValueError:
    #         pass
    #
    #     if not template:
    #         template = self.env.ref('auth_signup.reset_password_email')
    #     assert template._name == 'mail.template'
    #
    #     email_values = {
    #         'email_cc': False,
    #         'auto_delete': True,
    #         'message_type': 'user_notification',
    #         'recipient_ids': [],
    #         'partner_ids': [],
    #         'scheduled_date': False,
    #     }
    #
    #     for user in self:
    #         if not user.email:
    #             raise UserError(_("Cannot send email: user %s has no email address.", user.name))
    #         email_values['email_to'] = user.email
    #         # TDE FIXME: make this template technical (qweb)
    #         with self.env.cr.savepoint():
    #             force_send = not (self.env.context.get('import_file', False))
    #             template.send_mail(user.id, force_send=force_send, raise_exception=True, email_values=email_values)
