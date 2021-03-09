import csv


year_list, month_list, value_list = [], [], []

# This makes sense, each [] is a list that gets populated by the previous statements sequentially

with open("co2-ppm-daily.csv") as co2:
    # Still confused by the "with" statement. Is this just designating the csv file as "co2" for shorthand reasons?
    # If you did not have "as co2", would you just have to type of the entire file name every time?
    # Nvm, think i understand now, its importing the csv file and then naming it whatever we want. While also works

    csv_reader = csv.reader(co2, delimiter=",")
    # Based on what comes after deliminter, I assume it has to to with spacing up the data for analysis? Not sure though
    # Can the first csv_reader be named anything we want? Im assuming it can, but it was named cvs_reader to keep it simple
    line_count = 0
    # Is this saying to start at the first line? What would happen to the calculations if this wasnt here?
    # Tried it out, got "'line_count' is not defined" error on line 34, because the first line was never defined?

    next(csv_reader)

    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in year_list:
            year_list.append(year)
        if month not in month_list:
            month_list.append(month)
        # Is this saying "Go down each row, and add the new year/month to the list" created earlier? I think I
        # get it, but the function (row[0].split("-")) still confuses me a bit

        value_list.append(float(row[1]))
        line_count = line_count + 1

print(min(value_list))
print ("Total Minimum = " + str(min(value_list)))
print ("Total Maximum = " + str(max(value_list)))
print ("Total Average = " + str(float(sum(value_list) / int(line_count))))
# print ("Average 2 = " + str(sum(value_list) / len(value_list)))
# What is the Average 2? Not sure what len means. Just two different methods of obtaining the same result

# Getting error "min() arg is an empty sequence", assuming this means the list was not actually populated with values
# Nevermind, fixed this by commenting out print(lines) on 19, not sure why this fixed it though. Is it because printing the lines
# earlier in the code depopulated the list?

year_value_dict = {}

for year in year_list:
    temp_year_list = []
    with open("co2-ppm-daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')

        next(csv_reader)

        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")
            if year_co2 == year:
                temp_year_list.append(float(row[1]))

    year_value_dict[year] = str(sum(temp_year_list) / len(temp_year_list))

print ("Annual averages = " + str(year_value_dict))


spring_season_list = []
summer_season_list = []
autumn_season_list = []
winter_season_list = []
with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')

    next(csv_reader)
    #  Makes sense, same code as above, just different lists. Im assuming it can be written like the first list like year_list, month_list, value_list = [], [], []?

    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")
        if month_co2 == '03' or month_co2 == '04' or month_co2 == '05':
            spring_season_list.append(float(row[1]))
        if month_co2 == '06' or month_co2 == '07' or month_co2 == '08':
            summer_season_list.append(float(row[1]))
        if month_co2 == '09' or month_co2 == '10' or month_co2 == '11':
            autumn_season_list.append(float(row[1]))
        if month_co2 == '12' or month_co2 == '01' or month_co2 == '02':
            winter_season_list.append(float(row[1]))
#         Where did the numbers for each month come from? Were they created when the month_co2 list was created?

print ("Spring average = " + str(sum(spring_season_list) / len(spring_season_list)))
print ("Summer average = " + str(sum(summer_season_list) / len(summer_season_list)))
print ("Autumn average = " + str(sum(autumn_season_list) / len(autumn_season_list)))
print ("Winter average = " + str(sum(winter_season_list) / len(winter_season_list)))

# When I initially saw this, it all looked overwhelming, but what I should have done was focus on making one seasons list work,
# then the rest is the same code with slightly different variables.


average = sum(value_list) / len(value_list)
anomaly = {}

with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    next(csv_reader)


    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")
        anomaly[year_co2] = float(row[1]) - average

print ("Anomaly for years = " + str(anomaly))