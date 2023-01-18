# receive the input
user_in = input(" put here the phrase: ")

# replace negative space with ...

#print(user_in.replace(" ","..."))


# trying to replace without using replace method

n_str = ""
for i in user_in :
    if i != " " :
        n_str = n_str + i
    else :
        i = "..."
        n_str = n_str + i

print(n_str)