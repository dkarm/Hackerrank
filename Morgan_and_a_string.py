
import sys

combined_cases = []

num_case = int(raw_input())

for i in range(0, num_case):
	string1 = raw_input() + 'Z'
	string2 = raw_input() + 'Z'
	
	a_index = 0
	b_index = 0

	combined = ""
	
	while a_index < len(string1) and b_index < len(string2):
		if (string1[a_index] < string2[b_index]):
			cur_index = a_index
			a_index = a_index +1
			while (a_index < len(string1) and string1[cur_index]==string1[a_index]):
				a_index = a_index + 1
			combined = combined + string1[cur_index: a_index]

		elif (string1[a_index] > string2[b_index]):
			cur_index = b_index
			b_index = b_index +1
			while (b_index < len(string2) and string2[cur_index]==string2[b_index]):
				b_index = b_index + 1
			combined = combined + string2[cur_index: b_index]

		elif (string1[a_index] == string2[b_index]):
			if 	string1[a_index:] < string2[b_index:]:
				combined = combined + string1[a_index]
				a_index = a_index+1
			elif 	string1[a_index:] > string2[b_index:]:
				combined = combined + string2[b_index]
				b_index = b_index+1	
			elif string1[a_index:] == string2[b_index:]:
				combined = combined + string1[a_index]
				a_index = a_index+1
	
	if len(combined) < len(string1)+ len(string2):
		if a_index < len(string1):
			combined = combined + string1[a_index:]
		elif b_index < len(string2):
			combined = combined + string2[b_index:]

	combined_cases.append(combined)

for i in combined_cases:
	print i
