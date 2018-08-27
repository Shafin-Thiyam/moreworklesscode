from statistics import  mode

md=[53,50,42,23,54,55]
if len(set(md)) != len(md): # check different lengths, if different we have dups since set only keep unique values
    Most = mode(md)
    print ("The mode is ", Most)
else:      # else both are the  same size so no dups, just print
    print("No duplicates in nums")