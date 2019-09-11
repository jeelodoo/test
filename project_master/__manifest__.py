# -*- coding: utf-8 -*-
{
    'name': "Project Master",

    'summary': """
        Develop project module""",

    'description': """
        Long description of module's purpose to develop project module
    """,

    'author': "Hashmicro / Jeel",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.8',

    # any module necessary for this one to work correctly
    'depends': ['base','project', 'branch_ext_id', 'vit_efaktur'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_tree_view.xml',

    ],
   
}