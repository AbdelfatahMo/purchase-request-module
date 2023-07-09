from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    purchase_request_id = fields.Many2one(
        comodel_name="purchase.request",
        )

    def action_view_purchase_request(self):
        return {
            'name':_('Request Purchase'),
            'res_model':'purchase.request',
            'view_mode':'list,form',
            'domain':[('id','=',self.purchase_request_id.id)],
            'target':'current',
            'type':'ir.actions.act_window'
        }
