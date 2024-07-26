# hw_7_2

# a.
trimmed_string = " day-fun ".strip();
print(trimmed_string);
# b.
is_alpha_hello = "hello".isalpha();
print(is_alpha_hello);
# c.
is_digit_777 = "777".isdigit();
print(is_digit_777);
# d.
is_space_only = " ".isspace();
print(is_space_only);
# e.
list_of_chars = ['A', 'J', 'N', 'I', 'N'];
joined_string = ''.join(list_of_chars);
print(joined_string);
# f.
joined_string_with_asterisks = '*'.join(list_of_chars);
print(joined_string_with_asterisks);
# g.
contains_e = 'e' in "hELLo".lower();
print(contains_e);
# h.
user_input: str = str(input("Enter a word: "));
comprehension_list = [char.upper() for char in user_input if char.isalpha()];
print(comprehension_list);
