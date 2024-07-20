# Here, I defined the fucnction using the "def" function.
def count_the_number_of_e_in_the_new_national_anthem(new_national_anthem):

# Here, I assinged a variable "count" which takes on a string (the new national anthem),
# converts all the letters to lower cases, for effective counting, and counts the number of "Es".
    count = new_national_anthem.lower().count('e')
    
    # Here, I used 'f' function to include the output statement, and referencing/picking the value of 'count'
    print(f"In the New Nigerian national anthem, the letter 'e' appears {count} times across the whole sentences.")

# Here, I entered the strings 'new national anthem' using the 'Document-String' (""" """), 
# to embed the national anthem carrying multiple lines and puntuations. 
new_national_anthem = """
Nigeria we hail thee
Our own dear native land
Though tribes and tongue may differ
In brotherhood we stand
Nigerians all, are proud to serve
Our sovereign Motherland.
Our flag shall be a symbol
That truth and justice reign
In peace or battle honour'd,
And this we count as gain,
To hand on to our children
A banner without stain.
O God of all creation
Grant this our one request.
Help us to build a nation
Where no man is oppressed
And so with peace and plenty
Nigeria shall be blessed.
"""

# Here, I called Function earlier defined.
count_the_number_of_e_in_the_new_national_anthem(new_national_anthem)
