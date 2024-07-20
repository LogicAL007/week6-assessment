National_anthem_1 = "Nigeria, we hail thee, Our own dear native land, Though tribes and tongues may differ In brotherhood we stand, Nigerians all, and proud to serve Our sovereign Motherland."
National_anthem_2 = "Our flag shall be a symbol, That truth and justice reign, In peace or battle honour'd, And this we count as gain, To hand on to our children, A banner without stain"
National_anthem_3 = "O God of all creation,Grant this our one request. Help us to build a nation, Where no man is oppressed, And so with peace and plenty, Nigeria may be blessed."

National_anthem_123 = National_anthem_1 + National_anthem_2 + National_anthem_3
National_anthem = National_anthem_123.lower()
letter_e = National_anthem.count("e")

print("The letter 'e' appears", letter_e, "times in the new national anthem.")

