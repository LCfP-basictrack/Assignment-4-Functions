from unittest import TestCase

import compound_interest


class CompoundInterestTest(TestCase):
    def test_compound_interest(self):
        principle = 10000   # EUR
        interest = 1.5      # %
        term = 10           # Years

        expected_amount = 11605.40825025149
        amount = compound_interest.compound_interest(principle, interest, term)
        self.assertAlmostEqual(expected_amount, amount)

    def test_compound_interest_no_years(self):
        principle = 10000   # EUR
        interest = 1.5      # %
        term = 0            # Years

        expected_amount = 10000
        amount = compound_interest.compound_interest(principle, interest, term)
        self.assertAlmostEqual(expected_amount, amount)

    def test_compound_interest_no_interest(self):
        principle = 10000   # EUR
        interest = 0        # %
        term = 10           # Years

        expected_amount = 10000
        amount = compound_interest.compound_interest(principle, interest, term)
        self.assertAlmostEqual(expected_amount, amount)

    def test_compound_interest_no_principle(self):
        principle = 0   # EUR
        interest = 1.5  # %
        term = 10       # Years

        expected_amount = 0
        amount = compound_interest.compound_interest(principle, interest, term)
        self.assertAlmostEqual(expected_amount, amount)
