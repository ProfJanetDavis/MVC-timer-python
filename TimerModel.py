import threading
import time
from ObserverPattern import Subject, Observer

class TimerModel(Subject):
   """Implements a countdown timer with a one-second resolution."""

   def __init__(self, seconds):
       """Initialize the timer with the given initial time in seconds."""
       self.currentTime = 0     # Invariant: currentTime >= 0
       self.running = False     # True when thread is running
       self.thread = threading.Thread(target=self._thread_function) 
       self.lock = threading.Lock()
       self.observers = []
       self.set_time(seconds)

   def _thread_function(self):
       """Count down one second at a time.
          Notify observers at each second and at the end of the timer.
       """
       while self.running and self.currentTime > 0:
           time.sleep(1)
           with self.lock:
               self.currentTime -= 1
           self.notify()
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
       self.thread.start()
       self.notify()

   def stop(self):
       """Stop the timer."""
       self.running = False
       self.thread.join()
       self.notify()
   
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

if __name__ == '__main__':
    timer = TimerModel(10)
    timer.start()
    print("Liftoff!")
    timer.stop()
