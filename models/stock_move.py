# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models
import logging

class StockMove(models.Model):
    _inherit = "stock.move"

    costo = fields.Float('Costo', readonly = True)