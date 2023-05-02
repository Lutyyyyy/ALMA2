def get_frequencies_list(size : int) -> list:
    nOccurrences_list = [0] * (size + 1)
    for i in range(2**size):
        bin_str = "{0:010b}".format(i)
        counter = 0
        
        #condition of 3 fair coins next to each other (if found -> increase counter)
        if (bin_str[-1] == bin_str[0] and bin_str[0] == bin_str[1]):
            counter += 1
        if (bin_str[-2] == bin_str[-1] and bin_str[-1] == bin_str[0]):
            counter += 1    
        for j in range(1,size-1):
            if (bin_str[j-1] == bin_str[j] and bin_str[j] == bin_str[j+1]):
                counter += 1

        nOccurrences_list[counter] += 1
    
    for i in range(len(nOccurrences_list)):
        nOccurrences_list[i] /= 2**(size)
    return nOccurrences_list


def compute_mean(lst : list) -> float:
    mean = 0
    for i in range(len(lst)):
        mean += i * lst[i]
    
    return mean


def compute_variance(lst : list) -> float:
    mean = 0
    squared_mean = 0
    for i in range(len(lst)):
        mean += i * lst[i]
        squared_mean += (i**2) * lst[i]

    return (squared_mean - mean**2)


lst = get_frequencies_list(10)

for i in range(len(lst)):
    print("P( N =", i , ") =", lst[i])

print("E(N) =", compute_mean(lst))
print("Var(N) =", compute_variance(lst))
