#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sts=4:tw=80:
################################################################################
# Package: xuniverse
# File: xuniverse/sector.py
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
#
# Addition: YOU ARE NOT ALLOWED TO USE THIS SOFTWARE TO COMMIT (PROJECT
#           MONARCH) SLAVERY (like UN, EU, BAWAG, PostAG, LAM (Local Area
#           Machines) Research (Redmond?),...), AND TORT, especially but
#           not to P.U.S - Punish United System.
################################################################################

from gi.repository import Gtk,GObject

class SectorView(Gtk.Grid):
    views=['political','ore','silicon']
    def __init__(self,view='political'):
        Gtk.Grid.__init__(self)

class SectorChooser(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)


