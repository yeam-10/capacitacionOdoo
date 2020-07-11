# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SipTareas(models.Model):
    _name = 'sip.tareas'

    name = fields.Char('Descripcion', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?' , default=True)

    @api.one
    def sip_done(self):
        self.is_done = not self.is_done

     #def sip_done(self):
         