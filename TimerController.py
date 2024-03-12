from enum import Enum
from TimerModel import TimerModel
from ObserverPattern import Observer

class TimerController(Observer):
    """Decouples the model from the view."""

    def __init__(self, view):
        self._running = False
        self._paused = False
        self._view = view
        self._model = TimerModel()
        self._model.attach(self)

    def update(self, timer):
        """On notification from the model, update the view."""
        self._view.update_time(self._model.time)
        if timer.time == 0:
            self._running = False
            self._view.timer_done()

    def start(self, time):
        """Start the timer at the given time."""
        self._running = True
        self._model.stop_thread()
        self._model.time = time
        self._model.start_thread()

    def stop(self):
        """Stop the timer and clear the time."""
        self._running = False
        self._model.stop_thread()
        self._model.time = 0

    def pause(self):
        """Pause the timer at its current time."""
        self._paused = True
        self._model.stop_thread()

    def resume(self):
        """Resume the timer from its current time."""
        if self._running and self._paused:
            self._paused = False
            self._model.start_thread()

    def stopped(self):
        """True if the timer is stopped."""
        return not self._running

    def running(self):
        """True if the timer is running."""
        return self._running and not self._paused 

    def paused(self):
        """True if the timer is paused."""
        return self._running and self._paused
