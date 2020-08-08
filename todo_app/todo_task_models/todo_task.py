#-*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTask(models.Model):
    _inherit = 'sip.tareas'
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')

    name = fields.Char(help="What needs to be done?")

    @api.multi
    def sip_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True

    @api.one
    def sip_done(self):
        if self.user_id != self.env.user:
           raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).sip_done() 
   