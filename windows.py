import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import data
#objects pertaining to Question
Question=Gtk.Grid()
back=Gtk.Button("Go back")
label=Gtk.Label()

Board=Gtk.VBox(spacing=6)
H_Label=Gtk.Label("X for X")
stack=Gtk.Stack()
Q_Label=Gtk.Label("This is the question. It may be long or short but it should at least look good")
A_Label=Gtk.Label("This is the answer! Who knew!")
Q_Label.set_line_wrap(True)
A_Label.set_line_wrap(True)
stack.add_titled(Q_Label, "q", "Question")
stack.add_titled(A_Label, "a", "Answer")
stack_sw=Gtk.StackSwitcher()
stack_sw.set_stack(stack)

Question.set_column_homogeneous(True)
Question.set_row_homogeneous(True)
Question.attach(stack_sw,17,0,20,10)
Question.attach(H_Label, 0,10,40,10)
Question.attach(stack,5,20,30,80)
Question.attach(back,0,100,40,10)

win=Gtk.Window()
win.connect("destroy", Gtk.main_quit)
def on_click(widget):
    global Q_Label
    global A_Label
    win.remove(Board)
    back.connect("clicked", on_return)
    words=widget._value.split(":")
    Q_Label.set_text(data.questions[str(words[0])][str(words[1])])
    A_Label.set_text(data.answers[str(words[0])][str(words[1])])
    H_Label.set_text(str(words[0])+" for " + str(words[1]))
    ctx=widget.get_style_context()
    win.add(Question)
    Question.show_all()
    ctx.add_class("answered")

def on_return(widget):
    win.remove(Question)
    win.add(Board)
    stack.set_visible_child(Q_Label)
