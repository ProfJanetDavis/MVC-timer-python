from sys import argv
from model import ThreadTimerModel
from view_text import TextTimerView
from view_gui import GuiTimerView

Views = {"text": TextTimerView, "gui": GuiTimerView}

if __name__ == '__main__':

    if len(argv) > 2 or (len(argv) == 2 and argv[1] not in Views.keys()):
        print("Usage: python3 timer.py [text|gui]")
        exit(1)
    if len(argv) == 1:
        argv.append("gui")

    model = ThreadTimerModel()
    View = Views[argv[1]]
    View(model).run()
