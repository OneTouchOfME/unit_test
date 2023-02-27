from unittest import TestCase
from unittest.mock import patch
from project.unitTest_lib.Patching.func_check_out import new_model
# print(new_model.checking())

class TestNewModel(TestCase):

    @patch('project.unitTest_lib.Patching.func_check_out.new_model.checking', return_value='pankaj_abc')
    def test_checkout(self, mock_check_output):

        actual_output = new_model.checking()
        # expected_output = b'testing_new_model.py'
        # self.assertIn(b'testing_new_model.py', actual_output)
        expected_output = 'pankaj_abc'
        self.assertIn(expected_output, actual_output)