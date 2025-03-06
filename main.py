

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]


# Level 1

#One more thing, I refrence this code a lot when working with arrays
#Code: https://codehs.com/sandbox/id/genz-demo-emMcfZ
#First time I learned how to work with them and have been a big help since then

'''
For the Level 1 solution, I believe we must use an if function to tell whether tables are free or not. It can start with something like
"if tables == "o":
        So on so on

It will definatly use a return funtion in order to return all the free tables and list them for the user.
'''



def free_tables(restaurant_tables2,timeslot):

    seating_row = restaurant_tables2[timeslot]

    #I saw that the headers were mentioned and those are the table names so here is a function to get names
    #Note: Arrays count by whole numbers (All natural numbers + 0)
    header = restaurant_tables2[0]


if open:
        print("Tables available:", free)
else:
        print("No free tables at this time.")


free_tables()




# Level 2

'''
I'm not exactly sure how to implement my thoughts into codes but I believe that for this we will have to use 
Comparison operaters to show table capacity. It will need input for user so it can show the user what exactly 
how maybe people they will be sitting

if seatings == capacity
    print("Table -- can seat you!")

Something along those lines

'''

# Level 3

'''

Now this one will be similar to the first function, I was thinking the function above could be used along side the top function
because it already tells us the tables with the the ability to hold the amouont of guests.

if tables == ["o"] && amount <---this is what I'll call the function above:
    print("Table --- is avalible for you!)

'''

# Level 4

'''

This is the longest of the four, but I believe that you can use the two function above in the same function.
If I really think about it, it only needs the second since the second has it's own and the top one. 
It could be written somewhat like:

if size (<-- fucntion above) and tables and tables = ["o"]
    print("Table --- and --- can be joined to fit your group!")
    
I know this looks a bit jumbled but something like this is my thought process at the moment.

'''