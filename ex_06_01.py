# Assignment 6.1 using find and split in python string

text = "X-DSPAM-Confidence:    0.8475"

spcpos = text.find(' ')

str_num = text[ spcpos+5 : len(text)]

num = float(str_num)

print(num)