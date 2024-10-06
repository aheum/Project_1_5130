if __name__ == "__main__":
    import random
    import time
    
    
    def bubble_sort(sort_list: list[int]):
        """This function sorts out a list of ints in place using Bubble Sort Format.
        ----------
        Params
        ----------
            sort_list: list[int]
                list of ints
        ----------
        Returns
        ----------
            none:
                sorts list in place
        """
        #increments through list via i
        for i in range(len(sort_list)-1):
            #increments through list j of i
            for j in range(i+1,len(sort_list)):
                #conditional to chheck if position j is less than j-1, then swaps if true
                if sort_list[j] < sort_list[j-1]:
                    #tmp for temp storage for int at value j
                    tmp:int=sort_list[j]
                    sort_list[j]=sort_list[j-i]
                    sort_list[j-i]=tmp


    def insert_sort(sort_list: list[int]):
        """This function sorts out a list of ints in place using Insert Sort Format.
        ----------
        Params
        ----------
            sort_list: list[int]
                list of ints
        ----------
        Returns
        ----------
            none:
                sorts list in place.
        """
        for j in range(2,len(sort_list)):
            key=sort_list[j]
            i=j-1
            while i > 0 and sort_list[i] > key:
                sort_list[i+1]=sort_list[i]
                i=i-1
            sort_list[i+1]=key

    #Constant used for determining the number of times each input is run            
    LIST_NUM: int=10
    #list for containing insert sort times with range 10000xi
    insert_sort_times: list[int]=[]
    #list for containing bubble sort times with range 10000xi
    bubble_sort_times: list[int]=[]

    
    #Loop for bubble_sort_times population
    for j in range(LIST_NUM):
        #Start Time
        start: int=time.perf_counter_ns()
        #generates 10,000 integers between 1 and 1000
        input: list[int] = [random.randrange(1, 1000, 1) for i in range((j+1)*10000)]
        #Calls bubble_sort using input
        bubble_sort(input)
        #Stop Time
        stop: int=time.perf_counter_ns()
        #Appends difference between start and stop times to bubble_sort_times
        bubble_sort_times.append(stop-start)

    #Loop for insert_sort_times population
    for j in range(LIST_NUM):
        #Start Time
        start: int=time.perf_counter_ns()
        #generates 10,000 integers between 1 and 1000
        input: list[int]= [random.randrange(1, 1000, 1) for i in range((j+1)*10000)]
        #Calls insert_sort using input
        insert_sort(input)
        #Stop Time
        stop: int=time.perf_counter_ns()
        #Appends difference between start and stop times to bubble_sort_times
        insert_sort_times.append(stop-start)
    
    print("Insert Sort Times per 10,000", insert_sort_times)
    print("Bubble Sort Times per 10,000", bubble_sort_times)