#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sts=4:tw=80:
################################################################################
# Package: xuniverse
# File: xuniverse/dialogs.py
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
from gi.repository import Gtk,GObject
import data

class FirstRunAssistant_Pages(object):
        (
            INTRO,
            GAMES,
            X3TC_EXECUTABLES,
            X3TC_SAVEGAMES,
            X3AP_EXECUTABLES,
            X3AP_SAVEGAMES,
            DATALOADER,
            CONFIRM
        )=range(8)
        def __init__(self):
            object.__init__(self)

class SelectGameExecutableDialog_GUI(object):
    _OBJECTS_={
        'dialog':'SelectGameExecutableDialog',
    }
    _GUI_=dict(file=config.SETTINGS['uifile'],objects=[_OBJECTS_['dialog']])

    def __init__(self):
        self.__builder=Gtk.Builder()
        builder.add_objects_from_file(_GUI_['file'],_GUI_['objects'])
        self._objmap_=dict()
    @property
    def builder(self):
        return self.builder

    def get_object(self,oid):
        return self.builder.get_object(_OBJECTS_.get(oid,oid))

    @property
    def dialog(self):
        dialog=self.builder.get_object('dialog')
        if not hasattr(dialog,'gui_handle'):
            setattr(dialog,'gui_handle',self)
            for attr,value in self._objmap_.iteritems():
                setattr(dialog,attr,value)
        return dialog

    def _on_toplevel_destroy(self,toplevel):
        for attr in self._objmap_.iterkeys():
            if hasattr(toplevel,attr):
                delattr(toplevel,attr)
        if hasattr(toplevel,'gui_handle'):
            delattr(toplevel,'gui_handle')

def SelectGameExecutableDialog():
    return SelectGameExecutableDialog_GUI().dialog

################################################################################

