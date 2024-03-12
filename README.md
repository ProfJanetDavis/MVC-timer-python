Example MVC application developed by [@ProfJanetDavis](https://github.com/ProfJanetDavis) for [CS 370 at Whitman College](https://github.com/whitmancs370).

# Usage
- `python3 view_text.py` runs a text-based timer in the terminal.
- `python3 view_gui.py` runs a graphical timer app.
- `python3 test_model.py` runs model unit tests.

# Files
These files are listed in implementation order and recommended reading order.
- `observer.py` demonstrates the use of the Observer pattern in an abstract context. Provides abstract bases classes for Subject and Observer.
- `thread_example.py` shows how to use the `threading library` for concurrency.
- `model.py` implements a countdown timer using threads and the Observer pattern. 
- `test_model.py` tests the timer model using the `unittest` framework.
- `controller.py` defines the controller and an abstract base class for the view.
- `view_text.py` implements a text-based timer.
- `view_gui.py` implements a graphical timer using the `tkinter` library.

# Exercises
1. Read and run all Python files. Follow the links in the documentation. What questions do you have?
2. Modify the text timer to play a sound when the timer is done.
3. In `view_gui.py`, the code to enable and disable buttons is repetitive. Refactor this code to eliminate the duplication.
4. In the graphical timer app, what happens if you push the time setting buttons while the timer is running? Come up with at least two different ways you could prevent the unexpected behavior, and implement one of them.
5. Modify the GUI to use Unicode characters or images for play, stop, and pause: ▶ ⏹ ⏸. Research how to display the pause button as either raised or sunken depending on whether the timer is currently paused.
5. Extend the graphical timer app so that the user can choose a sound to play when the timer is done.
7. Use the `curses` library to make an improved text-based timer view.
