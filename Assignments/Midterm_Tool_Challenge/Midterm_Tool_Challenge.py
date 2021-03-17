#
# In this assignment, you are instructed to produce a small script tool that takes
# advantage of arcpy and Python. You will need to provide example data, and the code
# should run on all PC's. The tool needs to manipulate a dataset across three different
# processes, for example, extracting, modifying and exporting data. The exact workflow
# is entirely up to yourself. You are expected to take 3-4 hours on this coding assignment,
# and you should deposit your code and example files within a Github repository for feedback and grading.
#
# The criteria are:
#
# Cleanliness of code (10 points)
# Functionality (10 points)
# Appropriate use of documentation (10 points)
# Depth of processing operation (10 points)
# In addition, you must provide example data and minimize the amount
# of editing a user must make in order for the program to run (10 points).

# Notes

# Import dataset from RIGIS or another data file website
# Use a set a sequential tools to work with the data
# Idea - Import soil CSV data from RIGIS, extract all soils in charlstown/RI area, buffer the selected soils to
# create an area that will likely contain the extracted soil



import arcpy, csv

arcpy.env.workspace = r"C:\NRS_528\Midterm_Tool_Challenge"
file_name = r"C:\NRS_528\Midterm_Tool_Challenge\CSV\Soils_Special_Point_Features.csv"

arcpy.env.overwriteOutput = True

soils_list = []

with open(file_name) as soil:
    csv_reader = csv.reader(soil, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        if str(row[9]) not in soils_list:
            soils_list.append(str(row[9]))

for soil in soils_list:

    print("Extracting " + str(soil) + "from:" + file_name)
    file = open(soil + ".csv", "a")
    with open(file_name) as soil_file:
        first_row = next(soil_file).split(",")
        file.write(",".join(first_row))
        for row in csv.reader(soil_file, delimiter=","):
            if str(row[9]) == soil:
                file.write(",".join(row))
                file.write("\n")

    file.close()
    
# Everything up to here works, and I get a .csv output for each soil type. 


# Everything after here has me confused. I am trying to use a for loop to cycle through each created csv file and output a shapefile for each. I've played around
# with it for a few hours so far, and I did some googling (most promising was from https://community.esri.com/t5/geoprocessing-questions/using-python-to-execute-make-x-y-layer-event-across-all-files/m-p/202932 
# where it looked like someone was trying to do the same thing. Since this is the midterm, I certainly dont want to ask for an outright answer. Any small hint would be appreciated,
# especially if I'm thinking about it incorrectly! Might try to perform other functions with the data in the meantime so I dont get stuck here. 


csvlist = arcpy.ListFiles("*.csv")

print(csvlist)
for csvfile in csvlist:
    # print(csvfile)
    in_Table = csvfile
    x_coords = "X"
    y_coords = "Y"
    z_coords = ""
    out_Layer = soil + str("layer")
    saved_Layer = soil + str(".shp")

    spRef = arcpy.SpatialReference(4326)

    layer = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)


    arcpy.CopyFeatures_management(layer, saved_Layer)

# file.close()

        # desc = arcpy.Describe(r"C:\NRS_528\Midterm_Tool_Challenge\Shapefiles)
