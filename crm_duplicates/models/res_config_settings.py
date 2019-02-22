# -*- coding: utf-8 -*-

from odoo import fields, models

class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_duplicate_id = fields.Many2one(
        'res.company',
        string='Company Duplicates',
        default=lambda self: self.env.user.company_id,
        required=True,
    )
    duplicate_fields_partner = fields.Many2many(
        related='company_duplicate_id.duplicate_fields_partner',
        compute_sudo=True,
        string='Partner Rigid Duplicates Fields',
        domain=[
            ('model', '=', 'res.partner'),
            ('ttype', 'not in', ['one2many', 'many2many', 'binary', 'reference', 'serialized']),
            ('store', '=', True),
        ],
        help='Select criteria, how to search partner duplicates. \
            Odoo would not allow to save a duplicate in comparison to the soft fields.',
    )
    duplicate_fields_partner_soft = fields.Many2many(
        'ir.model.fields', 'rel_table1', 'rel1x', 'rel1y',
        string='Partner Soft Duplicates Fields',
        related='company_duplicate_id.duplicate_fields_partner_soft',
        compute_sudo=True,
        domain=[
            ('model', '=', 'res.partner'),
            ('ttype', 'not in', ['one2many', 'many2many', 'binary', 'reference', 'serialized']),
            ('store', '=', True),
        ],
        help='Select criteria, how to search partner duplicates. \
            Odoo would show such duplicates on a special button, but would allow to save such object!',
    )
    search_duplicates_for_companies_only = fields.Boolean(
        string="Only companies and stand-alone individuals",
        related='company_duplicate_id.search_duplicates_for_companies_only',
        compute_sudo=True,
        help="""
            If checked duplicates would be searched only for and among partners without parent.
            In such a way all contacts would be excluded.
        """,
    )
    duplicate_fields_lead = fields.Many2many(
        related='company_duplicate_id.duplicate_fields_lead',
        compute_sudo=True,
        string='Leads Rigid Duplicates Fields',
        domain=[
            ('model', '=', 'crm.lead'),
            ('ttype', 'not in', ['one2many', 'many2many', 'binary', 'reference', 'serialized']),
            ('store', '=', True),
        ],
        help='Select criteria, how to search leads duplicates. \
            Odoo would not allow to save a duplicate in comparison to the soft fields.',
    )
    duplicate_fields_lead_soft = fields.Many2many(
        related='company_duplicate_id.duplicate_fields_lead_soft',
        compute_sudo=True,
        string='Leads Soft Duplicates Fields',
        domain=[
            ('model', '=', 'crm.lead'),
            ('ttype', 'not in', ['one2many', 'many2many', 'binary', 'reference', 'serialized']),
            ('store', '=', True),
        ],
        help='Select criteria, how to search leads duplicates. \
            Odoo would show duplicates on the special button, but it would allow to save a duplicate',
    )
