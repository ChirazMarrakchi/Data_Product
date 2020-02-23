Problems : 

1-Cleanup : files used = cleanup.py , first_edit.csv , DataSample.csv 

Goal : find corrupted requests that have the same geoinfo or timesets 
idea : save geoinfo(long+latitude) as a value in a dictionary 
id as a key 
and determine if value is redudant that is its count is more than 0 

We do similary for timset 

=> if request is not redudant(not corrupt), we save its id in a dictionary : listId
once we have the list of ids corresponding to the right requests ,
 we run through a DataSample file and write the data corresponding to the right requests in a new file : first_edit.csv 
 -------------------------------------------------------------------------------------------------------------------------------------------------
 2- Label : files used : label.py + POI_List.csv + first_edit.csv 
 
 Goal : Finding the closest request to each POI
idea : calculating the distance of each request to POI and select the min value 

steps : POI_values is a dictionary that saves all values of POI's with its geoinfo 
we save our result : closest request to POI in a dictionary :
by appending min_distance_val to POI ids 
-----------------------------------------------------------------------------------------------------------------------------------
3- Analysis : files used: label.py  
1/ for each POI, calculate the average and standard deviation of the distance between the POI to each of its assigned requests.

functions used : Average , stdev
2/ At each POI, draw a circle (with the center at the POI) that includes all of its assigned requests.
 Calculate the radius and density (requests/area) for each POI.
get  a list min_distance = radius for each POI using POI1_lst , POI2_lst , POI3_lst

collect all circles data in a an array CIRCLES=[(posx, posy) , radius]
=> for position, radius in CIRCLES: draw circles using Turtle Library 

--------------------------------------------------------------------------------------------------------

4-
4a. Model files used : label.py + matplotlib and numpy libraries
To visualize the popularity of each POI, they need to be mapped to a scale that ranges from -10 to 10. Please provide a mathematical model to implement this, taking into consideration of extreme cases and outliers.
 Aim to be more sensitive around the average and provide as much visual differentiability as possible.
 
 in this problem, I assumed that poularity is measured in terms of number of requests againt the total number of requests
 
 my steps were : -collecting the total number of requests per POI 
 and -save this mapping to a csv file : POIList.csv + DataVisulatization.py 
 
 in DataVisulatization:  
 - get the values of all POIs + POIs requests in an array 
 - calculate the population of each POI using find_pop() function 
 - Visulize Data using Barchart 
 
 



