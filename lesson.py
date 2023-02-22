num: int = 1
name: str = ('Mike' * 2) + 'Mike'

# num = name # エラーにはならない(Pythonならでは)

print(num, type(num))
print(name, type(name))

path = r'C:\home\user\src' # 生データ
print(path)
print(r'C:\home\user\src')

print('aaaaaaaaaa'
      'bbbbbbbbbb') # 改行する場合、+ はなくても良い

word: str = f'python'
print(word[0:2])
word = f'j{word[1:]}'
print(word)

s: str = f'My name is Mike. Hi Mike.'
print(s)
is_start: bool = s.startswith('My') # スタートの文字を調べる
print(is_start)
is_start = s.startswith('X')
print(is_start)
print(s.find('Mike')) # 先頭の要素番号を返す
print(s.rfind('Mike')) # 先頭の要素番号を返す
print(s.count('Mike')) # Mikeの数を数える
print(s.capitalize())
print(s.title())
print(s.replace('Mike', 'Nancy'))

n: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1]) # 降順
a: list = ['a', 'b', 'c']
x: list = [a, n]
print(x)

s: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = [] # 特定の要素を空にする
print(s)

n.insert(0, 100) # 先頭に100を追加する
print(n)
n.pop(0) # 先頭を取り出す
print(n)

n = [1, 2, 3, 4, 5, 6, 6, 6]
n.remove(6) # 先頭の6を削除
print(n)
n.remove(6)
n.remove(6)
print(n)
# n.remove(6) # 消せるnがない

a: list = [1, 2, 3, 4, 5, 6]
b: list = [7, 8, 9, 10, 11, 12]
x: list = a + b
print(x)
a += b # 追加する
print(a)
print(x)
x = [1, 2, 3, 4, 5, 6]
y = [7, 8, 9, 10, 11, 12]
x.extend(y) # += と一緒
print(x)

r = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8]
print(r.index(3))
print(r.index(3, r.index(3) + 1)) # 2番目の3の位置を返す

print(r.count(3))

if 15 in r:
      print('exist')

else:
      print('not exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike. Hi Mike.'
to_split: list = s.split(' ')
print(to_split)
print(to_split[0])

x = ' '.join(to_split) # 結合
print(x)
