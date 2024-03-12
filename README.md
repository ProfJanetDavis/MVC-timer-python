**A simple countdown timer application.**
Developed as a straightforward example of the MVC architecture by [@ProfJanetDavis](https://github.com/ProfJanetDavis) for [CS 370 at Whitman College](https://github.com/whitmancs370).

# Usage
- `python3 timer.py gui` runs a graphical timer application.
- `python3 timer.py text` runs a text-based timer in the terminal.
- `python3 test_model.py` runs model unit tests.

# Files
These files are listed in implementation order and recommended reading order.
- `observer.py` demonstrates the use of the Observer pattern in an toy application. Provides abstract base classes for the Subject and Observer roles.
- `thread_example.py` shows how to use the [threading](https://docs.python.org/3/library/threading.html) module for concurrency.
- `model.py` implements a countdown timer using threads and the Observer pattern. 
- `test_model.py` tests the timer model using the [unittest](https://docs.python.org/3/library/unittest.html) framework.
- `controller.py` defines the controller and an abstract base class for the view.
- `view_text.py` implements a text-based timer.
- `view_gui.py` implements a graphical timer using the [tkinter](https://docs.python.org/3/library/tkinter.html) package.
- `timer.py` is the main application, which runs either the graphical or text-based timer depending on its command-line arguments.

# Exercises
1. Run the application. Read the Python files. Follow the links in the documentation. What questions do you have?
2. Modify the text timer to play a sound when the timer is done.
3. Extend the graphical timer view so that the user can choose a sound to play when the timer is done. Try asking ChatGPT for help with the [tkinter](https://docs.python.org/3/library/tkinter.html) package.
4. In the graphical timer view, what happens if you push the time setting buttons while the timer is running? Come up with at least two different ways you could prevent the unexpected behavior, and implement one of them. 
5. In the graphical view, the code to enable and disable buttons is repetitive. Tidy up to eliminate the duplication.
6. Modify the GUI to use Unicode characters or images for play, stop, and pause: ▶ ⏹ ⏸. Research how to display the pause button as either raised or sunken depending on whether the timer is currently paused.
7. Use the [curses](https://docs.python.org/3/library/curses.html) module to make an improved timer view for the terminal.
