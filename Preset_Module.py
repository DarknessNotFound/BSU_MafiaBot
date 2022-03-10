# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:06:05 2022

@author: easto
"""

from Role_Module import *

class Preset():
    m_role_list = []
    m_name = ""
    
    def __init__(self, name, role_list):
        self.m_name = name
        self.m_role_list = role_list
    
    def display(self):
        string = ""
        if len(self.m_role_list)== 0:
            string+= "Empty preset"
        for role in self.m_role_list:
            string+= role.m_title + ", "
        return string
    
preset1 = Preset("Vanilla", [Mafia, Mafia])

m_presets = [preset1]
