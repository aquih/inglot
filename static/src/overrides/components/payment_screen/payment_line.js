/** @odoo-module */
import { TextInputPopup } from "@point_of_sale/app/utils/input_popups/text_input_popup";
import { PaymentScreenPaymentLines } from "@point_of_sale/app/screens/payment_screen/payment_lines/payment_lines";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreenPaymentLines.prototype, {
    async pedirCuatroDigitos(line){
        const { confirmed, payload } = await this.popup.add(TextInputPopup, {
                'title': 'Ingrese últimos cuatro dígitos',
            });
        if (confirmed && payload) {
            line.cuatro_digitos = payload;
        }else{
            this.props.deleteLine(line.cid)
        }
    },
    async selectedLineClass(line) {
        if (line.payment_method.numero_autorizacion == true){
            if (!('numero_autorizacion' in line && line['numero_autorizacion'] != false)){
                const { confirmed, payload } = await this.popup.add(TextInputPopup, {
                        'title': 'Ingrese Número de autorización',
                    });
                if (confirmed && payload) {
                    line.numero_autorizacion = payload;
                    this.pedirCuatroDigitos(line);
                }else{
                    this.props.deleteLine(line.cid)
                }
            }
        }
        return super.selectedLineClass(line)
    },

});