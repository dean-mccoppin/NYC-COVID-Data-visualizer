# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:39:29 2020

@author: truet
"""

import git, datetime, os, shutil, stat


giturl = 'https://github.com/nychealth/coronavirus-data.git'
project_folder = r'C:\Users\truet\Documents\COVID Data project'
virus_data = "C:/Users/truet/Documents/COVID Data project/coronavirus-data"


if os.path.isdir(virus_data):
    os.chmod('C:/Users/truet/Documents/COVID Data project/coronavirus-data\\.git\\objects\\pack\\pack-662f0b50a4629c6f990a942bee204db0eeef795b.idx', stat.S_IRWXO)
    shutil.rmtree(virus_data)
    git.Git(project_folder).clone(giturl)
    
else:
    git.Git(project_folder).clone(giturl)