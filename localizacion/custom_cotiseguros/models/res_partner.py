from email.policy import default
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    policy_number = fields.Char('Nro de Poliza')
    type_partner = fields.Selection([('new', 'Nuevo'), ('renewal', 'Renovacion')],string='Tipo')
    emission_date = fields.Date('Fecha de Emisión')
    due_date = fields.Date('Fecha de Vencimiento')
    age = fields.Char('Edad')
    gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')],
                              string='Genero')
    rif_ci = fields.Char('RIF/CI')
    # company_type = fields.Selection(string='Company Type',
    #     selection=[('person', 'Tomador'), ('company', 'Company')],
    #     compute='_compute_company_type', inverse='_write_company_type')

