# In this coding challenge, your objective is to utilize the arcpy.da
# module to undertake some basic partitioning of your dataset. In this
# coding challenge, I want you to work with the Forest Health Works dataset
# from RI GIS (I have provided this as a downloadable ZIP file in this repository).
#
# Using the arcpy.da module (yes, there are other ways and better tools to do this),
# I want you to extract all sites that have a photo of the invasive species (Field:
# PHOTO) into a new Shapefile, and do some basic counts of the dataset. In summary,
# please addressing the following:
#
# Count how many sites have photos, and how many do not (2 numbers), print the results.
#
# Count how many unique species there are in the dataset, print the result.
#
# Generate two shapefiles, one with photos and the other without.

import arcpy
arcpy.env.workspace = r'C:\NRS_528\Assignment9\RI_Forest_Health_Works_Project_Points_All_Invasives'
input_shp = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
fields = ['Species']



line_count_da = 0
line_count_do = 0
with arcpy.da.SearchCursor(input_shp, ['Other']) as cursor:
    for row in cursor:
        if row[0] == 'PHOTO':
            line_count_da += 1
        else:
            line_count_do += 1


print("There are " + str(line_count_da) + " sites that contain photos.")
print("There are " + str(line_count_do) + " sites that do not contain photos.")


species_list = []
with arcpy.da.SearchCursor(input_shp, ['Species']) as cursor:
    for row in cursor:
        species_list.append(row[0])


species_count={}
for i in species_list:
    if i not in species_count.keys():
        species_count[i]=1
    else:
        species_count[i]+=1

print("There are " + str(len(species_count)) + " unique species in this dataset")


# Used "split by attribute" tool which easily splits the dataset into two shapefiles. Only issue not tackled yet is the naming/renaming of the output shape 
# files, for they have very generic 1 letter names. I imagine this is pretty simple to do with os.rename which I may add in soon

in_feature_class = input_shp
target_workspace = arcpy.env.workspace
fields = ['PHOTO']

arcpy.SplitByAttributes_analysis(in_feature_class, target_workspace, fields)
