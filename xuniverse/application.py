#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sts=4:tw=80:
################################################################################
# Package: xuniverse
# File: xuniverse/application.py
# Author: Christian Moser
################################################################################
#
# Copyright (C) 2018  Christian Moser
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################

import config
from gi.repository import Gtk,GObject,Gio,GLib,Gdk,GdkPixbuf
import sys,os
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

        self.navigator=navigator.NavigatorSidebar()
        self.browser=browser.Browser()

        try:
            self.hpaned=Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
            self.hpaned.pack1(self.navigator,False,True)
            self.hpaned.pack2(self.browser,True,False)
            self.vbox.pack_start(self.hpaned,True,True,0)
            print("1.2")
        except:
            pass

        self.statusbar=Gtk.Statusbar()
        self.vbox.pack_start(self.statusbar,False,True,0)
        self.set_default_size(400,400)
        self.add(self.vbox)
        self.show_all()

    def _on_action_quit(self,action,param):
        pass

class Application(Gtk.Application):
    GUI=dict(file=config.SETTINGS['uifile'],
             objects=['ApplicationMenu'])

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

        if config.SETTINGS.get('firstrun',False):

            def _on_cancel(a):
                a.hide()
                a.destroy()
                exit(0)

            assistant=dialogs.FirstRunAssistant()
            assistant.connect('delete-event',Gtk.main_quit)
            assistant.connect('cancel',_on_cancel)
            assistant.present()
            Gtk.main()
            assistant.hide()
            assistant.destroy()
            del assistant


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
