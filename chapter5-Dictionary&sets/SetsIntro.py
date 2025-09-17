
'''
#NOTE : set is a collection of a non repititive elements 

#   ways to make an empty set :
       ❌ wrong way :  s = { } --> this is not an empty set but it is a empty dictionary
       ✅ Correct way : e = s( ). --> this is correct way

    #NOTE : set's don't have order (which means we will get different order of element every time)

    s = {1, 2, 44, 2, 2, 4, 6, 2}

    OUTPUT may be : {44, 1, 6, 4, 2}
       
'''

###############################################################################
#               PROPERTIES OF SETS IN PYTHON :
###############################################################################
'''
1) Elements order doesn't matter.
2) We cannot access elements using indexes in case of sets cuz these are not array , string, etc
3) We cannot change the items of the sets(immutable)
4) Sets cannot contain duplicate values.
'''


###############################################################################
#               Methods OF SETS IN PYTHON :
###############################################################################

'''
1) set.add(element)        => adds a single element into the set
2) Set.remove(element)     => removes the element and shows keyerror if element not found
3) Set.discard(element)    => removes the element and shows no error if element not found 
4) Set.update(olditem, newitem) => this work same as replacement of items 
5) set.clear()             => Removes all elements from the set

'''

###############################################################################
#                SET OPERATIONS IN PYTHON :
###############################################################################

'''
1) set1.union(set2)         => union of two or more sets
2) set1.intersection(set2)  => intersection between two or more sets
3) set1.difference(set2)    => finds difference between two or more sets
4) set1.symmetric_difference(other_set)   => forms a new sets of the elements those are not 
#                                       common 
# NOTE : this can also be performed using (caret) symbol for eg : reslult = s1 ^ s2
5) set1.issubset(set2)      => returns True if set1 is subset of set2
6) set1.issuperset(set2)    => returns True if set1 is super set of set2
7) set1.isdisjoint(set2)    => returns True if no elements are common
'''

###############################################################################
