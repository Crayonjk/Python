#if语句练习

day=int(input("请输入："))
weeks = "星期一星期二星期三星期四星期五星期六星期日"
if day==1:
	print("{}".format(weeks[0:3]))
elif day==2:
	print("{}".format(weeks[3:6]))

elif day==3:
	print("{}".format(weeks[6:9]))

elif day==4:
	print("{}".format(weeks[9:12]))

elif day==5:
	print("{}".format(weeks[12:15]))

elif day==6:
	print("{}".format(weeks[15:18]))

else:
	print("{}".format(weeks))

