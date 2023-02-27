from unittest import TestCase
from unittest.mock import patch
from project.unitTest_lib.Patching.func_check_out import new_model

class TestNewModel(TestCase):

    def test_checkout(self):

        with patch('project.unitTest_lib.Patching.func_check_out.new_model.checking', return_value='pankaj_abc'):
            actual_output = new_model.checking()

        expected_output = 'pankaj_abc'
        self.assertIn(expected_output, actual_output)