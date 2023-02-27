from project.unitTest_lib.Patching.func_check_out import code_generator
from unittest.mock import patch, Mock
from unittest import TestCase


mock_get_code = Mock(name="get_code", return_value=30)
# code_generator.get_code = mock_get_code
#
# print(code_generator.get_code())


class TestGetCode(TestCase):

    @patch('random.randint')
    def test_get_code_should_should_return_30(self, patch_obj):
        patch_obj.return_value = 'CX-30'
        code_generator.get_code = patch_obj

        self.assertEqual(code_generator.get_code(), 'CX-30')

    @patch('project.unitTest_lib.Patching.func_check_out.code_generator.get_code')
    def test_get_code_mock_should_return_30(self, patch_obj):
        patch_obj.return_value = 'CX-30'
        code_generator.get_code = patch_obj

        self.assertEqual(code_generator.get_code(), 'CX-30')



