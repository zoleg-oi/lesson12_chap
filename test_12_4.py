#Логирование
import logging
import unittest
import runner_l

class RunnerTest(unittest.TestCase):
    '''
    Класс осуществляет контроль правильности выполнения функции
    в программе runner
    '''
    isFrozen = False

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r = runner_l.Runner('Вася', -5)
            for i in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('"test_walk". Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r = runner_l.Runner(6)
            for i in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('"test_run". Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rw = runner_l.Runner('name')
        rr = runner_l.Runner('name')
        for i in range(10):
            rw.walk()
            rr.run()
        self.assertNotEqual(rw.distance, rr.distance)

class TournamentTest(unittest.TestCase):
    '''
    Данный класс осуществляет проверку правильности вычисления
    результата забегов участников соревнования.
   '''

    isFrozen = True

    def setUp(self):
        self.a = runner_l.Runner('Андрей', 9)
        self.n = runner_l.Runner('Ник', 3)
        self.y = runner_l.Runner('Усэйн', 10)
    def tearDown(self):
        self.a = None
        self.n = None
        self.y = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        dic_out = {}
        for i in cls.all_results:
            dic = cls.all_results[i]
            for key  in dic:
                dic_out[key] = dic[key].name
            print(dic_out)


    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        t = runner_l.Tournament(90, self.y, self.n)
        all_res = t.start()
        self.all_results['test1'] = all_res
        # print(all_results)
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')
    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        t = runner_t.Tournament(90, self.a, self.n)
        all_res = t.start()
        self.all_results['test2'] = all_res
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        t = runner_l.Tournament(90, self.y, self.a, self.n)
        all_res = t.start()
        self.all_results['test3'] = all_res
        # print(all_results)
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')

logging.basicConfig(level=logging.INFO,filemode='w',filename='runner_tests.log',encoding='UTF8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()

