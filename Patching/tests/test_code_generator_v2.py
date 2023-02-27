from unittest import TestCase
from project.unitTest_lib.Patching.func_check_out.code_generator_v2 import get_code_with_day
from unittest.mock import patch

print(get_code_with_day())
class TestGetCodeWithDay(TestCase):

    @patch('project.unitTest_lib.Patching.func_check_out.code_generator_v2.get_code')
    @patch('project.unitTest_lib.Patching.func_check_out.code_generator_v2.get_today_name')
    def test_get_code_with_day_with_mocked_friday(self, get_today_patch, get_code_patch):

        get_today_patch.return_value = "FRI"
        get_code_patch.return_value = "CX-5"
        self.assertEqual(get_code_with_day(), "CX-5-FRI")
