# largest name find an array

def find_longest_string(strings):
    longest = ""
    for string in strings:
        if(len(string) > len(longest)):
            longest = string
    return longest


print("find largest string an array:",find_longest_string(["Tanvir","Shakib","jamal","Tanvir Hossain","kamal uddin"]))