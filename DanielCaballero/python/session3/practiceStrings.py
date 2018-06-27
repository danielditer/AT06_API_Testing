def replace(s,old,new):
    words = s.split(old)
    new_string = new.join(words)
    return new_string

print(replace("Mississippi","i","I"))