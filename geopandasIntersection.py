# Find the intersection area between two shapefiles

# Import packages to be used
import geopandas as gpd
import pandas as pd
import time 

# Define a runtime function
def timer(start,end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

# Import shapefile1
shape1_path='/path/shape1.shp'
shape1=gpd.read_file(shape1_path)[['ID', 'DESCRIPTION', 'GEOMETRY']]
shape1.rename(columns={'ID':'ID_shape1'},inplace=True)

# Convert shapefile1 coordinate projection to desired format
shape1new=shape1.to_crs("epsg:####")
shape1new['AREA_shape1_SQM']=shape1new.area

# Import shapefile2
shape2_path='/path/shape2.shp'
shape2=gpd.read_file(shape2_path)[['ID', 'DESCRIPTION', 'GEOMETRY']]
shape2.rename(columns={'ID':'ID_shape2'},inplace=True)

# Convert shapefile2 coordinate projection to desired format
shape2new=shape2.to_crs("epsg:####")
shape2new['AREA_shape2_SQM']=shape2new.area

# Start timer
start = time.time() 

# Find intersection between shape1 and shape2
s1s2_intersection = gpd.overlay(shape1,shape2, how='intersection')
s1s2_intersection['INTERSECT_AREA_SQM']=current_overlay.area
s1s2_intersection['PERCENT_AREA_CONTAINED']= round((s1s2_intersection.area/s1s2_intersection['AREA_SHAPE2_SQM'])*100, 6)
s1s2_intersection.drop(columns=['GEOMETRY'], inplace=True)

# Output results to a csv file
s1s2_intersection.to_csv('/path/shape1_shape2_intersection.csv',encoding='utf-8',index=False)

# End timer
end = time.time()      
print("Total time to process shape1_shape2_intersection:",timer(start,end))