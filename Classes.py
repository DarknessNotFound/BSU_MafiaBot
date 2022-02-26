# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:56:31 2022

@author: Easton Ingram
"""

from random import choice

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
    
    def assign_role(self, role):
        """ Assigns a random role from an array and then removes an instance of that role from the list. """
        self.m_role = choice(role)

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
            

class Game:
    m_player_list = []
    m_role_list = []
    
    preset1 = Preset("Vanilla", [Mafia(), Mafia()])
    
    m_presets = [preset1]
    
    def find_player(self, name):
        for player in self.m_player_list:
            if name == player.m_name:
                return player
        return False
    
    def add_player(self, name):
        if self.find_player(name) == False:
            self.m_player_list.append(Player(name))
            return name + " has joined the game."
        else:
            return "Player already in game"
        
    def remove_player(self, name):
        if self.find_player(name):
            self.m_player_list.remove(self.find_player(name))
            return name + " has left the game."
        else:
            return "Player not in game"
    
    def new(self):
        self.m_player_list = []
        
    def list_queue(self):
        string = ""
        if len(self.m_player_list)== 0:
            string+= "No players in game queue"
        for player in self.m_player_list:
            string+= player.m_name + "\n"
        return string
            
    def add_role(self, role):
        if role == "Mafia":
            self.m_role_list.append(Mafia())
        elif role == "Villager":
            self.m_role_list.append(Villager())
        else:
            return "Role not found"
        return role + " added to role selection"
    
    def find_role(self, title):
        for role in self.m_role_list:
            if title == role.m_title:
                return role
        return False
    
    def list_roles(self):
        string = ""
        if len(self.m_role_list)== 0:
            string+= "No roles selected"
        for role in self.m_role_list:
            string+= role.m_title + "\n"
        return string
    
    def remove_role(self, title):
        if self.find_role(title):
            self.m_role_list.remove(self.find_role(title))
            return title + " unselected."
        else:
            return "Role not previously selected"
        
    def all_presets(self):
        string = ""
        if len(self.m_presets)== 0:
            string+= "No presets"
        else:
            for preset in self.m_presets:
                string+= preset.m_name + " - " + preset.display() +" ...\n"
        return string
        
    def find_preset(self, name):
        for preset in self.m_presets:
            if name == preset.m_name:
                return preset
        return False
    
    def assign_preset(self, name):
        if self.find_preset(name):
            self.m_role_list = []
            for role in self.find_preset(name).m_role_list:
                self.add_role(role.m_title)
            return name + " preset declared."
        else:
            return "No such preset"
        
    def fill(self):
        difference = 0
        while(len(self.m_player_list) > len(self.m_role_list)):
            self.add_role("Villager")
            difference += 1
        if difference < 1:
            return "No empty roles to fill"
        else:
            return "Empty roles to match player count filled with Villager roles (" + str(difference) +")"
    
    def good_to_go(self):
        if len(self.m_player_list) == len(self.m_role_list):
            return True
        else:
            return False
        