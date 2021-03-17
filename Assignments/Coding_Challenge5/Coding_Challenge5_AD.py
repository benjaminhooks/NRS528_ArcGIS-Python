import arcpy, csv, os

arcpy.env.workspace = r"C:\Data\Students_2021\Hooks\Assignments\Coding_Challenge5"
file_name = "homarus_americanus_gammarus.csv" #Moved the filename out here for simplicity.

arcpy.env.overwriteOutput = True

# Create empty list to capture n species in your file.
species_list = []


# with open(file_name) as species:
#
#     csv_reader = csv.reader(species, delimiter=" ") #I also think your delimiter is likely tab not space
#     next(csv_reader)
#     line_count = 0
#
#     for row in csv_reader:
#         if species not in species_list: #issue is here, species does not exist as a row or item from the file, it is the file!
#             species_list.append(species)
#
#         species_list.append(str(row[9]))
#         line_count = line_count + 1
#
# print(species_list)

# Davies fixed code
with open(file_name, encoding="utf8") as species: #I got a character decode error, it is usually due to latin chars
    csv_reader = csv.reader(species, delimiter="	") #tab not space
    next(csv_reader)

    for row in csv_reader:
        if str(row[9]) not in species_list: #changed the variable speices to row[9]
            species_list.append(str(row[9]))

print(species_list[0])
print(species_list[1])


# Trying to extract the information from the "species" colummn, which is the 10th variable in the list


# os.mkdir("Homarus_Americanus")

#
# for species in species_list:
#     with open(file_name, encoding="utf8") as homarus_americanus:
#         next(homarus_americanus)
#         for row in csv.reader(homarus_americanus):
#             if str(row[0]) not in species:
#                 file = open("Homarus_Americanus/" + species + ".csv", "a")
#                 file.write(",".join(row))
#                 file.write("\n")
#     file.close()


# Davies edits, just small changes needed, you didn't need to hard code lobster names
# not sure what row[0] is for as it is not the speices column in your csv.
# not in species will match none of the species, you need to do an absolute if test
# on the species from species_list against row[9]

#realized that you weren't capturing the header row that would cause issues for csv to shapefile.

for species in species_list:

    print("Extracting: " + str(species) + " from: " + file_name)
    file = open(species + ".csv", "a", encoding="utf-8")
    with open(file_name, encoding="utf8") as species_file:
        first_row = next(species_file).split("\t")
        file.write(", ".join(first_row))
        for row in csv.reader(species_file, delimiter="\t"):
            if str(row[9]) == species:
                file.write(", ".join(row))
                file.write("\n")
    file.close()

# Now do shapefile stuff

for species in species_list:

    #convert species to shjapefile
    species_file_name = species + ".csv"

    #heatmap

    #delete intermetdiate files






 # I feel like I am close! My idea was to change row 50 to str(row[9]) because that is where the species name is in the original file,
# but I got "out of range" error again. I also played around with changing row 46 to include [0] or [1], but that did not seem to work.
# I have gotten the script to output a CSV file, but I cannot figure out a way to output only Homarus Americanus or Gammarus as a CSV
# I am using the code below from a past class as my example, when we output multiple CSV files depending on country name. I feel as though the neccesary code is a 
# slight variation on that, but I have not figured it out yet. 
# Also, I apologize for the inefficient way I am uploading my code for review. For some reason I got GitHub desktop to work once but then it had trouble
# working again. Trying to get it to work again to make this easier!

# for country in country_list:
#     with open("Step_4.csv") as population_csv:
#         next(population_csv)
#         for row in csv.reader(population_csv):
#             if row[0] == country:
#                 file = open("Country Directory/" + country + ".csv", "a")
#                 file.write(",".join(row))
#                 file.write("\n")
#     file.close()






# in_Table = r"homarus_americanus_gammarus.csv"
# x_coords = "decimalLongitude"
# y_coords = "decimalLatitude"
# z_coords = ""
# out_Layer = "homarus_americanus_gammarus"
# saved_Layer = r"homarus_americanus_gammarus.shp"
#
# spRef = arcpy.SpatialReference(4326)
#
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# # print(arcpy.GetCount_management(out_Layer))
#
# arcpy.CopyFeatures_management(lyr, saved_Layer)

#
# desc = arcpy.Describe(r"C:\NRS 528\Assignment5\homarus_americanus_gammarus.shp")
#
# # print(desc.extent)
# # print("Extent:\n  XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
#
#
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
#
#
#
# outFeatureClass = "homarus_americanus_gammarus_fishnet.shp"
# originCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMin)
# yAxisCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMax)
# cellSizeWidth = "5"
# cellSizeHeight = "5"
# numRows = ""
# numColumns = ""
# oppositeCorner = str(desc.extent.XMax) + " " + str(desc.extent.YMax)
# labels = "NO_LABELS"
# templateExtent = "#"
# geometryType = "POLYGON"
#
# arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
#                                cellSizeWidth, cellSizeHeight, numRows, numColumns,
#                                oppositeCorner, labels, templateExtent, geometryType)
#
#
#
# target_features="homarus_americanus_gammarus_fishnet.shp"
# join_features="homarus_americanus_gammarus.shp"
# out_feature_class="homarus_americanus_gammarus_heatmap.shp"
# join_operation="JOIN_ONE_TO_ONE"
# join_type="KEEP_ALL"
# field_mapping=""
# match_option="INTERSECT"
# search_radius=""
# distance_field_name=""
#
# arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
#                            join_operation, join_type, field_mapping, match_option,
#                            search_radius, distance_field_name)
#
#
#
#
# # if arcpy.Exists(out_feature_class):
# #     arcpy.Delete_management(target_features)
# #     arcpy.Delete_management(join_features)
#
# if arcpy.Exists(out_feature_class):
#      print("Created heatmap successfully!")
