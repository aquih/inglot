# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    costo_total = fields.Float('Costo total', readonly = True)
    
    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        for albaran in self:
            costo = 0
            if albaran.move_ids_without_package:
                costo_linea = 0
                for linea in albaran.move_ids_without_package:
                    costo_linea = linea.product_id.standard_price * linea.quantity
                    costo += costo_linea
                    linea.costo = costo_linea
                albaran.costo_total = costo