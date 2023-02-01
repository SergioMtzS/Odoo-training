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
    'depends': ['sale_management'],
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        ],
    'demo': [
        'demo/academy_demo.xml',
        ],
    
    'license': 'OPL-1'
}