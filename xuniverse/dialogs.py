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
#
# Addition: YOU ARE NOT ALLOWED TO USE THIS SOFTWARE TO COMMIT (PROJECT
#           MONARCH) SLAVERY (like UN, EU, BAWAG, PostAG, LAM (Local Area
#           Machines) Research (Redmond?),...), AND TORT (expecially P.U.S -
#           Punish United System!).
################################################################################

import config
from gi.repository import Gtk,GObject
import sys,os

import data

################################################################################

class SelectExecutableDialogX3TC_GUI(object):
    _OBJECTS_={
        'dialog':'SelectExecutableDialogX3TC',
        'apply-button':'SelectExecutableDialogX3TC.apply-button',
        'cancel-button':'SelectExecutableDialogX3TC.cancel-button',
        'executable-label':'SelectExecutableDialogX3TC.executble-label',
        'executable-filechooserbutton':'SelectExecutableDialogX3TC.executable-filechooserbutton',
        'name-label':'SelectExecutableDialogX3TC.name-label',
        'name-entry':'SelectExecutableDialogX3TC.name-entry',
    }
    _GUI_=dict(file=config.SETTINGS['uifile'],
               objects=[_OBJECTS_['dialog'],
                        'x3tc-executable-filter'])

    def __init__(self,parent=None,name='default',executable=None):
        self.__builder=Gtk.Builder()
        self.builder.add_objects_from_file(self._GUI_['file'],self._GUI_['objects'])
        self._objmap_=dict(
            executable_label=self.executable_label,
            executable_filechooserbutton=self.executable_filechooserbutton,
            name_label=self.name_label,
            name_entry=self.name_entry,
            apply_button=self.apply_button,
            cancel_butoon=self.cancel_button)

        if parent:
            self.dialog.set_transient_for(parent)
        self.builder.connect_signals(self)
        self.name_entry.set_text(name)
        if executable:
            self.executable_filechooserbutton.set_filename(executable)
            self.apply_button.set_sensitive(os.path.exists(executable))

    @property
    def builder(self):
        return self.__builder

    def get_object(self,oid):
        return self.builder.get_object(self._OBJECTS_.get(oid,oid))

    @property
    def dialog(self):
        dialog=self.get_object('dialog')
        if not hasattr(dialog,'gui_handle'):
            setattr(dialog,'gui_handle',self)
            for attr,value in self._objmap_.iteritems():
                setattr(dialog,attr,value)
        return dialog

    @property
    def apply_button(self):
        return self.get_object('apply-button')

    @property
    def cancel_button(self):
        return self.get_object('cancel_button')

    @property
    def executable_label(self):
        return self.get_object('executable-label')

    @property
    def executable_filechooserbutton(self):
        return self.get_object('executable-filechooserbutton')

    @property
    def name_label(self):
        return self.get_object('name-label')

    @property
    def name_entry(self):
        return self.get_object('name-entry')


    def _on_toplevel_destroy(self,toplevel):
        for attr in self._objmap_.iterkeys():
            if hasattr(toplevel,attr):
                delattr(toplevel,attr)
        if hasattr(toplevel,'gui_handle'):
            delattr(toplevel,'gui_handle')

    def on_executable_filechooserbutton_file_set(self,filechooser):
        if os.path.exists(self.executable_filechooserbutton.get_filename()):
            self.apply_button.set_sensitive(True)

def SelectExecutableDialogX3TC(parent=None,name='default',executable=None):
    return SelectExecutableDialogX3TC_GUI(parent=parent,name=name,executable=executable).dialog

################################################################################

class RemoveExecutableDialog_GUI(object):
    _OBJECTS_={
        'dialog':'RemoveExecutableDialog'}
    _GUI_=dict(file=config.SETTINGS['uifile'],
               objects=[_OBJECTS_['dialog']])

    def __init__(self,parent=None,executable=""):
        self.__builder=Gtk.Builder()
        self.builder.add_objects_from_file(_GUI_['file'],_GUI_['objects'])

    @property
    def builder(self):
        return self.__builder

    @property
    def dialog(self):
        return self.get_object('dialog')

    def get_object(self,oid):
        return sel.builder.get_object(oid)

def RemoveExecutableDialog(parent=None):
    return RemoveExecutableDialog_GUI()

################################################################################

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

