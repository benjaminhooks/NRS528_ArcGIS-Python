import arcpy
class Toolbox(object):
    def __init__(self):
        self.label = "SLR Impacts Python Toolbox"
        self.alias = ""
        self.tools = [buffer, clip, statistics]

class buffer(object):
    def __init__(self):
        self.label = "Buffer Areas"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []

        slr_data = arcpy.Parameter(name="SLR_data",
                                     displayName="Sea Level Rise Data",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")
        # slr_data.value = r"C:\NRS_528\Python Toolbox\RISPP_-_Road_Assets_Exposed_to_Storm_Surge_%26_SLR_by_2100.shp"
        slr_data.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Sea Level Rise Data\RISPP_-_Road_Assets_Exposed_to_Storm_Surge_%26_SLR_by_2100.shp"
        params.append(slr_data)


        buffer_data = arcpy.Parameter(name="RI_Buffer",
                                     displayName="Buffer Data",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Output")
        # buffer_data.value = r"C:\NRS_528\Python Toolbox\Buffer.shp"
        buffer_data.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Buffer.shp"
        params.append(buffer_data)

        return params

    def isLicensed(self):
            return True

    def updateParameters(self, parameters):
            return

    def updateMessages(self, parameters):
            return

    def execute(self, parameters, messages):


        slr_data = parameters[0].valueAsText
        buffer_data = parameters[1].valueAsText


        arcpy.Buffer_analysis(in_features=slr_data,
                              out_feature_class=buffer_data,
                              buffer_distance_or_field="150 Feet",
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        return

class clip(object):
    def __init__(self):
        self.label = "Clip Areas"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []

        buffer_data = arcpy.Parameter(name="RI_Buffer",
                                     displayName="Buffer Data",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")
        # buffer_data.value = r"C:\NRS_528\Python Toolbox\Buffer.shp"
        buffer_data.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Buffer.shp"
        params.append(buffer_data)

        census_data = arcpy.Parameter(name="RI_Census",
                                      displayName="Census Data",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Input")
        # census_data.value = r"C:\NRS_528\Python Toolbox\US_Census_2010%3A_Summary_File_1_Indicators.shp"
        census_data.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Census Data\US_Census_2010%3A_Summary_File_1_Indicators.shp"

        params.append(census_data)

        clipped_census = arcpy.Parameter(name="clipped_census",
                         displayName="Clipped Census Data",
                         datatype="DEFeatureClass",
                         parameterType="Required",
                         direction="Output")
        # clipped_census.value = r"C:\NRS_528\Python Toolbox\Census_clipped.shp"
        clipped_census.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Census_clipped.shp"
        params.append(clipped_census)

        building_data = arcpy.Parameter(name="RI_Buildings",
                                        displayName="Building Data",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input")
        building_data.value = r"C:\NRS_528\Python Toolbox\Building Footprints\d8bb3398-7ceb-4d22-9750-9b31a25a18e02020329-1-17guvsp.9olw.shp"
        # building_data.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Building Footprints\d8bb3398-7ceb-4d22-9750-9b31a25a18e02020329-1-17guvsp.9olw.shp"

        params.append(building_data)

        clipped_buildings = arcpy.Parameter(name="clipped_buildings",
                                            displayName="Clipped Building Data",
                                            datatype="DEFeatureClass",
                                            parameterType="Required",
                                            direction="Output")
        # clipped_buildings.value = r"C:\NRS_528\Python Toolbox\Buildings_clipped.shp"
        clipped_buildings.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Buildings_clipped.shp"
        params.append(clipped_buildings)

        return params

    def isLicensed(self):
            return True

    def updateParameters(self, parameters):
            return

    def updateMessages(self, parameters):
            return

    def execute(self, parameters, messages):

        buffer_data = parameters[0].valueAsText
        census_data = parameters[1].valueAsText
        clipped_census = parameters[2].valueAsText
        building_data = parameters[3].valueAsText
        clipped_buildings = parameters[4].valueAsText

        arcpy.Clip_analysis(in_features=census_data,
                            clip_features=buffer_data,
                            out_feature_class=clipped_census,
                            cluster_tolerance="")



        arcpy.Clip_analysis(in_features=building_data,
                    clip_features=buffer_data,
                    out_feature_class=clipped_buildings,
                    cluster_tolerance="")

        return


class statistics(object):
    def __init__(self):
        self.label = "Calculate Statistics"
        self.description = ""
        self.canRunInBackground = False


    def getParameterInfo(self):
        params = []


        clipped_census = arcpy.Parameter(name="clipped_census",
                         displayName="Clipped Census Data",
                         datatype="DEFeatureClass",
                         parameterType="Required",
                         direction="Output")
        #clipped_census.value = r"C:\NRS_528\Python Toolbox\Census_clipped.shp"
        clipped_census.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Census_clipped.shp"
        params.append(clipped_census)


        clipped_buildings = arcpy.Parameter(name="clipped_buildings",
                         displayName="Clipped Building Data",
                         datatype="DEFeatureClass",
                         parameterType="Required",
                         direction="Output")
        #clipped_buildings.value = r"C:\NRS_528\Python Toolbox\Buildings_clipped.shp"
        clipped_buildings.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Buildings_clipped.shp"
        params.append(clipped_buildings)

        population_output = arcpy.Parameter(name="population_output",
                         displayName="Affected Population Output",
                         datatype="Field",
                         parameterType="Required",
                         direction="Output")
        #population_output.value = r"C:\NRS_528\Python Toolbox\Population.shp"
        population_output.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Population.shp"
        params.append(population_output)

        building_output = arcpy.Parameter(name="building_output",
                         displayName="Affected Buildings Output",
                         datatype="Field",
                         parameterType="Required",
                         direction="Output")
        #building_output.value = r"C:\NRS_528\Python Toolbox\Buildings.shp"
        building_output.value = r"C:\Data\Students_2021\Hooks\Assignments\Python Toolbox\Data\Buildings.shp"
        params.append(building_output)

        return params

    def isLicensed(self):

        return True

    def updateParameters(self, parameters):

        return

    def updateMessages(self, parameters):

        return

    def execute(self, parameters, messages):

        print(parameters)

        clipped_census = parameters[0].valueAsText
        clipped_buildings = parameters[1].valueAsText
        population_output = parameters[2].valueAsText
        building_output = parameters[3].valueAsText


        arcpy.analysis.Statistics(in_table=clipped_census,
                                  out_table=population_output,
                                  statistics_fields=[["POP1", "SUM"]],
                                  case_field=[])


        arcpy.analysis.Statistics(in_table=clipped_buildings,
                                  out_table=building_output,
                                  statistics_fields=[["OBJECTID", "UNIQUE"]],
                                  case_field=[])
        return

# def main():
#     tool = calculatesealevel()
#     tool.execute(tool.getParameterInfo(), None)
# if __name__ == '__main__':
#     main()
