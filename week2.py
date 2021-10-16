# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:38:48 2021

@author: khongorzul
"""

#Lecture code for week 2


my_string = "Zulaa"
type(my_string)

my_int = -15
type(my_int)

my_float = 15.78
type(my_float)

my_bool = False #True
type(my_bool)

import datetime
today = datetime.date.today()
today.year
today.month
today.day

datetime.datetime.strptime("2017-01-22","%Y-%m-%d") #Convert string to datetime
today.strftime,("%Y - %M - %")


my_list_str = ["bat", "bold", "suren"]
my_list_str[1]
my_list_str[:2] #2hurtelh
my_list_str[1:]
my_list_str[::-1]
my_list_str[-1] #hamgin suuliinh

my_list_num = [15,25,2,4.7]
type(my_list_num)