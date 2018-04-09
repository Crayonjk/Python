import datetime
import turtle

def yjkdraw(isdraw):
	turtle.pendown() if isdraw else turtle.penup()
	if isdraw == True:
		turtle.penup()
		turtle.forward(5)
		turtle.pendown()
		turtle.pensize(5)
		turtle.forward(40)
		turtle.penup()
		turtle.forward(5)
	else :
		turtle.forward(50)


	turtle.right(90)


def yjkdraw1(num):
	yjkdraw(True) if num in (2,3,4,5,6,8,9) else yjkdraw(False)
	yjkdraw(True) if num in (0,1,3,4,5,6,7,8,9) else yjkdraw(False)
	yjkdraw(True) if num in (0,2,3,5,6,8,9) else yjkdraw(False)
	yjkdraw(True) if num in (0,2,6,8) else yjkdraw(False)
	
	turtle.left(90)
	yjkdraw(True) if num in (0,4,5,6,8,9) else yjkdraw(False)
	yjkdraw(True) if num in (0,2,3,5,6,7,8,9) else yjkdraw(False)
	yjkdraw(True) if num in (0,1,2,3,4,7,8,9) else yjkdraw(False)
	turtle.left(180)
	turtle.penup()
	turtle.fd(20)
	turtle.pendown()
def mytime(mytimestr):
	for i in mytimestr:
		yjkdraw1(int(i))

if __name__ ==  "__main__":
	turtle.setup(800,600,200,200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	
	s = datetime.date.strftime(datetime.datetime.now(),"%Y%m%d")
	mytime(s)

	turtle.done()

















