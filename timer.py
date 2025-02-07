import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Timer")
        self.set_border_width(15)

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

        label1 = Gtk.Label(label="Automatic Date & Time", xalign=0)
        vbox.pack_start(label1, True, True, 0)

        listbox.add(row)



        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)


        self.button1 = Gtk.ToggleButton(label="Start")
        self.button1.connect("toggled", self.on_start_toggled, "1")
        # hbox.pack_start(button1, True, True, 0)

       
   

        

        self.button2 = Gtk.Button(label="Reset")
        self.button2.connect("clicked", self.on_reset_clicked)

        hbox.pack_start(self.button1, True, True, 0)
        hbox.pack_start(self.button2, True,True, 0)

        listbox.add(row)
    



    def on_reset_clicked(self, widget):
        print("Reset clicked")

    def on_start_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

