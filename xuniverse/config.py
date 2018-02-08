#!/usr/bin/env python
# -*- coding: utf-8 -*-
####BEGIN:HEAD####
# Author: Christian Moser
# License: GPL-V3
# Copyright: 2018
####END####

from gi.repository import GLib
import sys,os

PACKAGE='xuniverse'
VERSION=(0,0,0)
USER_CONFIG_DIR=os.path.join(os.path.normpath(GLib.get_user_config_dir()),PACKAGE)
PACKAGE_DIR=os.path.dirname(os.path.normpath(__file__))

SETTINGS={
    'user': {
        'config-dir': USER_CONFIG_DIR,
        'config': os.getenv(USER_CONFIG_DIR,'xuniverse.config')},
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
    'Data': {},
    'Context': {}
}

