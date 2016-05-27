#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011~2013 Deepin, Inc.
#               2011~2013 Kaisheng Ye
#
# Author:     Kaisheng Ye <kaisheng.ye@gmail.com>
# Maintainer: Kaisheng Ye <kaisheng.ye@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

def touch_file_dir(filepath):
    d = os.path.dirname(filepath)
    if not os.path.exists(d):
        os.makedirs(d)

def convert_filename(theme_dir, theme, oldfile, type):
    newfile = os.path.join(type, theme_dir, theme+"-"+type+".png")
    touch_file_dir(newfile)
    os.system("cp %s %s" % (oldfile, newfile))

current_dir = os.path.dirname(os.path.realpath(__file__))

DIRS = ["IconThemes", "WindowThemes"]

for theme_dir_name in DIRS:
    old_theme_dir = os.path.join(current_dir, "components", theme_dir_name)
    themes = os.listdir(old_theme_dir)
    print "%s: %s" % (theme_dir_name, len(themes))
    for theme in themes:
        old_thumbnail_png = os.path.join(old_theme_dir, theme, "thumbnail.png")
        if os.path.exists(old_thumbnail_png):
            convert_filename(theme_dir_name, theme, old_thumbnail_png, "thumbnail")
