import unittest
from main import sphere_function, hill_climbing, random_local_search, simulated_annealing

class TestOptimizationAlgorithms(unittest.TestCase):
    def setUp(self):
        self.bounds = [(-5, 5), (-5, 5)]

    def test_sphere_function(self):
        self.assertEqual(sphere_function([0, 0]), 0)
        self.assertEqual(sphere_function([2, 3]), 13)

    def test_hill_climbing(self):
        solution, value = hill_climbing(sphere_function, self.bounds)
        self.assertEqual(len(solution), 2)
        for i in range(2):
            self.assertTrue(-5 <= solution[i] <= 5)
        self.assertGreaterEqual(value, 0)

    def test_random_local_search(self):
        solution, value = random_local_search(sphere_function, self.bounds)
        self.assertEqual(len(solution), 2)
        for i in range(2):
            self.assertTrue(-5 <= solution[i] <= 5)
        self.assertGreaterEqual(value, 0)

    def test_simulated_annealing(self):
        solution, value = simulated_annealing(sphere_function, self.bounds)
        self.assertEqual(len(solution), 2)
        for i in range(2):
            self.assertTrue(-5 <= solution[i] <= 5)
        self.assertGreaterEqual(value, 0)

if __name__ == "__main__":
    unittest.main()
