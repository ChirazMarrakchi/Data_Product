'''

A sample dataset of request logs is given in data/DataSample.csv. We consider records that have identical geoinfo and timest as suspicious. 
Please clean up the sample dataset by filtering out those suspicious request records.

'''

'''
1/ we create dictionary 1 
we start by finding if some requests have the same geoinfo 

the idea is we do long+latutide as a string and compare it of another request
long+latitude is value in a dictionary where keys are ids 

2/ we create dictionary 2 

key :id 
value : timeset

3/ to find out if requests have the same geoinfo or timeset 
we find if values have more than one occurance in dictionary if so we remove based on KEY value (id_value)
 --- using this command :  count_occ = (list(dict.values()).count(val ))
 if count_occ > 1  : continue 
 else : get id_value(append in correct id_values) 


write rows / delete rows 

      


'''


dict1 = {}
dict2 = {}
import csv
with open('DataSample.csv', 'r') as inp  :
    
    for row in csv.reader(inp):
        dict1[row[0]] = row[5] + "."+ row[6]
        dict2[row[0]] = row[1]


listId = []
for key, value in dict1.items():
    count_occ = list(dict1.values()).count(value )
    if count_occ > 1 : 
        listId.append(key)
        
        

for key, value in dict2.items():
    count_occ2 = list(dict2.values()).count(value )
    if count_occ2 > 1 : 
        listId.append(key)

        



with open('DataSample.csv', 'r') as inp, open('first_edit.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if not(row[0] in listId):
            
           writer.writerow(row)
        


                     
        
        