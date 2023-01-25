# -*- coding: utf-8 -*-


{
    'name': 'Odoo Academy',
    
    'summary': """Academy app""",
    
    'description': """
        Academy trainnig:
        -Courses
        -Sessions
        -Attendees
        """,
    
    'author': 'Sergio',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        ],
    'demo': [
        'demo/academy_demo.xml',
        ],
    
    'license': 'OPL-1'
}