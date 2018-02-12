import unittest
from io import StringIO
from unittest.mock import patch


class CliTests(unittest.TestCase):
    test_conf = './sample.yml'

    @patch('sys.stdout', new_callable=StringIO)
    def test_flags(self, mock_stdout):
        from cryptoportfolio.main import main
        main(
            open(self.test_conf, 'r'),
            summarize=True,
            hide_zeros=True,
            hide_usd_zeros=True,
            sort=True,
            print_all_total=True,
            print_group_total=True,
        )
