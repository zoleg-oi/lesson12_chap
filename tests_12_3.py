from runner import Runner
import unittest
import runner_t
from runner import Runner

class RunnerTest(unittest.TestCase):
    '''
    Класс осуществляет контроль правильности выполнения функции
    в программе runner
    '''
    isFrozen = False

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = Runner('name')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = Runner('name')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(isFrozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rw = Runner('name')
        rr = Runner('name')
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
        self.a = runner_t.Runner('Андрей', 9)
        self.n = runner_t.Runner('Ник', 3)
        self.y = runner_t.Runner('Усэйн', 10)
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
        t = runner_t.Tournament(90, self.y, self.n)
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
        t = runner_t.Tournament(90, self.y, self.a, self.n)
        all_res = t.start()
        self.all_results['test3'] = all_res
        # print(all_results)
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')
