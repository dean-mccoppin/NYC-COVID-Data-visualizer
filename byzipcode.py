# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:02:23 2020

@author: truet
"""
import csv
import pygal

#data sorted by zipcodes

filename = "coronavirus-data/data-by-modzcta.csv"

userzip = str(input("Enter zipcode to retrieve COVID data on: "))
userdata = None

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    zipcode, block_name, borough, case_count, case_rate, pop_demonator, death_count, death_rate, pct_pos, total_tests = [],[],[],[],[],[],[],[],[],[] 
    
    for row in reader:
        zipcode1 = row[0]
        block_name1 = row[1]
        borough1 = row[2]
        case_count1 = row[3]
        case_rate1 = row[4]
        pop_demonator1 = row[5]
        death_count1 = row[6]
        death_rate1 = row[7]
        pct_pos1 = row[8]
        total_tests1 = row[9]
        
        zipcode.append(str(zipcode1))
        block_name.append(str(block_name1))
        borough.append(str(borough1))
        case_count.append(int(float(case_count1)))
        case_rate.append(int(float(case_rate1)))
        pop_demonator.append(int(float(pop_demonator1)))
        death_count.append(int(float(death_count1)))
        death_rate.append(int(float(death_rate1)))
        pct_pos.append(int(float(pct_pos1)))
        total_tests.append(int(float(total_tests1)))

#retrieve user info
for zipc in enumerate(zipcode):
    if userzip == zipc[1]:
        userdata = zipc[0]

#zipcode graph        
line_chart = pygal.Bar(title="%s COVID Data" % block_name[userdata])
line_chart.add("Case Count", case_count[userdata])
line_chart.add("Case Rate", case_rate[userdata])
line_chart.add("Death Count", death_count[userdata])
line_chart.add("Death Rate", death_rate[userdata])
line_chart.add("Percent Tested Positive", pct_pos[userdata])
line_chart.add("Total Tests", total_tests[userdata])
line_chart.render_to_file("%s.svg" % zipcode[userdata])

