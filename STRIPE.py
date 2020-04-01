# INPUT FORM = {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}
# BY TANISHQ GUPTA
def tanishq_function(given_dictionary, formed_dictionary, presented_key):
    for key in given_dictionary.keys():
        if type(given_dictionary[key]) == int: formed_dictionary[(presented_key + "." + key).strip(".")] = given_dictionary[key]
        else : formed_dictionary = tanishq_function(given_dictionary[key], formed_dictionary, (presented_key + "." + key).strip('.'))
    return(formed_dictionary)

print(tanishq_function(eval(input()), {}, ""))