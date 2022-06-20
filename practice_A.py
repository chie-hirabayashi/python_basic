"""
A-1: 文字列のリスト
Bob", "Tom", "Ken" という3つの文字列要素を持つusersというリスト
を定義してください。
"""
from multiprocessing.sharedctypes import Value
from os import sep
from random import random
from tkinter.ttk import Separator


user = ["Bob", "Tom", "Ken"]

# 確認
# print(user)
# print(user[0])


"""
A-2: 整数のリスト
1から5までの整数を要素として持つint_numbersリスト
を定義してください
"""
int_numbers = [1, 2, 3, 4, 5]

# 確認
# number = print(int_numbers[0] + int_numbers[1])
# number = print(int_numbers[0] + int_numbers[4])

# str_numbers = ["1", "2", "3", "4", "5"]
# number = print(str_numbers[0] + str_numbers[1])


"""
A-3: 要素のデータ型が異なるリスト
"Bob", "Dylan", 79 という 3つの要素をもつbob_infoというリスト
を定義してください
"""
bob_list = ["Bob", "Dylan", 79]

# 確認
# print(bob_list)
# print(bob_list[0])
# print(bob_list[0]+" "+bob_list[1])
# print(bob_list[0]+" "+str(bob_list[2]))


"""
A-4: 要素へのアクセス
次のmembersというリストから "Bob" と "Tom" を
取得して出力してください
"""
members = ["Bob", "Tom", "Ken"]

print("<A-4_回答>")

print(members[0])
print(members[1])

print(sep="")


"""
A-5: 要素へのアクセスとフォーマット
次のリストを利用して、"Name: Bob Dylan, Age: 79"と
出力してください
"""
print("<A-5_回答>")

bob_info = ["Bob", "Dylan", 79]

print("Name:" + bob_info[0] + " " + bob_info[1] + "," + "Age:" + str(bob_info[2]))

print(sep="")

"""
A-6: forによるループその1
for を使って odd_numbers の各要素を出力してください
"""
print("<A-6_回答>")

odd_numbers = [1, 3, 5, 7, 9]

for number in range(0, 4):
    print(odd_numbers[number], end=",")
print(odd_numbers[4], sep="")

# 改行なし
# print(end="")
# 改行あり
# print(sep="")
# print("\n")

for number in range(0, 4):
    print(f"{odd_numbers[number]}", end=" ")
print(f"{odd_numbers[4]}", sep=" ")

for number in range(0, len(odd_numbers) - 1):
    print(f"{odd_numbers[number]}", end="/")
print(f"{odd_numbers[len(odd_numbers)-1]}", sep="")

print(sep="")

"""
A-7: forによるループその2
for を使って even_numbers の
それぞれの値を2倍した値を出力してください
"""
print("<A-7_回答>")

even_numbers = [2, 4, 6, 8]
for number in range(0, len(even_numbers)):
    print(f"{even_numbers[number]*2}", end=" ")

print(sep="")
print(sep="")

"""
A-8: リストを要素に持つリスト
users_info を使って次のような出力をしてください
"""
print("<A-8_回答>")
users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]
"""
# ーーー挙動確認ーーー
users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]
print(users_info[0])

# 0のリストを取り出して、0,1の順に取り出す。
user_info = users_info[0]
print(user_info[0] + str(user_info[1]))

# part1作成
for number in range(0, len(users_info)):
    print(f"{users_info[number]}")
# part2作成
for number in range(0, len(user_info)):
    print(f"{user_info[number]}")
# part1,2合体・・・うまくいかない

# 多次元リスト・・・これでいこう
print(users_info[0][0])
print(users_info[0][1])

# 連想配列？
users_info = {"Bob": 79, "Tom": 59, "Ken": 61}
print(users_info["Bob"])
"""

# part1
print("Name:" + users_info[0][0], end=", ")
print("Age:" + str(users_info[0][1]))
print("Name:" + users_info[1][0], end=", ")
print("Age:" + str(users_info[1][1]))
print("Name:" + users_info[2][0], end=", ")
print("Age:" + str(users_info[2][1]))

print(sep="")

# part2・・・あとで
for num1 in range(0, 3):
    for num2 in range(0, 2):
        print(users_info[num1][num2])

print(sep="")

"""
A-9: 辞書
下記のコードが期待通り動作するような辞書を定義してください
print(bob_info["first_name"]) # "Bob"
print(bob_info["family_name"]) # "Dylan"
print(bob_info["age"]) # 79
"""
print("<A-9_回答>")
bob_info = {"first_name": "Bob", "family_name": "Dylan", "age": 79}
print(bob_info["first_name"])
print(bob_info["family_name"])
print(bob_info["age"])

print(sep="")

"""
A-10: サイコロ
下記のコードが期待通り動作するような、
1から6の整数をランダムに出力する dice() 関数を実装してください
print(dice()) # 1から6の整数をランダムに出力する
"""
print("<A-10_回答>")
# print(dice())
saikoro = [1, 2, 3, 4, 5, 6]
import random
result = random.choice(saikoro)
print(f"{result}")
