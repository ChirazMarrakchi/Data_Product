'''

Assign each request (from data/DataSample.csv) to the closest (i.e. minimum distance) POI (from data/POIList.csv).

Note: a POI is a geographical Point of Interest.

'''

from math import cos, asin, sqrt
import csv
from turtle import Turtle, Screen


# thsi function computes the dsitance based on latitude and longtitude
def distance(lat1_, lon1_, lat2_, lon2_):
    lat1 = float(lat1_)
    lon1 = float(lon1_)
    lat2 = float(lat2_)
    lon2 = float(lon2_)
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...


'''
--Analysis------------------
For each POI, 
Calculate the average and standard deviation of the distance between the POI to each of its assigned requests.

'''

def Average(lst): 
    return sum(lst) / len(lst)

def stdev(lst) : 
    avg = Average(lst)
    s = 0 
    for v in lst : 
        s = s + (v - avg)**2
    return sqrt(s / len(lst))

#POI_values : gather all POI values
POI_values = {}
with open('POIList.csv', 'r') as inp2  :
    i = 0
    inp2.readline() 
    for row in csv.reader(inp2):
        #skip first row 
        
            
            
        POI_values[i] = [row[1] , row[2]]
        i = i +1


min_distance = {}
average_distance = {}
st_deviations = {}

#get POI values
POI_values = []
with open('POIList.csv', 'r') as inp2  :
    inp2.readline() 

    for row2 in csv.reader(inp2):
        POI_values.append(row2[0])
POI1_lst = []
POI2_lst = []
POI3_lst = []
with open('first_edit.csv', 'r') as inp  :

    '''
    we run a loop over every Request id : id_ and compute the min distance to POI  using distance function 
    distance will be saved in min_distance dictionary'''
    inp.readline() 
    for row in csv.reader(inp):
        #runing a loop to find the min distance over all POI values
        
        with open('POIList.csv', 'r') as inp2  :
            #skip first row 
            inp2.readline() 
            min_distance_cal=[]

            for row2 in csv.reader(inp2):
                min_distance_cal.append(distance(row[5], row[6], row2[1] , row2[2]))
                
            
        
        #get minimum distance in min_distance_cal 
        min_distance[row[0]] = min(min_distance_cal)
        minpos = min_distance_cal.index(min(min_distance_cal)) 
        POI = POI_values[minpos]
        
        #get the index of selected POI 
        if POI == "POI1" :
            POI1_lst.append(min(min_distance_cal))
            
        elif POI == "POI2" : 
            POI2_lst.append(min(min_distance_cal))
        else : 
            POI3_lst.append(min(min_distance_cal))

        #POI_Requests[0].append(min(min_distance_cal))
        



        '''
        Computing Average and Standard Deviation
        '''
        average_distance[row[0]] = Average(min_distance_cal)
        st_deviations[row[0]] = stdev(min_distance_cal)




'''
At each POI, draw a circle (with the center at the POI) that includes all of its assigned requests. 
Calculate the radius and density (requests/area) for each POI

'''





    

CIRCLES = []

with open('POIList.csv', 'r') as inp2  :
    inp2.readline() 

    for row2 in csv.reader(inp2):
        x = float(row2[1])
        y = float(row2[2])
        if row2[0] == "POI1" :
            for i in POI1_lst : 
                CIRCLES.append(((x , y) , float(i)))
        elif row2[0] == "POI2" :
            for i in POI2_lst : 
                CIRCLES.append(((x , y) , float(i)))
        else : 
            for i in POI3_lst :
                CIRCLES.append(((x , y) , float(i))) 




'''
screen = Screen()

turtle = Turtle("turtle")



for position, radius in CIRCLES:
    turtle.penup()
    turtle.setposition(position)
    turtle.pendown()
    #turtle.circle(radius)

turtle.hideturtle()

screen.exitonclick()
'''

'''
To visualize the popularity of each POI, they need to be mapped to a scale that ranges from -10 to 10. 
Please provide a mathematical model to implement this, taking into consideration of extreme cases and outliers. 
Aim to be more sensitive around the average and provide as much visual differentiability as possible.
 
 
 I am writing in a csv file : POI id => #requests
'''
POI_requests = {}
POI_requests["POI1"] = str(len(POI1_lst))
POI_requests["POI2"] = str(len(POI2_lst))
POI_requests["POI3"] = str(len(POI3_lst))

print(POI_requests)


#save POI_values + Total number of requests in a file POI_requets 
#this data will later be used in Visualization 
with  open('POI_requests.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    for key in POI_requests : 
        str_ = key + "," + POI_requests[key] 
        writer.writerow([str_])

