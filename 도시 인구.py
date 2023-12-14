city = []
city_pop = []

s = 0
print('입력 유지 키 = 1, 입력 종료 키 = 2')
while s < 2:
    s = 0
    a = input('도시 이름 :')
    if a in city:
        pop = int(input('인구 :'))
        i = city.index(a)
        city_pop.append[i] = pop
    else:
        city.append(a)
        pop = int(input('인구 :'))
        city_pop.append(pop)
    s1 = int(input('종료 또는 유지 :'))
    s = s + s1
    


city_pop.sort(reverse=True)
print('최댓값 :', city_pop[:1])

city_pop.sort()
print('최솟값 :', city_pop[:1])

pop_sum = 0
n = 0
for p in city_pop:
    pop_sum += p
    n += 1

print('평균값 :', pop_sum / n)
