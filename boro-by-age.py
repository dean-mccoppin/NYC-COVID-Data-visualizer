import csv
import pygal

#data updated at 1pm
#"CC" refers to Case_Count, HC refers to Hospitalized_Count, DC refers to Death_Count,
#CR refers to Case_Rate, HR refers to Hospitalized_Rate, DR refers to Death_Rate

filename = "coronavirus-data/boro/boroughs-by-age.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #row 1-6 is brooklyn, 7-12 bronx, 13-18 manhattan, 19-25 queens, 26 - 31 SI
    
    #si
    si_case, si_hospt, si_death_count, si_rate, si_hospitalized, si_death_rate = [],[],[],[],[],[]
    #queens 
    qn_case, qn_hospt, qn_death_count, qn_rate, qn_hospitalized, qn_death_rate = [],[],[],[],[],[]
    #mntn
    mntn_case, mntn_hospt, mntn_death_count, mntn_rate, mntn_hospitalized, mntn_death_rate = [],[],[],[],[],[]
    #bx
    bx_case, bx_hospt, bx_death_count, bx_rate, bx_hospitalized, bx_death_rate = [],[],[],[],[],[]
    #bk
    bk_case, bk_hospt, bk_death_count, bk_rate, bk_hospitalized, bk_death_rate = [],[],[],[],[],[]
    

    for row in reader:
        try:
            #Staten Island
            SI_CASE_COUNT = row[25]
            SI_HOSPITALIZED_COUNT = row[26]
            SI_DEATH_COUNT = row[27]
            SI_CASE_RATE = row[28]
            SI_HOSPITALIZED_RATE = row[29]
            SI_DEATH_RATE = row[30]
            #queens
            QN_CASE_COUNT = row[19]
            QN_HOSPITALIZED_COUNT = row[20]
            QN_DEATH_COUNT = row[21]
            QN_CASE_RATE = row[22]
            QN_HOSPITALIZED_RATE = row[23]
            QN_DEATH_RATE = row[24]
            #mntn
            MNTN_CASE_COUNT = row[13]
            MNTN_HOSPITALIZED_COUNT = row[14]
            MNTN_DEATH_COUNT = row[15]
            MNTN_CASE_RATE = row[16]
            MNTN_HOSPITALIZED_RATE = row[17]
            MNTN_DEATH_RATE = row[18]
            #bronx
            BX_CASE_COUNT = row[7]
            BX_HOSPITALIZED_COUNT = row[8]
            BX_DEATH_COUNT = row[9]
            BX_CASE_RATE = row[10]
            BX_HOSPITALIZED_RATE = row[11]
            BX_DEATH_RATE = row[12]
            #brooklyn 
            BK_CASE_COUNT = row[1]
            BK_HOSPITALIZED_COUNT = row[2]
            BK_DEATH_COUNT = row[3]
            BK_CASE_RATE = row[4]
            BK_HOSPITALIZED_RATE = row[5]
            BK_DEATH_RATE = row[6]
            
        except:
            print("Error: row not appendable")
        
        else:
            #SI data
            si_case.append(int(float(SI_CASE_COUNT)))
            si_hospt.append(int(float(SI_HOSPITALIZED_COUNT)))
            si_death_count.append(int(float(SI_DEATH_COUNT)))
            si_rate.append(int(float(SI_CASE_RATE)))
            si_hospitalized.append(int(float(SI_HOSPITALIZED_RATE)))
            si_death_rate.append(int(float(SI_DEATH_RATE)))
            #queens data
            qn_case.append(int(float(QN_CASE_COUNT)))
            qn_hospt.append(int(float(QN_HOSPITALIZED_COUNT)))
            qn_death_count.append(int(float(QN_DEATH_COUNT)))
            qn_rate.append(int(float(QN_CASE_RATE)))
            qn_hospitalized.append(int(float(QN_HOSPITALIZED_RATE)))
            qn_death_rate.append(int(float(QN_DEATH_RATE)))
            #mntn data
            mntn_case.append(int(float(MNTN_CASE_COUNT)))
            mntn_hospt.append(int(float(MNTN_HOSPITALIZED_COUNT)))
            mntn_death_count.append(int(float(MNTN_DEATH_COUNT)))
            mntn_rate.append(int(float(MNTN_CASE_RATE)))
            mntn_hospitalized.append(int(float(MNTN_HOSPITALIZED_RATE)))
            mntn_death_rate.append(int(float(MNTN_DEATH_RATE)))
            #bronx data
            bx_case.append(int(float(BX_CASE_COUNT)))
            bx_hospt.append(int(float(BX_HOSPITALIZED_COUNT)))
            bx_death_count.append(int(float(BX_DEATH_COUNT)))
            bx_rate.append(int(float(BX_CASE_RATE)))
            bx_hospitalized.append(int(float(BX_HOSPITALIZED_RATE)))
            bx_death_rate.append(int(float(BX_DEATH_RATE)))
            #brooklyn data
            bk_case.append(int(float(BK_CASE_COUNT)))
            bk_hospt.append(int(float(BK_HOSPITALIZED_COUNT)))
            bk_death_count.append(int(float(BK_DEATH_COUNT)))
            bk_rate.append(int(float(BK_CASE_RATE)))
            bk_hospitalized.append(int(float(BK_HOSPITALIZED_RATE)))
            bk_death_rate.append(int(float(BK_DEATH_RATE)))
            #value 0= "0-17", 1= "18-44", 2="45-64", 3="65-74", 4="75+', 5="boroughwide
            
            