class FirstRunAssistant_GUI(object):
    _OBJECTS_={
        'assistant':'FirstRunAssistant',
        'action-area': 'FirstRunAssistant.action-area',
        'advanced-options-checkbutton':'FirstRunAssistant.advanced-options-checkbutton',
        'x3ap-checkbutton':'FirstRunAssistant.x3ap-checkbutton',
        'x3ap-executables-liststore':'FirstRunAssistant.x3ap-executables-liststore',
        'x3ap-executables-scrolledwindow':'FirstRunAssistant.x3ap-executables-scrolledwindow',
        'x3ap-executables-toolbar':'FirstRunAssistant.x3tc-executables-toolbar',
        'x3tc-executables-add-toolbutton':'FirstRunAssistant.x3tc-executables-add-toolbutton',
        'x3ap-executables-treeview':'FirstRunAssistant.x3tc-executables-treeview',
        'x3tc-checkbutton':'FirstRunAssistant.x3tc-checkbutton',
        'x3tc-executables-liststore':'FirstRunAssistant.x3tc-executables-liststore',
        'x3tc-executables-scrolledwindow':'FirstRunAssistant.x3tc-executables-scrolledwindow',
        'x3tc-executables-toolbar':'FirstRunAssistant.x3tc-executables-toolbar',
        'x3tc-executables-treeview':'FirstRunAssistant.x3tc-executables-treeview'}

    _GUI_=dict(file=config.SETTINGS['uifile'],
               objects=[_OBJECTS_['x3ap-executables-liststore'],
                        _OBJECTS_['x3tc-executables-liststore'],
                        _OBJECTS_['assistant']])

    pages=FirstRunAssistant_Pages()

    def __init__(self,exit_on_cancel=False):
        object.__init__(self)
        self.builder=Gtk.Builder()
        self.builder.add_objects_from_file(self._GUI_['file'],self._GUI_['objects'])

        self._objmap_=dict(
            pages=self.pages,
            action_area=self.action_area,
            advanced_options_checkbutton=self.advanced_options_checkbutton,
            advanced_options_enabled=self.advanced_options_enabled,
            x3ap_checkbutton=self.x3ap_checkbutton,
            x3ap_enabled=self.x3ap_enabled,
            x3tc_checkbutton=self.x3tc_checkbutton,
            x3tc_enabled=self.x3tc_enabled)

        self.builder.connect_signals(self)

        self.assistant.connect('destroy',self._on_toplevel_destroy)
        self.assistant.set_forward_page_func(self._forward_page_func)


    def get_object(self,oid):
        return self.builder.get_object(self._OBJECTS_.get(oid,oid))

    @property
    def assistant(self):
        assistant=self.get_object('assistant')
        if not hasattr(assistant,'gui_handle'):
            setattr(assistant,'gui_handle',self)
            for attr,value in self._objmap_.iteritems():
                setattr(assistant,attr,value)
        return assistant

    @property
    def action_area(self):
        return self.get_object('action-area')

    @property
    def advanced_options_checkbutton(self):
        return self.get_object('advanced-options-checkbutton')

    @property
    def advanced_options_enabled(self):
        return self.advanced_options_checkbutton.get_active()



    @property
    def x3ap_checkbutton(self):
        return self.get_object('x3ap-checkbutton')

    @property
    def x3ap_enabled(self):
        return self.x3ap_checkbutton.get_active()


    @property
    def x3tc_checkbutton(self):
        return self.get_object('x3tc-checkbutton')

    @property
    def x3tc_enabled(self):
        return self.x3tc_checkbutton.get_active()

    @property
    def x3tc_executables_scrolledwindow(self):
        return self.get_object('x3tc-executables-scrolledwindow')

    @property
    def x3tc_executables_toolbar(self):
        return self.get_object('x3tc-executables-toolbar')

    @property
    def x3tc_executables_add_toolbutton(self):
        return self.get_object('x3tc-executables-add-toolbutton')

    def _forward_page_func(self,current_page,*args):
        def get_advanced_page():
            if self.advanced_options_enabled:
                return self.pages.DATALOADER
            return self.pages.CONFIRM

        if current_page == self.pages.GAMES:
            if self.x3tc_enabled:
                return self.pages.X3TC_EXECUTABLES
            elif self.x3ap_enabled:
                return self.pages.X3AP_EXECUTABLES
            return get_advanced_page()
        elif current_page == self.pages.X3TC_SAVEGAMES:
            if self.x3ap_enabled:
                return self.pages.X3AP_EXECUTABLES
            return get_advanced_page()
        elif current_page == self.pages.X3AP_SAVEGAMES:
            return get_advanced_page()
        return (current_page + 1)

    #### Signal Handles ########################################################

    def _on_root_widget_destroy(self,root_widget):
        self._on_toplevel_destroy(root_widget)

    def _on_toplevel_destroy(self,toplevel):
        for attr in self._objmap_.iterkeys():
            if hasattr(toplevel,attr):
                delattr(toplevel,attr)
        if hasattr(toplevel,'gui_handle'):
            delattr(toplevel,'gui_handle')

    def on_assistant_apply(self,assistant):
        pass
    def on_assistant_cancel(self,assistant):
        pass
    def on_assistant_close(self,assistant):
        pass
    def on_assistant_prepare(self,assistant,*args):
        """
            Called for every page!
        """
        pass
    def on_assistant_escape(self,assistant):
        pass

    def on_x3ap_executables_add_toolbutton_clicked(self,button):
        pass

    def on_x3tc_executables_add_toolbutton_clicked(self,button):
        dialog=SelectGameExecutableDialog()
        if dialog.run() == Gtk.ResponseType.APPLY:
            #TODO: add to liststore
        dialog.hide()
        dialog.destroy()

    def on_x3tc_executables_edit_toolbutton_clicked(self,button):
        pass

    def on_x3tc_executables_remove_toolbutton_clicked(self,button):
        pass



def FirstRunAssistant(exit_on_cancel=False):
    return FirstRunAssistant_GUI(exit_on_cancel=exit_on_cancel).assistant

