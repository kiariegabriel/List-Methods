s=input('Enter a string: ')
s=s.lower()
print('a.) ',len(s))
print('b.) ', s*10, end=' ')
print()
print('c.) ', s[0])
print('d.) ', s[:3])
print('e.) ', s[-3:])
print('f.) ', s[-1::-1])
if len(s)>=10:
	print(s[9])
else:
	print('The string is short!!')
s_n=s.replace(s[0],'')
s_n=s.replace(s[-1],'')
print(s_n)
s_c=s.upper()
print(s.upper())
for c in s:
	if c=='a':
		s_r=s.replace(c,'e')
print(s_r)
for c in range(len(s)):
	s_s=s.replace(s[c],'_')
print(s_s)