#Систематизация и пропуск тестов.

import unittest
import tests_12_3

runTest = unittest.TestSuite()
TourTest = unittest.TestSuite()
runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
TourTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(runTest)
runner.run(TourTest)
