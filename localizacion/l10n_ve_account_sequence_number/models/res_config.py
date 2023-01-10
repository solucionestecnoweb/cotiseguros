# -*- coding: utf-8 -*-

from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    is_control_unique = fields.Boolean(related='company_id.is_control_unique', readonly=False)

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        params_obj = self.env['ir.config_parameter']
        params_obj.sudo().set_param("is_control_unique", self.is_control_unique)
        return res