import threading
import time
from ObserverPattern import Subject, Observer

class TimerModel(Subject):
   """
   Implements a countdown timer with a one-second resolution.
   Observers will be notified for each value from the initial value down to 
   zero, unless the timer is stopped, after which there will be no further
   notifications. 
   """

   def __init__(self, seconds):
       """Initialize the timer with the given initial time in seconds."""
       self.currentTime = 0     # Invariant: currentTime >= 0
       self.running = False     # True when a thread is running
       self.thread = None       
       self.lock = threading.Lock()
       self.observers = []
       self.set_time(seconds)

   def _thread_function(self):
       """Count down one second at a time, stopping at zero."""
       while self.running and self.currentTime > 0:
           self.notify()
           time.sleep(1)
           with self.lock:
               self.currentTime -= 1
       if self.running:
           self.running = False
           self.notify()

   def set_time(self, seconds):
       """Set current time to the given value of seconds."""
       assert seconds > 0, "Time in seconds must be positive"
       with self.lock:
           self.currentTime = seconds

   def start(self):
       """Start the timer."""
       self.running = True
       self.thread = threading.Thread(target=self._thread_function) 
       self.thread.start()

   def stop(self):
       """Stop the timer."""
       if self.running:
           self.running = False
           self.thread.join()
   
   def attach(self, observer):
       """Add an observer."""
       self.observers.append(observer)

   def detach(self, observer):
       """Remove an observer."""
       self.observers.remove(observer)

   def notify(self):
       """Call update on all observers."""
       for o in self.observers:
           o.update(self)

class TestObserver(Observer):
    def update(self, subject):
        print(subject.currentTime)

if __name__ == '__main__':
    my_timer = TimerModel(10)
    my_timer.attach(TestObserver())

    print("Expected output: 10 9 8 7 6 5")
    my_timer.start()
    time.sleep(5.5)

    print("Expected output: 9 8")
    my_timer.set_time(10)
    time.sleep(2)
    my_timer.stop()
    my_timer.stop()

    print("Expected output: 3 2 1 0")
    my_timer.set_time(3)
    my_timer.start()
