import itertools
import random 

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

    
    
def main(base_length, ssr_insert_times): # base_length is the original random sequence's length and ssr_insert_times is how many SSR you want to insert
    # Generate the SSR database in a list
    upto_length = 6 # The length of the SSR's basic units can be upto. The maximum ranged from 6 to 10, depending on different papers 
    
    basic_unit_collection = clean(upto_length)
    
    ssr_collection = unit_repeat(basic_unit_collection)
    ssr_collection.sort()
    
    if len(ssr_collection) - len(list(set(ssr_collection))) != 0: # Your ssr_collection shouldn't have any duplicated SSR
        print('Something is wrong!')
    else: 
        print('Awesome!')
    # Instead of saving the ssr_collection into a file, you can directly use it here
        
        
    # Generate the random sequence
    bp = ['A', 'T', 'G', 'C']
    raw_random_sequence = []
    for i in range(base_length):
        idx = random.randint(0,3)
        raw_random_sequence.append(bp[idx])
    
    random_position = [] # Create a random list of where you want to insert SSR
    for i in range(ssr_insert_times):
        random_int = random.randint(1,base_length-1) # The range of randint() already forces that random_int shouldn't be outside of the raw random sequence
        if random_int in random_position: # I don't want 2 inserted SSR are too close to each other 
            continue
        else: 
            random_position.append(random_int)
    
    random_ssr_index = [] # Create a random list of which SSR you want to insert
    for i in range(ssr_insert_times):
        random_inte = random.randint(1,len(ssr_collection)-1) # The range of randint() already forces that random_int shouldn't be outside of the raw random sequence 
        # A single SSR can be inserted more than once 
        random_ssr_index.append(random_inte)
            
    for position_idx, ssr_index in zip(random_position, random_ssr_index): 
        raw_random_sequence.insert(position_idx, ssr_collection[ssr_index])
    
    print(raw_random_sequence)
        
    with open('C:/Users/louie/Desktop/Simulated DNA.txt', 'w') as output_file:
        output_file.write(''.join(raw_random_sequence))
    print('Finished!')

main(100, 5)
