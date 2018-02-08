#!/usr/bin/env python
####BEGIN:HEAD####
# Author: Christian Moser
# License: GPL-V3
# Copyright: 2018
####END####

from gi.repository import Gtk,GObject,Gio,GLib,Gdk,GdkPixbuf
import sys,os
import config
import dialogs,navigator,browser,xgame,data

class ApplicationWindow(Gtk.ApplicationWindow):
    CONFIG=config.SETTINGS['ApplicationWindow']

    def __init__(self,application):
        print("1.0")
        Gtk.ApplicationWindow.__init__(self,application=application)
        self.builder=Gtk.Builder()
        self.vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        try:
            self.toolbox=Gtk.FlowBox()
            #self.vbox.pack_start(self.toolbox,False,True,0)
            print("1.1")
        except:
            pass

        try:
            self.hpaned=Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
            #self.vbox.pack_start(self.hpaned,True,True,0)
            print("1.2")
        except:
            pass


        self.set_default_size(400,400)
        self.add(self.vbox)
        self.show_all()

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
