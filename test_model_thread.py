import unittest

from io import StringIO
from time import sleep
from observer import Observer
from model_thread import ThreadTimerModel

class TestObserver(Observer):
    def __init__(self, writer):
        """Initialize with a stream to write output to."""
        self.writer = writer

    def update(self, subject):
        self.writer.write(f"{subject._time} ")

class TestTimerModel(unittest.TestCase):

    def setUp(self):
        self.buffer = StringIO()
        self.timer = ThreadTimerModel()
        self.timer.attach(TestObserver(self.buffer))

    def tearDown(self):
        self.timer.stop_timer()
        self.buffer.close()

    def test_timer(self):
        """When given a positive time, the timer should stop running when it reaches 0."""
        self.timer.time = 3
        self.timer.start_timer()
        sleep(3.5)
        self.assertFalse(self.timer.running)
        self.assertEqual(self.timer.time, 0)
        self.assertEqual(self.buffer.getvalue(), "3 2 1 0 ")

    def test_uninitialized_timer(self):
        """When uninitialized, the timer should immediately stop at 0."""
        self.timer.start_timer()
        sleep(1)
        self.assertEqual(self.buffer.getvalue(), "0 ")

    def test_stopped_timer(self):
        """When stopped, the timer should not produce its next value."""
        self.timer.time = 5
        self.timer.start_timer()
        sleep(2.5)
        self.assertTrue(self.timer.running)
        self.timer.stop_timer()
        sleep(1)
        self.assertFalse(self.timer.running)
        self.assertEqual(self.buffer.getvalue(), "5 4 3 ")
        self.assertEqual(self.timer.time, 2)

    def test_set_running_timer(self):
        """
        When a new time is set on a running timer, the next time produced should be one
        less than the new time.
        """
        self.timer.time = 3
        self.timer.start_timer()
        sleep(2.5)
        self.assertTrue(self.timer.running)
        self.assertEqual(self.timer.time, 1)
        self.timer.time = 5
        sleep(5.5)
        self.assertEqual(self.buffer.getvalue(), "3 2 1 4 3 2 1 0 ")

if __name__ == '__main__':
    unittest.main()
