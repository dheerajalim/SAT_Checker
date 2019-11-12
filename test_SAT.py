import unittest
from SAT import SatChecker

class TestSatChecker(unittest.TestCase):
    def test_output_1(self):
        cnf_instance = 'Lab-data/Lab-data/Inst/uf20-01.cnf'
        solution_file = 'Lab-data/Lab-data/sols/1.txt'
        sat_checker = SatChecker(cnf_instance, solution_file)
        self.assertEqual(sat_checker.solution(),True)

    def test_output_2(self):
        cnf_instance = 'Lab-data/Lab-data/Inst/uf20-01.cnf'
        solution_file = 'Lab-data/Lab-data/sols/2.txt'
        sat_checker = SatChecker(cnf_instance, solution_file)
        self.assertEqual(sat_checker.solution(),False)