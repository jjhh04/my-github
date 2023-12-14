#p.73 도전 문제
num = int(input('초 :'))
a = num % 3600
print(num // 3600, '시간', a // 60, '분', num % 60, '초')


#p.74 피타고라스
a = float(input('밑변의 길이 :'))
b = float(input('높이의 길이 :'))
c = (a ** 2 + b ** 2) ** 0.5
print('빗변의 길이 :', c)


#p.77 RFM
a = int(input('여성이면 1, 남성이면 0을 입력 :'))
b = float(input('키 :'))
c = float(input('허리둘레 :'))
d = 64 - (20 * (b / c)) + 12 * a
print('당신의 RFM은 :', d)


#p.78 lab 실습
m = int(input('투입한 돈 :'))
p = int(input('가격 :'))

a = m - p
print('거스름 돈 :', a)

b = a // 500
print('500원 개수 :', b)

a = a % 500

c = a // 100
print('100원 개수 :', c)
