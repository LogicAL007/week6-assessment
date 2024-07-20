# The letter e is said to be the most frequent letter in the English
# language. Count and print how many times this letter appears in the
# new national anthem.

# Print the e
count = 0
National_anthem = """Nigeria we hail thee Our own dear native land Though tribes and tongue may differ
In brotherhood we stand Nigerians all, are proud to serveOur sovereign Motherland.
Our flag shall be a symbol That truth and justice reign In peace or battle honour'd,
And this we count as gain, To hand on to our children A banner without stain.
O God of all creation Grant this our one request. Help us to build a nation 
Where no man is oppressed And so with peace and plenty Nigeria shall be blessed."""

for i in National_anthem:
  if i == "e":
    count += 1
print(National_anthem.count("e"))



