# String.concat

# string1.concat(str2,str3,...,strX) - add string(s) to end of existing one. Return new string.

def str_cat(str):
	new_str = ""
	for item in str:
		new_str += item
	return new_str
my_str = ['kittens', 'puppies', 'chicks']
print str_cat(my_str)

# string.slice(start,end) - extract part of a string and return in a new one. Start and end are indices into the string, with the first character at index 0. End param is optional and, if present, refers to one beyond the last character to include.

def kitty_string(str, i, n):
	my_kitty = animals[i:n]
	while n >=0:
		return my_kitty
animals = "My favorite animal is a cat."
print kitty_string(animals,2, 5)

def remove_whitespace(str):
	new_str = ""
	for item in str:
		new_str += item
	return ''.join(new_str)
my_str = " \n hello goodbye\t " 
print remove_whitespace(my_str)

# string.split(separator,limit) - split string into array of substrings, returning the new array. Separator specifies where to divide substrings and is not included in any substring. If "" is specified, split string on every character.
def string_split(str):
	my_list = []
	for i in xrange(len(str)):
		if str[i] != ' ':
			my_list.append(str[i])
	return my_list
my_string = "This  is a string "
print string_split(my_string)
print my_string