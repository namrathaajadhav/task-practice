#finding substring
# find
age = "you are eligible to vote."
print(age.find("g"))
print(age.find("z"))
print(age.find("are"))

# rfind
age = ("you are not eligible to vote, your'not under 18")
print(age.rfind("vote"))
print(age.rfind("under"))
print(age.rfind("b"))
print(age[-1])


# index
traffic = "caution! the light is yellow, prepare to stop"
print(traffic.index("l"))
print(traffic.index("c"))
print(traffic.index("yellow"))
print(traffic.index("Yellow"))


# rindex
print(traffic.rfindindex("p"))


#count 
poeam = "rain rain go away"
print(poeam.count("a"))

colours = " red white black blue purple green"
print(colours.count("e"))
print(colours.count("m"))

#replace 
animals = "cat"
print(animals.replace("cat","dog"))

say = "i hate coding"
print(say.replace("hate", "love"))


#split
quote = "every, moment, is, a, fresh, beginning"
q = quote.split(" ")
print(len("quote"))
print(len("q"))

q = quote.split("e")
print(quote)
print(len(quote))


colours = " red", "white", "black", "blue", "purple", "green"
for element in colours:
  print(element)


quote = "every", "moment", "is", "a", "fresh", "beginning"
for element in quote:
 print(element)
 

#changing case 
#uppercae 
poeam = "rain rain go away"
print(poeam.upper())

#lowercase

poeam = "Rain raiN go aWay"
print(poeam.lower())

#swapcase

poeam = "Rain raIn go aWay"
print(poeam.swapcase())

#title


poeam = "Rain raIn go aWay"
print(poeam.title())

#captials

poeam = "Rain raIn go aWay"
print(poeam.capitalize())
 
 #checking case
 #startwith 
song = "I love you mummy"
print(song.startswith("I"))

song = "I love you mummy"
print(song.endswith("mummy"))
