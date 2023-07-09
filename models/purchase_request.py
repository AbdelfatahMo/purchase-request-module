# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import date


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection(
        selection=[("draft", "Draft"),
                   ("confirmed", "Confirmed")]
    )

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string="Analytic Account"
    )

    requested_by = fields.Many2one(
        comodel_name="res.users",
        string="Requested by",
        default=lambda self: self.env.user.id,
    )

    requested_on = fields.Date(
        string="Requested On",
        default=date.today()
    )

    purchase_request_line_ids = fields.One2many(
        comodel_name='purchase.request.line',
        inverse_name='purchase_request_id',
    )

    
    
    purchase_order_ids = fields.One2many(
        comodel_name='purchase.order',
        inverse_name='purchase_request_id',
    )
    
    purchase_order_count=fields.Integer(
            compute='_compute_field' 
            )
        
    @api.depends('purchase_order_ids')
    def _compute_field(self):
        for record in self:
            record.purchase_order_count = len(self.purchase_order_ids)
        
        
        
   
    

    def action_draft(self):
        self.state = "draft"

    def action_confirmed(self):
        dic = {}
        for line in self.purchase_request_line_ids:
            if line.partner_id not in dic.keys():
                dic[line.partner_id] = list(line)
            else:
                dic[line.partner_id].append(line)
        list_of_ids=[]
        for key in dic.keys():
            vals = {
                'partner_id': key.id,
                'state': 'draft',
                'purchase_request_id':self.id,
            }
            purchase_order = self.env['purchase.order'].create(vals)
            list_of_ids.append(purchase_order.id)
            for line in dic[key]:
                line_vals = {
                    'order_id': purchase_order.id,
                    'product_id': line.product_id.id,
                    'product_qty': line.quantity,
                }
                self.env['purchase.order.line'].create(line_vals)
        self.purchase_order_ids = list_of_ids
        self.state = "confirmed"
        
    def action_view_purchase_order(self):
        return {
            'name':_('Requested Orders'),
            'res_model':'purchase.order',
            'view_mode':'list,form',
            'domain':[('purchase_request_id','=',self.id)],
            'target':'current',
            'type':'ir.actions.act_window'
        }