# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Patient (Rec) Log (for CLVhealth-JCAFB Solution)',
    'summary': 'Patient (Rec) Log Module used in CLVhealth-JCAFB Solution.',
    'version': '15.0.6.1',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_patient_rec',
        'clv_global_log',
    ],
    'data': [
        'views/patient_rec_log_view.xml',
        'data/global_log_client.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
