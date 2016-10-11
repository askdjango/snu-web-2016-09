for i in range (1,10):
	blank = " "*abs(5-i)
	asteroid = "*"*(2*(5-abs(5-i))-1)  
	print ( {}{}{}.format('blank','asteroid','blank')