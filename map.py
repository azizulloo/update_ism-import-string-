import string

def update_upper(word):
    result={}
    for i in range(len(string.ascii_lowercase)):
        result[string.ascii_lowercase[i]]=string.ascii_uppercase[i]
    
    for i in range(len(string.ascii_lowercase)):
        result[string.ascii_uppercase[i]]=string.ascii_uppercase[i]
    return result[word]


def update_lower(word):
    result={}
    for i in range(len(string.ascii_lowercase)):
        result[string.ascii_lowercase[i]]=string.ascii_lowercase[i]
    
    for i in range(len(string.ascii_lowercase)):
        result[string.ascii_uppercase[i]]=string.ascii_lowercase[i]
    return result[word]

ismlar=["abdulloh","ubaydulloh","ahRor","sarDor"]

def my_func(word):
    natija=""
    natija+=update_upper(word[0])
    for i in word[1:]:
        natija+=update_lower(i)
    return natija

natija=list(map(my_func,ismlar))
print(natija)