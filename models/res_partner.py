from odoo import models, fields, api


class ResPartner(models.Model):
     _inherit = 'res.partner'

     academy_id = fields.Many2one(
         comodel_name="ope.academy",
         string="Academy",
     )

     academies_ids = fields.Many2many(
         comodel_name="ope.academy",
         relation="academy_partner_rel",
         column1="partner_id",
         column2="academy_id",
         string="Amacademies"
     )
