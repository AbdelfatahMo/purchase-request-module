from odoo import fields, models, api


class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'

    purchase_request_id = fields.Many2one(
        comodel_name="purchase.request",
        string="Purchase Request"
    )
    
    product_id = fields.Many2one(
        string="Product",
        comodel_name='product.product',
    )

    partner_id = fields.Many2one(
        'res.partner', string='Vendor', required=True,
    )

    quantity = fields.Float(
        string="Quantity"
    )
    
    state=fields.Selection(
         selection=[("draft", "Draft"),
                   ("confirmed", "Confirmed")],
        related='purchase_request_id.state'
    )

    product_uom = fields.Many2one(
        comodel_name='uom.uom',
        string='Unit of Measure',

    )

    