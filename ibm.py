def findTotalWeight(cans):
    total_weight = 0
    
    while len(cans) > 0:
        # Find the index of the minimum weight can
        min_index = cans.index(min(cans))
        # Add the weight of the lightest can to the total weight
        total_weight += cans[min_index]
        
        # Determine the range to remove (the can and its adjacent cans)
        if min_index == 0:
            # If it's the first can, remove the first two
            del cans[:2]
        elif min_index == len(cans) - 1:
            # If it's the last can, remove the last two
            del cans[-2:]
        else:
            # Otherwise, remove the can and its two adjacent cans
            del cans[min_index-1:min_index+2]
    
    return total_weight

# Sample test
if __name__ == '__main__':
    cans = [132, 45, 65, 765, 345, 243, 75, 67]
    result = findTotalWeight(cans)
    print(result)  # Output should be 68
