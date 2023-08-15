# -*- coding: utf-8 -*-
"""
__version__ = '1.0'

Created on 2023.03.06
Author wry

Copyright (c) 2021 Star-Net
"""


class UiManager(object):
    widget_dict = dict()
    page_dict = dict()

    @staticmethod
    def add_page(name, obj):
        UiManager.page_dict[name] = obj

    @staticmethod
    def get_page(name):
        return UiManager.page_dict.get(name)

    @staticmethod
    def add_widget(name, obj):
        UiManager.widget_dict[name] = obj

    @staticmethod
    def get_widget(name):
        return UiManager.widget_dict.get(name)
