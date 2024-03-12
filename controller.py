from abc import ABC, abstractmethod
from observer import Observer
from model import TimerModel

class TimerView(ABC):
    """Displays the timer."""

    @abstractmethod
    def run(self):
        """Called by a client to run the view."""
        pass
    
    @abstractmethod
    def update_time(self):
        """Called by the controller when the timer value may have changed."""
        pass

    @abstractmethod
    def timer_done(self):
        """Called by the controller when the timer reaches 0."""
        pass

class TimerController(Observer):
    """Starts, stops, and pauses the timer model. Updates the timer view."""

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
