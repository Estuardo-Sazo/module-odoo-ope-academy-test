from odoo import models, fields, api


class OpeAcademy(models.Model):
     _name = 'ope.academy'
     _description = 'Open Academy'

     name = fields.Char(
         string='Name',
         required=True,
     )

     partner_id= fields.Many2one(
         comodel_name="res.partner",
         string="Patner",
         help="This is the teacher"
     )

     partner_ids = fields.One2many(
         comodel_name="res.partner",
         inverse_name="academy_id",
         string="Partner",
         help="This are students"
     )

     partners_ids = fields.Many2many(
         comodel_name="res.partner",
         relation="academy_partner_rel",
         column1="academy_id",
         column2="partner_id",
         string="Many Partners"
     )