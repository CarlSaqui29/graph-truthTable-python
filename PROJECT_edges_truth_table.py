
vertex_list = [] # where vertex is inserted
empty_status = [] # [0,0] to be inserted in status
status = [] # [[0,0], [0,0]] the status of vertices
storage_list = [] # where updated status is inserted and not to be edited
index_vertex = 0 #index for vertex_list
added_edge = 0 # when and edge is added it will increment

while True:
    print('1. add vertex\n2. add edge\n3. show table')
    accept = input('>> ')

    if accept == '1':
        new_vertex = input('add vertex:' )
        if index_vertex == 0 and added_edge == 0:# the first input of vertex will fall here   
            vertex_list.insert(index_vertex, new_vertex)
            #status = [] # intializing the status to be empty so that the value will be right
            #empty_status = []
            for i in range(len(vertex_list)):# creating a status defending on the len of vertices
                empty_status.insert(i, 0)

            for x in range(len(vertex_list)):
                status.insert(x, empty_status)

        if index_vertex > 0 and added_edge == 0:# if the user just continue to add vertex and never add edges (dealing in status)
            # we will insert a 0 in storage_list beacause the vertex is added
            vertex_list.insert(index_vertex, new_vertex)

            lenn = len(vertex_list)
            new = []# a empty_status for a new inserted vertex
            for x in range(lenn - 1):# inserting 0 to new, - 1 because we will insert the last zero together with the other empty_status
                new.insert(x, 0)

            i = vertex_list.index(new_vertex)# getting the index of a new added vertex so that we can insert the new there at the right index
            status.insert(i, new)

            for i in range(lenn):
                list__ = status[i]
                list__.insert(lenn, 0)

        if index_vertex > 0 and added_edge > 0: # if the user is already add edge (dealing in storage_list)
            # we will insert a 0 in storage_list beacause the vertex is added
            vertex_list.insert(index_vertex, new_vertex)

            lenn = len(vertex_list)
            new = []# a empty_status for a new inserted vertex
            for x in range(lenn - 1):# inserting 0 to new, - 1 because we will insert the last zero together with the other empty_status
                new.insert(x, 0)

            i = vertex_list.index(new_vertex)# getting the index of a new added vertex so that we can insert the new there at the right index
            storage_list.insert(i, new)

            for i in range(lenn):
                list__ = storage_list[i]
                list__.insert(lenn, 0)

            status = [] # clearing the status for updating
            status = storage_list # putting the content of storage_list in status

        index_vertex += 1

    if accept == '2':
        vertex_one = input('enter vertex 1: ')
        vertex_two = input('enter vertex 2: ')

        if added_edge == 0: # because we cannot assign again the last value of status to the storage list
            storage_list = status # [[0,0], [0,0]]

            index_one = vertex_list.index(vertex_one) # getting the index value in vetex_list so that we can modify and access
            index_two = vertex_list.index(vertex_two)

            new_list_one = storage_list[index_one] # putting the empty_status at this variable
            new_list_two = storage_list[index_two]

            len_one = len(new_list_one)
            len_two = len(new_list_one)
            new_list_one = [] # inializing to clear the list for inserting a new zero so that they will become new list
            new_list_two = []

            for i in range(len_one): # creating/inserting a status 0 in the 2 list
                new_list_one.insert(i, 0)

            for x in range(len_two):
                new_list_two.insert(x, 0)

            del new_list_one[index_two]
            new_list_one.insert(index_two, 1)

            del new_list_two[index_one]
            new_list_two.insert(index_one, 1)

            del storage_list[index_one]
            storage_list.insert(index_one, new_list_one)

            del storage_list[index_two]
            storage_list.insert(index_two, new_list_two)
            status = storage_list # passing again the value of storage_list to status so that it can be displayed


        if added_edge > 0: # we will just modify the status in storage_list


            index_one = vertex_list.index(vertex_one) # getting the index value in vetex_list so that we can modify and access
            index_two = vertex_list.index(vertex_two)

            new_list_one = storage_list[index_one] # putting the empty_status at this variable
            new_list_two = storage_list[index_two]

            del new_list_one[index_two]
            new_list_one.insert(index_two, 1)

            del new_list_two[index_one]
            new_list_two.insert(index_one, 1)

            del storage_list[index_one]
            storage_list.insert(index_one, new_list_one)

            del storage_list[index_two]
            storage_list.insert(index_two, new_list_two)

            status = storage_list
            
        added_edge += 1


    if accept == '3':
        length = len(vertex_list)
        print(length)
        indexing = 0
        format = ('{}\t' * length)
        tab = ('\t')
        print(tab + format.format(*vertex_list))
        for i in vertex_list:
            print(vertex_list[indexing] + tab + format.format(*status[indexing]))
            indexing += 1








        



