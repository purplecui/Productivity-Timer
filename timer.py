import gi
import time
import threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Timer")
        self.set_border_width(30)

        #the duration for countdown goes here but only in seconds
        self.duration = 5400 #5400 secs == 90 mins
        self.remaining = self.duration
        self.running = False
        self.thread = None

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=80)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 80)
        hbox.pack_start(vbox, True, True, 0)

        #label for automated timer
        self.label1 = Gtk.Label(xalign=40)
        self.label1.set_margin_bottom(20)
        vbox.pack_start(self.label1, True, True, 0)

        listbox.add(row)
        

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        # TOGGLE button for multiple(two) state signal
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
        # self.label1.set_text(f"{minutes:02d}:{seconds:02d}")
        self.label1.set_markup(f'<span font="24" weight="bold">{minutes:02d}:{seconds:02d}</span>')
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
            # changes button to stop after initializing counter
            button.set_label("Stop")
            state = "on"
            if not self.running:
                self.running = True
                self.thread = threading.Thread(target= self.timer_thread)
                self.thread.start()
        else:
            state = "off"
            #changes back to start after pressing
            button.set_label("Start")
            self.running = False
       
        print("Button", name, "was turned", state)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

