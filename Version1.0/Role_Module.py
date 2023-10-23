# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:03:04 2022

@author: easto
"""


class Role:
    def __init__(self, title, description, kill):
     self.m_title = title
     self.m_description = description
     self.m_kill = kill    
    
    m_title = ""
    m_description = "" 
    m_kill = None 
    
Mafia = Role("Mafia"
             , "Kill everyone but Mafia to win. Can move bodies and hide them. Get sneaky- don't let anyone see you do Mafia stuff."
             , True)    

Villager = Role("Villager"
                , "Try not to die. Vote out all killers at town meetings to win. GLHF!"
                , False)

Joker = Role("Joker"
             , "Wins if and only if the Joker gets voted out at a town meeting. HAHA"
             , False)

Kannibal = Role("Kannibal"
                , "Kill all other players to win the game. Can consume one body per game, which means that there is no vote or discussion at the town meeting resulting from the death. Can move bodies."
                , True)

Zombie = Role("Zombie"
              , "Once Zombie kill is made, the killer drops dead and the victim becomes the new Zombie. All players who were Zombies win if the Zombie is the last player alive. The Zombie role supersedes all other roles. Cannot move bodies."
              , True)

Judge = Role("Judge"
             , "Once per game, at the town meeting, the Judge can override a majority decision and eliminate a player."
             , False)

Sheriff = Role("Sheriff"
               ,"You have a gun. One bullet. One choice. One kill."
               , False)

Mute = Role("Mute"
            , "A Villager that cannot talk or call body. Unless there is actual blood. Then please say something."
            , False)

Liar = Role("Liar"
            , "The liar is a Villager who must say the opposite of the truth. However, cannot lie about being dead or alive. Cannot call body, but 'not body' and the waving of arms wildly usually gets the message across."
            , False)

Scooby_Doo_Villain = Role("Scooby Doo Villain"
                         ,"If the Scooby Doo Villain scares someone and the other person screams, the scared indivdual immediately turns into a ghost and goes to the graveyard. This character wins if they are the last person alive." 
                         + " -\"and I would have gotten away with it too, if it weren't for you meddling kids!\""
                         , True)

Mimic = Role("Mimic"
             ,"At the end of the role assignment, this character gets randomly assigned a role from the selection, and they become that new role.",
             False)
