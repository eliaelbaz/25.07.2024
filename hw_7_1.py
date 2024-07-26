# hw_7_1
full_name_and_city = "Eliya Elbaz Jerusalem";
# a.
length_of_string = len(full_name_and_city);
print(length_of_string);
# b.
upper_case_string = full_name_and_city.upper();
print(upper_case_string);
# c.
lower_case_string = full_name_and_city.lower();
print(lower_case_string);
# d.
starts_with_first_name = full_name_and_city.startswith("Eliya");
print(starts_with_first_name);
# e.
ends_with_city = full_name_and_city.endswith("Jerusalem");
print(ends_with_city);
# f.
split_string = full_name_and_city.split();
print(split_string);
# g.
replaced_string = full_name_and_city.replace(" ", "*");
split_replaced_string = replaced_string.split("*");
print(split_replaced_string);
# h.
centered_string = full_name_and_city.center(50, "=");
print(centered_string);
# i.
substring_from_4 = full_name_and_city[3:];
print(substring_from_4);
# j.
substring_to_4 = full_name_and_city[:4];
print(substring_to_4);
# k.
even_characters = full_name_and_city[1::2];
print(even_characters);
# l.
title_case_string = full_name_and_city.title();
print(title_case_string);
