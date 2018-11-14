{'name': 'Library Book Borrowing',
 'description': 'Members can borrow books from the library.',
 'author': 'Daniel Reis',
 'depends': [
     'mail',
     'library_member',
 ],
 'data': [
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/library_menu.xml',
    'views/checkout_view.xml',
    'views/checkout_mass_message_wizard.xml',
 ],
}
