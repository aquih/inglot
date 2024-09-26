# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    costo_total = fields.Float('Costo total', compute="_compute_inglot_move_ids_without_package")
    
    @api.onchange('move_ids_without_package')
    def _compute_inglot_move_ids_without_package(self):
        for albaran in self:
            costo_total = 0
            if albaran.move_ids_without_package:
                for linea in albaran.move_ids_without_package:
                    costo_total += linea.costo
            albaran.costo_total = costo_total