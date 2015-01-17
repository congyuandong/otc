import time


def printTime():
	print time.strftime('%H:%M:%S',time.localtime(time.time()))
if __name__ == '__main__':
	
	printTime()