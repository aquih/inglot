# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class PosConfig(models.Model):
    _inherit = 'pos.config'

    plantilla_correo_id = fields.Many2one("mail.template", string="Plantilla de correo")

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_plantilla_correo_id = fields.Many2one(related='pos_config_id.plantilla_correo_id', readonly=False)