#Staten Island graph     
line_chart = pygal.Bar(title="Staten Island COVID Data", x_title='Reported Ages')
line_chart.y_labels = 0, 5000, 10000, 15000, 20000, 25000, 30000
line_chart.x_labels = '0-17', '18-44', '45-64', "65-74", "75+"
line_chart.add("Case Count", si_case[:5])
line_chart.add("Hospitalized Count", si_hospt[:5])
line_chart.add("Death Count", si_death_count[:5])
line_chart.add("Case Rate", si_rate[:5])
line_chart.add("Hospitalized Rate", si_hospitalized[:5])
line_chart.add("Death Rate", si_death_rate[:5])
line_chart.render_to_file("si_chart.svg")

#Queens graph     
line_chart = pygal.Bar(title="Queens COVID Data", x_title='Reported Ages')
line_chart.y_labels = 0, 5000, 10000, 15000, 20000, 25000, 30000
line_chart.x_labels = '0-17', '18-44', '45-64', "65-74", "75+"
line_chart.add("Case Count", qn_case[:5])
line_chart.add("Hospitalized Count", qn_hospt[:5])
line_chart.add("Death Count", qn_death_count[:5])
line_chart.add("Case Rate", qn_rate[:5])
line_chart.add("Hospitalized Rate", qn_hospitalized[:5])
line_chart.add("Death Rate", qn_death_rate[:5])
line_chart.render_to_file("queens_chart.svg")

#Manhattan graph     
line_chart = pygal.Bar(title="Manhattan COVID Data", x_title='Reported Ages')
line_chart.y_labels = 0, 5000, 10000, 15000, 20000, 25000, 30000
line_chart.x_labels = '0-17', '18-44', '45-64', "65-74", "75+"
line_chart.add("Case Count", mntn_case[:5])
line_chart.add("Hospitalized Count", mntn_hospt[:5])
line_chart.add("Death Count", mntn_death_count[:5])
line_chart.add("Case Rate", mntn_rate[:5])
line_chart.add("Hospitalized Rate", mntn_hospitalized[:5])
line_chart.add("Death Rate", mntn_death_rate[:5])
line_chart.render_to_file("mntn_chart.svg")

#Bronx graph
line_chart = pygal.Bar(title="Bronx COVID Data", x_title='Reported Ages')
line_chart.y_labels = 0, 5000, 10000, 15000, 20000, 25000, 30000
line_chart.x_labels = '0-17', '18-44', '45-64', "65-74", "75+"
line_chart.add("Case Count", bx_case[:5])
line_chart.add("Hospitalized Count", bx_hospt[:5])
line_chart.add("Death Count", bx_death_count[:5])
line_chart.add("Case Rate", bx_rate[:5])
line_chart.add("Hospitalized Rate", bx_hospitalized[:5])
line_chart.add("Death Rate", bx_death_rate[:5])
line_chart.render_to_file("bx_chart.svg")

#Brooklyn graph        
line_chart = pygal.Bar(title="Brooklyn COVID Data", x_title='Reported Ages')
line_chart.y_labels = 0, 5000, 10000, 15000, 20000, 25000, 30000
line_chart.x_labels = '0-17', '18-44', '45-64', "65-74", "75+"
line_chart.add("Case Count", bk_case[:5])
line_chart.add("Hospitalized Count", bk_hospt[:5])
line_chart.add("Death Count", bk_death_count[:5])
line_chart.add("Case Rate", bk_rate[:5])
line_chart.add("Hospitalized Rate", bk_hospitalized[:5])
line_chart.add("Death Rate", bk_death_rate[:5])
line_chart.render_to_file("bk_chart.svg")




