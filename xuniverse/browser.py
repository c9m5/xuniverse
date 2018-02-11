#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sts=4:tw=80:
################################################################################
# Package: xuniverse
# File: xuniverse/browser.py
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

