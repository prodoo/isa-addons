# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 ISA s.r.l. (<http://www.isa.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Manage Employee's Holidays",
    "version" : "1.0",
    "author" : "ISA srl",
    "category": 'Human Resources',
    "description": """
    This module aims to manage employee's holidays.
    Calculates the hours of permissions by employee's working time allow the exclusion or inclusion of public holidays.
    """,
    'website': 'http://www.isa.it',
    'init_xml': [],
    "depends" : ['hr_holidays','hr_contract','report_aeroo_ooo','res_company_ext_isa'],
    'update_xml': ['hr_holidays_isa_view.xml',"report/report.xml",'wizard/hr_holidays_bymonth_view.xml','security/ir.model.access.csv'],
    'demo_xml': [
    ],
    'test': [
    ],
    'installable': True,
    'active': False,
}
