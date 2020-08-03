import csv
import pygal

#data updated at 1pm
#"CC" refers to Case_Count, HC refers to Hospitalized_Count, DC refers to Death_Count,
#CR refers to Case_Rate, HR refers to Hospitalized_Rate, DR refers to Death_Rate

filename = "coronavirus-data-master/coronavirus-data-master/boro/boroughs-by-age.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #row 1-6 is brooklyn, 7-12 bronx, 13-18 manhattan, 19-25 queens, 26 - 31 SI
    

    bk_case, bk_hospt, bk_death_count, bk_rate, bk_hospitalized, bk_death_rate = [],[],[],[],[],[]


    for row in reader:
        try:
            #bronx
            BX_CC = row[7]
            BX_HC = row[8]
            BX_DC = row[9]
            BX_CR = row[10]
            BX_HR = row[11]
            BX_DR = row[12]
            #brooklyn 
            BK_CASE_COUNT = row[1]
            BK_HOSPITALIZED_COUNT = row[2]
            BK_DEATH_COUNT = row[3]
            BK_CASE_RATE = row[4]
            BK_HOSPITALIZED_RATE = row[5]
            BK_DEATH_RATE = row[6]
            
        except:
            pass
        
        else:
            #brooklyn data
            bk_case.append(int(float(BK_CASE_COUNT)))
            bk_hospt.append(int(float(BK_HOSPITALIZED_COUNT)))
            bk_death_count.append(int(float(BK_DEATH_COUNT)))
            bk_rate.append(int(float(BK_CASE_RATE)))
            bk_hospitalized.append(int(float(BK_HOSPITALIZED_RATE)))
            bk_death_rate.append(int(float(BK_DEATH_RATE)))
            #value 0= "0-17", 1= "18-44", 2="45-64", 3="65-74", 4="75+', 5="boroughwide"
            
#Brooklyn graph        
line_chart = pygal.Bar(title="Brooklyn COVID Data", x_title='Reported Ages')
line_chart.x_labels = '0-17', '18-44', '45-64', "65-74", "75+"
line_chart.add("Case Count", bk_case[:5])
line_chart.add("Hospitalized Count", bk_hospt[:5])
line_chart.add("Death Count", bk_death_count[:5])
line_chart.add("Case Rate", bk_rate[:5])
line_chart.add("Hospitalized Rate", bk_hospitalized[:5])
line_chart.add("Death Rate", bk_death_rate[:5])
line_chart.render_to_file("chart.svg")





