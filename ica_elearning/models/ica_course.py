from odoo import api, fields, models

class Course(models.Model):
    _name   = "ica.course"
    _description = "ICA Course"

    name = fields.Char(string="Course Name", required=True)