class FirstRunAssistant_GUI(object):
    _OBJECTS_={
        'assistant':'FirstRunAssistant',
        'action-area': 'FirstRunAssistant.action-area',
        'advanced-options-checkbutton':'FirstRunAssistant.advanced-options-checkbutton',
        'x3ap-checkbutton':'FirstRunAssistant.x3ap-checkbutton',
        'x3ap-executables-liststore':'FirstRunAssistant.x3ap-executables-liststore',
        'x3ap-executables-scrolledwindow':'FirstRunAssistant.x3ap-executables-scrolledwindow',
        'x3ap-executables-toolbar':'FirstRunAssistant.x3tc-executables-toolbar',
        'x3ap-executables-add-toolbutton':'FirstRunAssistant.x3ap-executables-add-toolbutton',
        'x3ap-executables-edit-toolbutton':'FirstRunAssistant.x3ap-executables-edit-toolbutton',
        'x3ap-executables-remove-toolbutton':'FirstRunAssistant.x3ap-executables-remove-toolbutton',
        'x3ap-executables-treeview':'FirstRunAssistant.x3tc-executables-treeview',
        'x3tc-checkbutton':'FirstRunAssistant.x3tc-checkbutton',
        'x3tc-executables-liststore':'FirstRunAssistant.x3tc-executables-liststore',
        'x3tc-executables-scrolledwindow':'FirstRunAssistant.x3tc-executables-scrolledwindow',
        'x3tc-executables-toolbar':'FirstRunAssistant.x3tc-executables-toolbar',
        'x3tc-executables-add-toolbutton':'FirstRunAssistant.x3tc-executables-add-toolbutton',
        'x3tc-executables-edit-toolbutton':'FirstRunAssistant.x3tc-executables-edit-toolbutton',
        'x3tc-executables-remove-toolbutton':'FirstRunAssistant.x3tc-executables-remove-toolbutton',
        'x3tc-executables-treeview':'FirstRunAssistant.x3tc-executables-treeview',
        'x3tc-savegames-checkbutton':'FirstRunAssistant.x3tc-savegames-checkbutton',
        'x3tc-savegames-backup-checkbutton':'FirstRunAssistant.x3tc-savegames-backup-checkbutton',
        'x3tc-savegames-grid':'FirstRunAssistant.x3tc-savegames-grid',
        'x3tc-savegames-dir-label':'FirstRunAssistant.x3tc-savegames-dir-label',
        'x3tc-savegames-dir-filechooserbutton':'FirstRunAssistant.x3tc-savegames-dir-filechooserbutton',
        'x3tc-savegames-workdir-label':'FirstRunAssistant.x3tc-savegames-workdir-label',
        'x3tc-savegames-workdir-filechooserbutton':'FirstRunAssistant.x3tc-savegames-workdir-filechooserbutton',
        'x3tc-savegames-backupdir-label':'FirstRunAssistant.x3tc-savegames-backupdir-label',
        'x3tc-savegames-backupdir-filechooserbutton':'FirstRunAssistant.x3tc-savegames-backupdir-filechooserbutton'}

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
    def x3ap_executables_add_toolbutton(self):
        return self.get_object('x3ap-executables-add-toolbutton')

    @property
    def x3ap_executables_edit_toolbutton(self):
        return self.get_object('x3ap-executables-edit-toolbutton')

    @property
    def x3ap_executables_remove_toolbutton(self):
        return self.get_object('x3ap-executables-remove-toolbutton')


    @property
    def x3tc_checkbutton(self):
        return self.get_object('x3tc-checkbutton')

    @property
    def x3tc_enabled(self):
        return self.x3tc_checkbutton.get_active()

    @property
    def x3tc_executables_liststore(self):
        return self.get_object('x3tc-executables-liststore')

    @property
    def x3tc_executables_scrolledwindow(self):
        return self.get_object('x3tc-executables-scrolledwindow')

    @property
    def x3tc_executables_toolbar(self):
        return self.get_object('x3tc-executables-toolbar')

    @property
    def x3tc_executables_scrolledwindow(self):
        return self.get_object('x3tc-executables-scrolledwindow')

    @property
    def x3tc_executables_toolbar(self):
        return self.get_object('x3tc-executables-toolbar')

    @property
    def x3tc_executables_add_toolbutton(self):
        return self.get_object('x3tc-executables-add-toolbutton')

    @property
    def x3tc_executables_edit_toolbutton(self):
        return self.get_object('x3tc-executables-edit-toolbutton')

    @property
    def x3tc_executables_remove_toolbutton(self):
        return self.get_object('x3tc-executables-remove-toolbutton')

    @property
    def x3tc_executables_treeview(self):
        return self.get_object('x3tc-executables-treeview')

    @property
    def x3tc_savegames_checkbutton(self):
        return self.get_object('x3tc-savegames-checkbutton')
        
    @property
    def x3tc_savegames_enabled(self):
        return self.x3tc_savegames_checkbutton.get_active()
        
    @property
    def x3tc_savegames_grid(self):
        return self.get_object('x3tc-savegames-grid')
        
    @property
    def x3tc_savegames_backup_checkbutton(self):
        return self.get_object('x3tc-savegames-backup-checkbutton')
    
    @property
    def x3tc_savegames_dir_label(self):
        return self.get_object('x3tc-savegames-dir-label')
        
    @property
    def x3tc_savegames_dir_filechooserbutton(self):
        return self.get_object('x3tc-savegames-dir-filechooserbutton')
    
    @property
    def x3tc_savegames_workdir_label(self):
        return self.get_object('x3tc-savegames-workdir-label')
        
    @property
    def x3tc_savegames_workdir_filechooserbutton(self):
        return self.get_object('x3tc-savegames-workdir-filechooserbutton')
        
    @property
    def x3tc_savegames_backupdir_label(self):
        return self.get_object('x3tc-savegames-backupdir-label')
        
    @property
    def x3tc_savegames_backupdir_filechooserbutton(self):
        return self.get_object('x3tc-savegames-backupdir-filechooserbutton')
        
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
        dialog=SelectExecutableDialogX3TC(self.assistant)
        if dialog.run() == Gtk.ResponseType.APPLY:
            row=self.x3tc_executables_liststore.append()
            self.x3tc_executables_liststore[row][0]=dialog.name_entry.get_text()
            self.x3tc_executables_liststore[row][1]=dialog.executable_filechooserbutton.get_filename()
            self.x3tc_executables_treeview.show()
        dialog.hide()
        dialog.destroy()

    def on_x3tc_executables_edit_toolbutton_clicked(self,button):
        model,row=self.x3tc_executables_treeview.get_selection().get_selected()
        dialog=SelectExecutableDialogX3TC(self.assistant,model.get_value(row,0),model.get_value(row,1))
        if dialog.run() == Gtk.ResponseType.APPLY:
            row=self.x3tc_executables_liststore.append()
            self.x3tc_executables_liststore[row][0]=dialog.name_entry.get_text()
            self.x3tc_executables_liststore[row][1]=dialog.executable_filechooserbutton.get_filename()
            self.x3tc_executables_treeview.show()
        dialog.hide()
        dialog.destroy()

    def on_x3tc_executables_remove_toolbutton_clicked(self,button):
        model,row=self.x3tc_executables_treeview.get_selection().get_selected()
        dialog=RemoveExecutableDialog(self,model.get_value(row,1))

    def on_x3tc_executables_treeview_selection_changed(self,selection):
        model,iter=selection.get_selected()
        if iter is None:
            self.x3tc_executables_edit_toolbutton.set_sensitive(False)
            self.x3tc_executables_remove_toolbutton.set_sensitive(False)
        else:
            self.x3tc_executables_edit_toolbutton.set_sensitive(True)
            self.x3tc_executables_remove_toolbutton.set_sensitive(True)

    def on_x3tc_savegames_checkbutton_toggled(self,checkbutton):
        self.x3tc_savegames_backup_checkbutton.set_sensitive(checkbutton.get_active())
        self.x3tc_savegames_grid.set_sensitive(checkbutton.get_active())
        
    def on_x3tc_savegames_backup_checkbutton_toggled(self,checknutton):
        self.x3tc_savegames_backupdir_label.set_sensitive(checkbutton.get_active())
        self.x3tc_savegames_backupdir_filechooserbutton.set_sensivitive(checkbutton.get_active())

def FirstRunAssistant(parent=None,exit_on_cancel=False):
    return FirstRunAssistant_GUI(exit_on_cancel=exit_on_cancel).assistant

