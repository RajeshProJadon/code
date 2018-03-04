a_stirng = "this is\na sting split\t\tand tabbed"
print(a_stirng)

raw_string = r"this is\na sting split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed bysome text"
print(backslash_string)

backslash_string = "this is a backslash \\followed bysome text"
print(backslash_string)

error_string = r"this string ends with \\"
print(error_string)