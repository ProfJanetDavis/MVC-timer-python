from abc import ABC, abstractmethod

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

