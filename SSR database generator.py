import itertools

def unit_generator(length): # Generate a list of all the combinations of the given length
    bp = ['A', 'T', 'G', 'C']
    unit_collection = itertools.product(bp, repeat = length)
    
    unit_list = []
    for unit in unit_collection:
        unit_list.append(''.join(list(unit)))
    return unit_list

def check_multiplication_2_str(short_string, long_string): # Check whether long_string is a multiplication of short_string. Return True if it is and False if it isn't
    try: 
        if long_string == short_string: 
            return True 
        else: 
            if long_string [:len(short_string)] == short_string: 
                return check_multiplication_2_str(short_string, long_string[len(short_string):])
            else: 
                return False
    except: 
        return False
    
def check_multiplication_2_list(short_list, long_list): # Remove any long_item in long_list that is a multiplication of any short_item in the short_list and return the cleaned long_list
    for long_item in long_list: 
        for short_item in short_list: 
            if check_multiplication_2_str(short_item, long_item) == True: 
                long_list.remove(long_item)
    
    return long_list

def clean(upto_length): # After removing the duplications, make a list of all the passible units
    mother = []
    for number in range(1, upto_length+1):
        mother += check_multiplication_2_list(mother, unit_generator(number))
    return mother

def unit_repeat(unit_list): # Generate a list of all repeated possibilities from the unit sequence 
    sequence_list = []
    for unit in unit_list: 
        
        child_list = []
        for i in range (5, 51): # SSR repeat 5-50 times 
            sequence = unit*i
            child_list.append(sequence) 
        sequence_list += child_list
    return sequence_list
    
    
    
def main():
    upto_length = 6 # The length of the SSR's basic units can be upto. The maximum ranged from 6 to 10, depending on different papers 
    
    basic_unit_collection = clean(upto_length)
    print(basic_unit_collection)
    
    ssr_collection = unit_repeat(basic_unit_collection)
    ssr_collection.sort()
    
    if len(ssr_collection) - len(list(set(ssr_collection))) != 0: # Your ssr_collection shouldn't have any duplicated SSR
        print('Something is wrong!')
    else: 
        with open('C:/Users/louie/Desktop/SSR Database.txt', 'w') as output_file:
            for ssr in ssr_collection:
                output_file.write(ssr+'\n')
        print('Finished!')

main()
