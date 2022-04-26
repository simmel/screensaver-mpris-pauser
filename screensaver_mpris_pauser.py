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

    # Create and run main loop
    loop = gi.repository.GLib.MainLoop()
    loop.run()


if __name__ == "__main__":
    main()
