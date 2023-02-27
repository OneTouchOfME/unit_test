from unittest import TestCase
from unittest.mock import patch
from project.unitTest_lib.Patching.func_check_out.printing import just_print
from io import StringIO

class TestPrinting(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_print):
        just_print()
        expected_out = "name : pankaj\ncompany : EN-PHASE\n"
        self.assertEqual(mock_print.getvalue(), expected_out)
