#Defining a function to get the median of a list
def find_median(data):
    sort_data = sorted(data)
    count = len(sort_data)
    if count % 2 == 0:
        mid_index1 = count//2
        mid_index2 = mid_index1 - 1
        median = (sort_data[mid_index1]+sort_data[mid_index2])/2
    else:
        mid_index = count//2
        median = sort_data[mid_index]
    return round(median, 2)

testdata = [5,8,9,14,4,3]
print(find_median(testdata))
    
