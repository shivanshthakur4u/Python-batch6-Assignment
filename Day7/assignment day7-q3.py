
l=[(1,2,3), [1,2], ['a','hit','less']]

  


output = [] 

  

def removeNestings(l): 

    for i in l: 

        if type(i) == list: 

            removeNestings(i) 

        else: 

            output.append(i) 

  


print ('The original list: ', l) 
removeNestings(l) 

print ('The list after removing nesting: ', output) 