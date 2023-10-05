#محمد ناصر عبدالوهاب
#1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
lar_number = max(lst)
print(f"The largest number in the List : {lar_number} ")

small_number = min(lst)
lst.remove(small_number)
print(f"the smallest number : {small_number}")

lst.sort()
print(f"List = {lst}")

last_4_numb = lst[-4:]
print(f"The last four numbers :  {last_4_numb}", "\n")

#2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
count = 0
for sublist in main_lst:
    if "python" in sublist:
        count += 1
print(count, "\n")

#3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
new_lst = " ".join(my_lst)
new_lst = new_lst.capitalize()
new_lst = new_lst.title()
print(new_lst, "\n")

#4
my_list = [12, 3.8, "GSG", ["sKy", "zak"]]
Copy_list = my_list[:]
print(f"The Copy list :  {Copy_list}", "\n")

#5
my_LIST = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_LIST[2], my_LIST[4] = my_LIST[4], my_LIST[2]
print(my_LIST, "\n")

#6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sum1 = 0
for i in nums:
    sum1 += i
print(f"Sum List = {sum1}", "\n")

#7
tuple_one = (4, 'python', 'GSG', [8, 3, 1])
tuple_tow = 9,
tuple_three = tuple_one + tuple_tow
print(tuple_three, "\n")
#8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
tuple3 = 9,
new_tuple = tuple1 + tuple3 + tuple2
print(new_tuple)