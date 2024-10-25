# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import config, float_compare
import logging

class StockMove(models.Model):
    _inherit = "stock.move"

    costo = fields.Float('Costo', readonly = True)