#!/usr/bin/env python
####BEGIN:HEAD####
# Author: Christian Moser
# License: GPL-V3
# Copyright: 2018
####END####

from gi.repository import Gtk,GObject

class Navigator(Gtk.StackSidebar):
    def __init__(self,gameid='x3tc',context=None):
        Gtk.StackSidebar.__init__(self,stack=__create_stack)

    def __create_stack(self):
        stack=Gtk.Stack()
        return stack
