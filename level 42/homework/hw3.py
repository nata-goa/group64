
def get_keys_values(d):
    
    keys = d.keys()
    
    values = d.values()
    return keys, values

# მაგალითი:
my_dict = {"a": 1, "b": 2, "c": 3}

keys, values = get_keys_values(my_dict)

print("Keys:", list(keys))     
print("Values:", list(values))
