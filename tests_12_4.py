import unittest
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            self.runner = Runner("Леонардо", -5)
            logging.info('test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner, \n{e}', exc_info=True)

    def test_run(self):
        try:
            self.runner = Runner(123, 5)
            logging.info('test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner. \n{e}', exc_info=True)


if __name__ == '__main__':
    unittest.main()
