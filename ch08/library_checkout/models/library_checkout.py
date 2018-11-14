from odoo import api, fields, models


class Checkout(models.Model):
    _name = 'library.checkout'
    _description = 'Checkout Request'
    _inherit = ['mail.thread']
    _order = 'id desc'

    @api.multi
    def name_get(self):
        names = []
        for rec in self:
            name = '%s - %s' % (rec.request_date or '?', rec.borrower_id.name or '?')
            names.append((rec.id, name))
        print(names)
        return names

    @api.model
    def _default_stage(self):
        Stage = self.env['library.checkout.stage']
        return Stage.search([], limit=1)

    borrower_id = fields.Many2one(
        'library.member',
        required=True,
    )
    name = fields.Char()
    user_id = fields.Many2one(
        'res.users',
        'Librarian',
        default=lambda s: s.env.uid,
    )
    request_date = fields.Date(
        default=lambda s: fields.Date.today())
    checkout_date = fields.Date()
    closed_date = fields.Date()
    stage_id = fields.Many2one(
        'library.checkout.stage',
        default=_default_stage,
    )
    notes = fields.Html()
    line_ids = fields.One2many(
        'library.checkout.line',
        'checkout_id',
        string='Borrowed Books',)


class CheckoutLine(models.Model):
    _name = 'library.checkout.line'
    _description = 'Borrow Request Line'

    checkout_id = fields.Many2one('library.checkout')
    book_id = fields.Many2one('library.book')
    notes = fields.Char()
