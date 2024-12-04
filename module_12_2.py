# Методы Юнит-тестирования
import unittest
import runner_t

class TournamentTest(unittest.TestCase):
    '''
    Данный класс осуществляет проверку правильности вычисления
    результата забегов участников соревнования.
    При минимальных дистанциях Ник может пробежать быстрее, чем остальные, если окажется
    на старте перед другим участником. Оказаться он может из-за того, что при удалении из списка
    self.participants.remove(participant) в конце цикла смещает индексы списка, а цикл for идет по индексам сохраненным
    при инициализации цикла. Т.е., если Андрей был по индексу 1, то после удаления участника он становится 0,
    а Ник становится 1 и выбирается условием for participant in self.participants: вместо Андрея,
    тем самым на короткой дистанции, которая не больше чем скорость Ника * 2,
    он заканчивает быстрее Андрея, хотя скорость у него ниже.
    '''
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


    def test_tournament1(self):
        t = runner_t.Tournament(90, self.y, self.n)
        all_res = t.start()
        self.all_results['test1'] = all_res
        # print(all_results)
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')
    def test_tournament2(self):
        t = runner_t.Tournament(90, self.a, self.n)
        all_res = t.start()
        self.all_results['test2'] = all_res
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')

    def test_tournament3(self):
        t = runner_t.Tournament(90, self.y, self.a, self.n)
        all_res = t.start()
        self.all_results['test3'] = all_res
        # print(all_results)
        place = max(all_res.keys())
        name = all_res[place]
        self.assertTrue(name == 'Ник')

if __name__ == '__main__':
    unittest.main()
