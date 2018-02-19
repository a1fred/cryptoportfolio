import unittest


class CliTests(unittest.TestCase):
    test_conf = './sample.yml'

    def test_flags(self):
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
