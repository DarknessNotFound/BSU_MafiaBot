# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:56:31 2022

@author: Easton Ingram
"""

from random import choice

class Game:
    m_player_list = []
    
    def add_player(self, name):
        self.m_player_list.append(Player(name))

class Mafia:
    m_title = "Mafia"
    m_description = "Kill everyone but mafia to win. Get sneaky. Can move bodies and hide them. Don't let anyone see you."
    m_kill = True
    
class Villager:
    m_title = "Villager"
    m_description ="Try not to die. Vote out all killers at town meetings to win. GLHF!"
    m_kill = False
    
class Player:
    def __init__(self,name):
        self.m_name = name
        
    m_name = ""
    m_role = None
    
    def assign_random_role(self, role_list):
        """ Assigns a random role from an array and then removes an instance of that role from the list. """
        self.m_role = choice(role_list)
        role_list.remove(self.m_role)
