# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:05:17 2022

@author: easto
"""

class Player:
    def __init__(self,name):
        self.m_name = name
        
    m_name = ""
    m_role = None
    
    def assign_role(self, role):
        self.m_role = role