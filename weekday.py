
#输入一个年份，判断这天是星期几
def sundayk(year,mouth,day):
	a = 0
	for i in range(1990,year):
		
		if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
			a += 366
		else :
			a += 365				

	return a

def sundayj(year,mouth,day):
	b = 0
	h = 0
	if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
		n = 29
	else :
		n = 28
	a = [31,n,31,30,31,30,31,31,30,31,30,31]
	for i in range(1,13):
		if i == mouth :
			for j in range(i-1):
				h += a[j]
	b=day+h
	return b

year,mouth,day = eval(input("请输入日期（年，月，日：）"))
na = sundayk(year,mouth,day)
nb = sundayj(year,mouth,day)
nd = (na+nb)
nf = 0
if nd%7==0:
	nf = str('日')
else :
	nf = nd%7
print("{}年{}月{}日是星期{}".format(year,mouth,day,nf))











