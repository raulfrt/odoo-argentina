# -*- coding: utf-8 -*-
{   'active': False,
    'author': 'OpenERP - Team de Localizaci\xc3\xb3n Argentina',
    'category': 'Localization/Argentina',
    'demo_xml': [
       'data/partner_demo.xml',
      ],
    'depends': [   
                    'account',
                    'l10n_ar_base',
                    # 'l10n_ar_document',
                   'l10n_ar_base_vat', # Es usado en los onchange de documentos y demas
                   ],
    'description': '''
\n\nM\xc3\xb3dulo de Facturaci\xc3\xb3n de la localizaci\xc3\xb3n Argentina\n\n\n\nIncluye:\n\n\n\n  - Configuraci\xc3\xb3n de libros, diarios y otros detalles para facturaci\xc3\xb3n argentina.\n\n  - Wizard para configurar los talonarios necesarios para facturar.\n\n\n\nFalta:\n\n  - Terminar de completar la lista de codigos del AFIP de monedas (http://www.afip.gob.ar/fe/documentos/TABLA%20MONEDAS%20V.0%20%2025082010.xls)\n\n
''',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Argentina - Generador de Talonarios',
    'test': [   'test/products.yml',
                'test/partners.yml',
                'test/com_ri1.yml',
                'test/com_ri2.yml',
                'test/com_rm1.yml',
                'test/inv_ri2ri.yml',
                'test/inv_rm2ri.yml',
                'test/inv_ri2rm.yml',
                'test/bug_1042944.yml'],
    'data': [   
                      'security/l10n_ar_invoice_security.xml',
                      'wizard/journal_config_wizard_view.xml',
                      'data/responsability.xml',
                      'data/afip.document_letter.csv',
                      'data/afip.document_class.csv',
                      'data/document_type.xml', 
                      'data/partner.xml',
                      'data/country.xml',
                      'data/res.currency.csv',
                      'data/afip.concept_type.csv',
                      'view/partner_view.xml',
                      'view/company_view.xml',
                      'view/country_view.xml',
                      'view/afip_menuitem.xml',
                      'view/afip_document_letter_view.xml',
                      'view/afip_concept_type_view.xml',
                      'view/afip_optional_type_view.xml',
                      'view/afip_document_type_view.xml',
                      'view/afip_responsability_view.xml',
                      'view/afip_document_class_view.xml',
                      'view/account_journal_afip_document_class_view.xml',
                      'view/journal_view.xml',
                      'view/tax_code_view.xml',
                      'view/invoice_view.xml',
                      'view/account_move_view.xml',
                      'view/config_view.xml',
                      'view/report_invoice.xml',
                      'security/ir.model.access.csv',
                      ],
    'version': '2.7.243',
    'website': 'https://launchpad.net/~openerp-l10n-ar-localization'}