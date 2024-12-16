def update_dictionary(d, key, value):
    d[key] = value
    return d
d = {"A": 100, "B": 200}
key = "B"
value = 300
updated_dict = update_dictionary(d, key, value)
print(updated_dict)