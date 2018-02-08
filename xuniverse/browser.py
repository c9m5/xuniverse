#!/usr/bin/env python
####BEGIN:HEAD####
# Author: Christian Moser
# License: GPL-V3
# Copyright: 2018
####END####

from gi.repository import Gtk,GObject,Gio

class Browser(Gtk.Notebook):
    def __init__(self,gameid="x3tc",context=None):
        Gtk.Notebook.__init__(self)
        if context:
            self.__context=context
        else:
            pass

    @GObject.Property
    def context(self):
        return self.__context

