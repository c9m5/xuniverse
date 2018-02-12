#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sts=4:tw=80:
################################################################################
# Package: xuniverse
# File: xuniverse/config.py
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
#           Machines) Research (Redmond?),...), AND TORT (expecially P.U.S -
#           Punish United System!).
################################################################################

import gi; gi.require_version('Gtk','3.0')
from gi.repository import GLib
import sys,os

PACKAGE='xuniverse'
VERSION=(0,0,0)
XUNIVERSE_CONFIG_DIR=os.getenv('XUNIVERSE_CONFIG_DIR',os.path.join(os.path.normpath(GLib.get_user_config_dir()),PACKAGE))
XUNIVERSE_CONFIG='xuniverse.config'

if os.getenv('XUNIVERSE_CONFIG',None):
    if os.path.exists(os.path.abspath(os.getenv('XUNIVERSE_CONFIG',None))):
        XUNIVERSE_CONFIG=os.path.abspath(os.getenv('XUNIVERSE_CONFIG',None))
    else:
        XUNIVERSE_CONFIG=os.getenv('XUNIVERSE_CONFIG')
if not os.path.isabs(XUNIVERSE_CONFIG):
    XUNIVERSE_CONFIG=os.path.join(XUNIVERSE_CONFIG_DIR,XUNIVERSE_CONFIG or 'xuniverse-config')

PACKAGE_DIR=os.path.dirname(os.path.normpath(__file__))


FIRST_RUN=os.path.exists(XUNIVERSE_CONFIG)

SETTINGS={
    'configdir': XUNIVERSE_CONFIG_DIR,
    'config': XUNIVERSE_CONFIG,
    'datadir': os.getenv('XUNIVERSE_DATA_DIR',os.path.join(os.path.normpath(GLib.get_user_data_dir()),PACKAGE)),
    'cachedir': os.getenv('XUNVIERSE_CACHE_DIR',os.path.join(os.path.normpath(GLib.get_user_data_dir()),PACKAGE)),
    'firstrun': not os.path.exists(XUNIVERSE_CONFIG),
    'uifile':os.path.join(PACKAGE_DIR,'xuniverse.ui'),

    'Application': {
        'ui': {
            'file':'xuniverse.ui',
            'objects': ['ApplicationMenu']}},
    'ApplicationWindow': {
        'ui': {
            'file':'xuniverse.ui',
            'objects':['ApplicationToolbar']}},
    'DialogNew': {
        'ui': {
            'file':'xuniverse.ui',
            'objects':['DialogNew']}},
    'SectorView': {},
    'Browser': {},
    'Navigator': {},
    'UniverseNavigatorPage':{'navigator':dict(name='xuniverse.navigator.page')},
    'ToolsNavigatorPage':{'navigator':dict(name='xuniverse.navigator.page')},
    'Data': {
        'games': {
            'x3tc': dict(title='X3 - Terran Conflict'),
            'x3ap': dict(title='X3 - Albion Prelude')},
        'importers': {
            'xadrian':dict(importer='xadrian.import_data',
                           init_data=True,
                           games=['x3tc','x3ap'],
                           fields=['races','suns','wares','factories','sectors']),
            'xml': dict(fields='ALL'),
            'shelve': dict(fields='ALL')},
        'exporters':{
            'xml': dict(fields='ALL'),
            'shelve': dict(fields='ALL')}},
    'Context': {
        'importers': {
            'data': dict(create_new=True),
            'xml': {},
            'shelve': {}},
        'exporters': {
            'data': {},
            'xml': {},
            'shelve': {}}}
}

