# -*- coding: utf-8 -*-

{

'name': "sip_tareas_por_hacer",

'summary': """ Soluciones  integrales, Pyme C.A""",

'description': """ Modulo estandar para modificar el funcionamiento de account""",

'author': " anye",
'website': " https://yeam-10.github.io/Portafolio-yeam/ ",
'version': '1.0 ',
'depends': ['base'], 

'data': [
'sip_views/sip_menu_tareas.xml',
'sip_views/sip_vistas_tareas.xml',
'sip_security/sip_grupo_tareas.xml',
'sip_security/ir.model.access.csv',
],

 'installable': True,
 'application': False,
 'auto_install': False,




}