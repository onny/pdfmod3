from gi.repository import Gtk, Gio
from gi.repository import WebKit

HEIGHT = 500
WIDTH = 800

class MainWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Resolution")
        self.set_border_width(0)
        self.set_default_size(WIDTH, HEIGHT)

        hb = Gtk.HeaderBar()
        hb.props.show_close_button = True
        hb.props.title = "Resolution"
        hb.props.subtitle = "Digital Maths Revision Guide"
        self.set_titlebar(hb)

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="emblem-system-symbolic")
        image = Gtk.Image.new_from_gicon(icon, 1)
        button.add(image)
        button.connect("clicked", self.sidebarShowHide)
        button.set_focus_on_click(False)
        hb.pack_start(button)

        self.sidebarbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        toplevelbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        

        label = Gtk.Label("Contents Selector")
        self.sidebarbox.pack_start(label, True, True, 0)

        self.revealer = Gtk.Revealer()
        self.revealer.set_reveal_child(True)
        self.revealer.add(self.sidebarbox)

        scroller = Gtk.ScrolledWindow()
        content = WebKit.WebView()
        scroller.add(content)
        toplevelbox.pack_start(scroller, True, True, 0)

        content.open("/home/oliver/resolution/placeholder.html")

        toplevelbox.pack_start(self.revealer, False, False, 0)
        self.add(toplevelbox)

    def inital_show(self):
        win.show_all()
        #self.sidebarbox.hide();

    #This works. The sidebar does show/hide.
    def sidebarShowHide(self, button):
        if self.revealer.get_reveal_child():
            self.revealer.set_reveal_child(False)
        else:
            self.revealer.set_reveal_child(True)
        if self.sidebarbox.get_visible():
            self.sidebarbox.hide()
        else:
            self.sidebarbox.show()

    def search_changed(self, searchentry):
        pass

if __name__ == '__main__':
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.inital_show()
    Gtk.main()
