import pprint
# For this problem, we can use lists and dictionaries in python
# These are mutable data structures, which mean they can be modified
# without creating a whole new copy of the entire data
# We can say that our data is a list of boxes, and each box has a
# status of either opened or closed.  We will programmatically apply
# the following steps to set the final status of every box
#
# Step 1: For each box in series, open every box (or simply, start
# 			with every box open in our program)
# 
# Step 2: Starting with the 2nd box, open every 2nd box
#
# Step 3: Starting with the 3rd box, change every 3rd box's status to 
# 			be the opposite of what it currently is
#
# Step 4: Starting with the 4th box, change each 4th box's status to 
# 			be the opposite of what it currently is
#
# Step 5: Finaly, starting with the 5th box, change every 5th box's 
#			status to be the opposite of what it currently is

# how many boxes total
num_boxes = 50 # for 50 boxes
#num_boxes = 200 # for 200 boxes


# open up all the boxes
# in python we create a list of key value pairs
# where the key is just the number of the box
# and the value is the status of the box, (either
# opened or closed), but here we initialize it to
# opened for every box.  We name this 'data'
data = [ { i+1: "opened" } for i in range(num_boxes) ]


def step2():
	# in step 2, we start with box #2 and close it, along
	# with every 2nd box after that (2,4,6,8,..,50)
    index = [] # we create an empty list to hold the number of the box

    for item in data[1::2]: # data[1::2] is a way where we can 'slice' 
    			    # a python list starting with list index 1 
    			    # (counting from 0) which would be box 2
    			    # (the index number + 1, since we count from 1)
    			    # taking every 2nd element after the index

        index.append(item.keys()[0]) # we add to our 'index' list every 
        			     # key from our sliced list so we can 
        			     # iterate on them

    for i in index: # we use a for loop to step through each box in the 
    		    # 'index' list 

        data[i-1] = { i: "closed" } # and we set each of those boxes to
        			    # closed 

    return data # return our results

def step3():
	# in step 3, we do the same thing as step 2, except we first check the
	# box status to see if its opened or closed, then we close it if its open
	# and open it if its closed
    index = []

    for item in data[2::3]: # this time we slice the array starting at box 3, 
    			    # or index 2, and stepping through by 3

        index.append(item.keys()[0])
    for i in index:
        thisvalue = data[i-1].values()[0]
        data[i-1] = { i: swapvalues(thisvalue) } # instead of just setting the
        					 # box to closed like in step 2,
        					 # we check if the box is opened
        					 # or closed and change it
    return data # return our results

def step4():
	# rinse and repeat the logic for step3, but change the slice
    index = []
    for item in data[3::4]: # this time we slice the array starting at box 4,
    			    # or index 3, and stepping through by 4

        index.append(item.keys()[0])
    for i in index:
        thisvalue = data[i-1].values()[0]
        data[i-1] = { i: swapvalues(thisvalue) } 
    return data

def step5():
	# rinse and repeat the logic for step3, but change the slice
    index = []
    for item in data[4::5]: # this time we slice the array starting at box 4,
    			    # or index 3, and stepping through by 4

        index.append(item.keys()[0])
    for i in index:
        thisvalue = data[i-1].values()[0]
        data[i-1] = { i: swapvalues(thisvalue) } 
    return data


def swapvalues(boxstatus):
	# This function changes a box from closed to opened and vice versa
    if boxstatus == "closed":
        newboxstatus = "opened"
    elif boxstatus == "opened":
        newboxstatus = "closed"
    return newboxstatus


step2()
step3()
step4()
step5()
pprint.pprint(data)

            


