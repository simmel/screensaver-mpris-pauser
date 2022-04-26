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


def pause_all_players():
    for service in session_bus.list_names():
        if service.startswith("org.mpris.MediaPlayer2"):
            logging.info("Pausing %s", service)
            pause_player(service)


def pause_player(player_interface):
    player = session_bus.get_object(player_interface, "/org/mpris/MediaPlayer2")
    player.Pause(dbus_interface="org.mpris.MediaPlayer2.Player")


def pause_mpris(enabled, **kwargs):
    logging.debug("Screensaver %r=%r", kwargs["member"], enabled)
    if kwargs["member"] == "ActiveChanged" and enabled:
        pause_all_players()


if __name__ == "__main__":
    main()
