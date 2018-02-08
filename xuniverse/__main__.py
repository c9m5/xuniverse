#!/usr/bin/env python
####BEGIN:HEAD####
# Author: Christian Moser
# License: GPL-V3
# Copyright: 2018
####END####

import gi; gi.require_version('Gtk','3.0')
from xuniverse.application import Application

print("Starting XUniverse")
app=Application()
app.run()
