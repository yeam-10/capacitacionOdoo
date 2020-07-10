# -*- coding: utf-8 -*-

from odoo import models, fields

class SipTareas(models.Model):
    _name = 'sip.tareas'

    name = fields.Char('Descripcion', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?' , default=True)