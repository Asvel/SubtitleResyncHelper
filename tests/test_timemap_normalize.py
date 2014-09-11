# -*- coding: utf-8 -*-

from unittest import TestCase, main

from subsync.timemap import normalize
from subsync.time import Time


def to_time(o):
    if isinstance(o, Time):
        return o
    elif o[0] == '-':
        return -Time(o[1:])
    else:
        return Time(o)


class TestTimemap(TestCase):

    def _test(self, input_, output):
        input_ = [[to_time(v) for v in item] for item in input_]
        output = [dict(zip(('delta', 'until'), map(to_time, item))) for item in output]
        self.assertEqual(normalize(input_), output)

    def test_empty(self):
        self._test([], [])

    def test_single(self):
        self._test([
            ("12:34.567", "12:35.678"),
        ], [
            ("00:01.111", Time(h=100)),
        ])
        self._test([
            ("12:34.567", "12:33.456"),
        ], [
            ("-00:01.111", Time(h=100)),
        ])

    def test_iter(self):
        self._test(iter([
            ("12:34.567", "12:35.678"),
        ]), [
            ("00:01.111", Time(h=100)),
        ])

    def test_part(self):
        self._test([
            ("11:11.111", "11:22.111"),
            ("12:22.000",),
            ("12:34.567", "12:35.678"),
        ], [
            ("00:11.000", "12:22.000"),
            ("00:01.111", Time(h=100)),
        ])

    def test_tiny_delta(self):
        for input_ in [
            ("12:35.567", "12:35.567"),
            ("12:35.567", "12:35.571"),
            ("12:35.567", "12:35.563"),
        ]:
            self._test([
                input_,
            ], [
                ("00:00.000", Time(h=100)),
            ])

    def test_average(self):
        self._test([
            ("12:34.367", "12:35.477"),
            ("12:34.567", "12:35.678"),
            ("12:34.767", "12:35.879"),
        ], [
            ("00:01.111", Time(h=100)),
        ])
        self._test([
            ("00:02.000", "00:01.500"),
            ("12:34.167", "12:35.272"),
            ("12:34.367", "12:35.477"),  #
            ("12:34.567", "12:35.678"),  #
            ("12:34.767", "12:35.879"),  #
            ("12:34.967", "12:36.084"),
            ("12:45.678", "12:44.678"),
        ], [
            ("-00:00.500", "12:34.167"),
            ("00:01.105", "12:34.367"),
            ("00:01.111", "12:34.967"),
            ("00:01.117", "12:45.678"),
            ("-00:01.000", Time(h=100)),
        ])


if __name__ == '__main__':
    main()
