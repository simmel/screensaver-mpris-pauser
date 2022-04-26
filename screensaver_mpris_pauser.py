#!/usr/bin/env python3
import logging

import dbus  # type: ignore
import dbus.mainloop.glib  # type: ignore
import gi.repository.GLib  # type: ignore

logging.basicConfig(level=logging.INFO)

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
session_bus = dbus.SessionBus()


def main():
    logging.info("Hello world!")
    session_bus.add_signal_receiver(
        pause_mpris,
        dbus_interface="org.gnome.ScreenSaver",
        path="/org/gnome/ScreenSaver",
        interface_keyword="interface",
        path_keyword="path",
        member_keyword="member",
    )

    # Create and run main loop
    loop = gi.repository.GLib.MainLoop()
    loop.run()


def pause_mpris(enabled, **kwargs):
    logging.debug("Screensaver %r=%r", kwargs["member"], enabled)


if __name__ == "__main__":
    main()
