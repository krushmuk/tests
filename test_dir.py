import app_1
import unittest


class TestBookkeeping(unittest.TestCase):
    def setUp(self) -> None:
        app_1.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        app_1.directories = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }

    def test_get_own_name(self):
        self.assertEqual(app_1.get_doc_owner_name('11-2'), "Геннадий Покемонов")

    def test_get_all_doc_owners(self):
        self.assertEqual(app_1.get_all_doc_owners_names(), {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})

    def test_remove_doc(self):
        app_1.remove_doc_from_shelf("10006")
        self.assertEqual(app_1.directories['2'], [])

    def test_add_shelf(self):
        app_1.add_new_shelf('4')
        self.assertEqual(app_1.directories, {'1': ['2207 876234', '11-2'],
                                           '2': ['10006'],
                                           '3': [],
                                           '4': []
                                           })

    def test_append_doc_to_shelf(self):
        app_1.append_doc_to_shelf('11-2', '3')
        self.assertEqual(app_1.directories['3'], ['11-2'])

    def test_delete_doc(self):
        app_1.delete_doc('11-2')
        self.assertEqual(app_1.directories, {
            '1': ['2207 876234'],
            '2': ['10006'],
            '3': []
        })

    def test_get_doc_shelf(self):
        self.assertEqual(app_1.get_doc_shelf('11-2'), '1')

    def test_move_doc(self):
        app_1.move_doc_to_shelf('11-2', '3')
        self.assertEqual(app_1.directories['3'], ['11-2'])

    def test_show_all_doc_info(self):
        self.assertEqual(app_1.show_all_docs_info(), '''Список всех документов:
passport "2207 876234" "Василий Гупкин"
invoice "11-2" "Геннадий Покемонов"
insurance "10006" "Аристарх Павлов"
''')

    def test_add_new_doc(self):
        app_1.add_new_doc('number', 'type', 'owner', '1')
        self.assertEqual(app_1.documents, [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "type", "number": "number", "name": "owner"}
        ])
        self.assertEqual(app_1.directories['1'], ['2207 876234', '11-2', 'number'])
