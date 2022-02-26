# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:56:31 2022

@author: Easton Ingram
"""
            
from Player_Module import Player
from Preset_Module import *

from random import choice

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
    def assign_random_roles(self):
        copy_roles = self.m_role_list
        for player in self.m_player_list:
            role = choice(copy_roles)
            player.assign_role(role)
            copy_roles.remove(role)
    def player_role(self, name):
        return "Your role is " + self.find_player(name).m_role.m_title + "\nDescription: " + self.find_player(name).m_role.m_description
    
game = Game()
