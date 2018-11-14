from odoo import api, fields, models


class CheckoutBooks(models.TransientModel):
    _name = 'library.checkout.book'
    _description = 'Select Books for Checkout'

    checkout_id = fields.Many2one('library.checkout')
    search_text = fields.Char()

    available_ids = fields.Many2many(
        'library.book',
        relation='library_checkout_books_avail_rel',
        string='Available Titles')
    selected_ids = fields.Many2many(
        'library.book',
        relation='library_checkout_books_sel_rel',
        string='Selected Titles')

    @api.model
    def default_get(self, field_names):
        defaults = super().default_get(field_names)
        print(self.env.context)
        import pudb; pudb.set_trace()
        return defaults

    @api.multi
    def button_search(self):
        self.ensure_one()
        text = self.search_text
        domain = [
            '&', ('is_available', '=', True),
            '&', ('id', 'not in', self.selected_ids.ids),
            '|', ('name', 'ilike', text),
            '|', ('isbn', 'ilike', text),
            '|', ('publisher_id', 'ilike', text),
                 ('author_ids', 'ilike', text),
        ]
        Book = self.env['library.book']
        res = Book.search(domain)
        self.available_ids = res
        return _reload_form(self)

    def button_select(self):
        print(self.env.context)
        import pudb; pudb.set_trace()
