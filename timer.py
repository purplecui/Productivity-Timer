import gi
import time
import threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Timer")
        self.set_border_width(15)

        self.duration = 5400
        self.remaining = self.duration
        self.running = False
        self.thread = None

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        self.label1 = Gtk.Label(xalign=0)
        vbox.pack_start(self.label1, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.button1 = Gtk.ToggleButton(label="Start")
        self.button1.connect("toggled", self.on_start_toggled, "1")

        self.button2 = Gtk.Button(label="Reset")
        self.button2.connect("clicked", self.on_reset_clicked)

        hbox.pack_start(self.button1, True, True, 0)
        hbox.pack_start(self.button2, True,True, 0)

        listbox.add(row)

        self.update_timer() #called this here so as to show timer at start of the execution.

    def update_timer(self):
        minutes = self.remaining // 60
        seconds = self.remaining % 60
        self.label1.set_text(f"{minutes:02d}:{seconds:02d}")
        return True

    def timer_thread(self):
        while self.running and self.remaining > 0:
            time.sleep(1)
            self.remaining -= 1
            GLib.idle_add(self.update_timer)


    def on_reset_clicked(self, widget):
        print("Reset clicked")
        self.running = False
        self.remaining = self.duration
        self.update_timer()

    def on_start_toggled(self, button, name):
        if button.get_active():
            button.set_label("Stop")
            state = "on"
            if not self.running:
                self.running = True
                self.thread = threading.Thread(target= self.timer_thread)
                self.thread.start()
        else:
            state = "off"
            button.set_label("Start")
            self.running = False
       
        print("Button", name, "was turned", state)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

