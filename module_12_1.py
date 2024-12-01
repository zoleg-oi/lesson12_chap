# Цель: приобрести навык создания простейших Юнит-тестов
# Задача "Проверка на выносливость":
from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    '''
    Класс осуществляет контроль правильности выполнения функции
    в программе runner
    '''

    def test_walk(self):
        r = Runner('name')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runner('name')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        rw = Runner('name')
        rr = Runner('name')
        for i in range(10):
            rw.walk()
            rr.run()
        self.assertNotEqual(rw.distance, rr.distance)


if __name__ == '__main__':
    rt = RunnerTest()
    print(rt.test_walk())
