from threading import Thread, Lock
from time import sleep
from ObserverPattern import Subject, Observer

class TimerModel(Subject):
    """
    Implements a countdown timer with a one-second resolution.
    Observers will be notified for each value from the initial value down to 
    zero, unless the thread is stopped, after which there will be no further
    notifications. 
    """

    def __init__(self):
        """Initialize the timer."""
        self._time = 0            # Invariant: time >= 0
        self._running = False     # True when a thread is running
        self._thread = None       
        self._lock = Lock()
        self._observers = []

    # See documentation for properties:
    # https://realpython.com/python-getter-setter/#using-properties-instead-of-getters-and-setters-the-python-way

    @property 
    def time(self):
        """Get current time in seconds."""
        return self._time

    @time.setter
    def time(self, value):
        """Set current time to the given non-negative value in seconds."""
        assert value >= 0, "Time in seconds must be non-negative"
        with self._lock:
            self._time = value

    @property 
    def running(self):
        """True if a thread is running and not about to stop."""
        return self._running

    def _timer(self):
        """
        Count down one second at a time, stopping at zero.
        This function should always be run in a new _thread.
        """
        while self._running and self._time > 0:
            self.notify()
            sleep(1)
            with self._lock:
                self._time -= 1
        if self._running:
            self._running = False
            self.notify()

    def start_thread(self):
        """Start the timer from the current time."""
        self._running = True
        self._thread = Thread(target=self._timer) 
        self._thread.start()

    def stop_thread(self):
        """Stop the timer, retaining the current time."""
        if self._running:
            self._running = False
            self._thread.join()
    
    def attach(self, observer):
        """Add an observer."""
        self._observers.append(observer)

    def detach(self, observer):
        """Remove an observer."""
        self._observers.remove(observer)

    def notify(self):
        """Call update on all observers."""
        for o in self._observers:
            o.update(self)

class TestObserver(Observer):
     def update(self, subject):
         print(subject._time)

if __name__ == '__main__':
     my_timer = TimerModel()
     my_timer.attach(TestObserver())

     print("Expected output: 0")
     my_timer.start_thread()
     sleep(1)
     assert not my_timer.running

     print("Expected output: 10 9 8 7 6 5")
     my_timer.time = 10
     my_timer.start_thread()
     sleep(5.5)
     assert my_timer.running

     print("Expected output: 9 8")
     my_timer.time = 10
     sleep(2)
     assert my_timer.running
     my_timer.stop_thread()
     my_timer.stop_thread()
     assert not my_timer.running

     print("No output for 5 seconds")
     sleep(5)

     print("Expected output: 3 2 1 0")
     my_timer.time = 3
     my_timer.start_thread()
     assert my_timer.running
     sleep(5)
     assert not my_timer.running
     
     print("Tests completed")
