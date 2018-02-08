#!/usr/bin/env python
####BEGIN:HEAD####
# Author: Christian Moser
# License: GPL-V3
# Copyright: 2018
####END####

from gi.repository import Gtk,GObject,Gio,GLib
import sys,os
import config
import dialogs,navigator,browser,xgame,data

class ApplicationWindow(Gtk.ApplicationWindow):
    CONFIG=config.SETTINGS['ApplicationWindow']

    def __init__(self,application):
        print("1.0")
        Gtk.ApplicationWindow.__init__(self,application=application)
        self.__builder=Gtk.Builder()
        self.__vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.add(self.vbox)
        self.set_default_size(400,400)
        self.show_all()

    @GObject.Property
    def vbox(self):
        """Vertical Gtk.Box of the Window."""
        return self.__vbox

    @GObject.Property
    def builder(self):
        """Gtk.Builder of the Window"""

    def _on_action_quit(self,action,param):
        pass

class Application(Gtk.Application):
    CONFIG=config.SETTINGS['Application']

    def __init__(self,*args,**kwargs):
        Gtk.Application.__init__(self,*args,**kwargs)
        self.__builder=Gtk.Builder()
        self.__toplevels=[]

        self.window=None


    @GObject.Property
    def builder(self):
        """ The builder for Application.
        """
        return self.__builder

    @GObject.Property
    def toplevels(self):
        """ Toplevel Windows.
            !!! NOT IMPLEMENTED !!!
        """
        return self.__toplevels

    def do_startup(self):

        def mk_action(id,callback=None):
            action=Gio.SimpleAction.new(id)
            if callback and callable(callback):
                action.connect('activate',callback)
            return action
        Gtk.Application.do_startup(self)

        self.add_action(mk_action('new',self._on_action_new))
        self.add_action(mk_action('open',self._on_action_open))
        self.add_action(mk_action('quit',self._on_action_quit))


    def do_command_line(self,command_line):
        Gtk.Application.do_command_line(self,command_line)
        self.activate()

    def do_activate(self):
        Gtk.Application.do_activate(self)
        if not self.window:
            self.window=ApplicationWindow(self)
            self.window.connect('delete-event',lambda *args: self.quit())
        self.window.present()

    def _on_action_quit(self,action,param):
        self.quit()

    def _on_action_new(self,action,param):
        pass

    def _on_action_open(self,action,param):
        pass

    def _on_action_recent(self,action,param):
        pass
