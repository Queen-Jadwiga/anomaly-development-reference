"""Regression checks for native property registration omissions; no engine execution."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from binding_patterns import BINDING_PATTERN, binding_kind, valid_binding_origin

class BindingPatternsTest(unittest.TestCase):
    def test_properties_are_indexed_alongside_methods_and_fields(self):
        text = '''.def("has_upgrade", &has_upgrade)
                  .property("condition", &get_condition_script, &set_condition_script)
                  .property("readonly", &get_value)
                  .def_readonly("id", &type::id)
                  .def_readwrite("value", &type::value)
                  def("lookup", &lookup)'''
        forms = [m.group(1) for m in BINDING_PATTERN.finditer(text)]
        self.assertEqual(forms, ['.def', '.property', '.property', '.def_readonly', '.def_readwrite', 'def'])
        self.assertEqual(binding_kind('.property', '&getter, &setter'), 'property')
        self.assertEqual(binding_kind('.property', '&getter_static'), 'property')

    def test_property_origin_is_accepted_without_a_def_token(self):
        self.assertTrue(valid_binding_origin('.property("condition", &get_condition_script, &set_condition_script)'))
        self.assertTrue(valid_binding_origin('luabind_class_server_entity(type);'))
        self.assertFalse(valid_binding_origin('return value;'))

    def test_existing_binding_categories_stay_distinct(self):
        cases = [('.def', '&type::method', 'method'), ('.def', '&type_static', 'virtual_method'),
                 ('.def_readonly', '&type::field', 'readonly_field'),
                 ('.def_readwrite', '&type::field', 'writable_field'),
                 ('def', '&lookup', 'global_function'), ('constructor', 'constructor<>()', 'constructor')]
        for form, expression, expected in cases:
            self.assertEqual(binding_kind(form, expression), expected)

if __name__ == '__main__':
    unittest.main()
