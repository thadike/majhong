import pyautogui
import time
import operator

# pyautogui.PAUSE = 3.1



# 牌背颜色范围201，124，33 +— 10
def isBackColor(color):
	trueColor = [201,124,33]
	if color[0] < trueColor[0]+10 and color[0] > trueColor[0]-10 and color[1] < trueColor[1]-10 and color[1] > trueColor[1]+10 and color[2] < trueColor[2]+10 and color[2] > trueColor[2]-10:
		return True
	else:
		return False

def genPostionList(lastpoint,card_width,num):
	temp = [[lastpoint[0]-(num-2-i)*card_width,lastpoint[1]] for i in range(num-1)]
	first = [lastpoint[0]-(num-0.5)*card_width,lastpoint[1]]
	result = [first] + temp
	return result

def checkState(resultRecord):
	# print(len(resultRecord))
	if len(resultRecord) < 4:
		return 'waitting'
	if checkOneState(resultRecord[-2]) =='normal' and checkOneState(resultRecord[-1]) =='incard':
		return '已摸牌，准备切'
	elif checkOneState(resultRecord[-2]) =='incard' and checkOneState(resultRecord[-1]) =='normal':
		return '模切中，模切完毕'
	elif checkOneState(resultRecord[-2]) =='incard' and checkOneState(resultRecord[-1]) =='mqie':
		return '模切中'
	elif checkOneState(resultRecord[-2]) =='mqie' and checkOneState(resultRecord[-1]) =='mqie':
		return ''
	elif checkOneState(resultRecord[-2]) =='mqie' and checkOneState(resultRecord[-1]) =='normal':
		return '模切完毕'
	elif checkOneState(resultRecord[-2]) =='incard' and checkOneState(resultRecord[-1]) =='sqie':
		return '手切中'
	elif checkOneState(resultRecord[-2]) =='sqie' and checkOneState(resultRecord[-1]) =='sqie':
		return ''
	elif checkOneState(resultRecord[-2]) =='sqie' and checkOneState(resultRecord[-1]) =='normal':
		return '手切完毕'
	else:
		return ''



def checkOneState(result):
	# normal
	state_normal = [False,True,True,True,True,True,True,True,True,True,True,True,True,True]
	# 进张
	state_incard = [True,True,True,True,True,True,True,True,True,True,True,True,True,True]
	# 出牌状态
	if operator.eq(result,state_normal):
		return 'normal'
	elif operator.eq(result,state_incard):
		return 'incard'
	elif result[0]:
		# 正在出牌，且第一张还在
		return 'sqie'
	elif not result[0]:
		# 正在出牌，且第一张不在
		return 'mqie'

# 主流程
def mainfun():
	resultRecord = [];
	while True:
		result = [False]*len(pointList)
		screenshot_temp = pyautogui.screenshot(region=(0,0, 1920, 100))
		for i in range(len(pointList)) :
			color = screenshot_temp.getpixel((pointList[i][0],pointList[i][1]))
			result[i] = isBackColor(color)
		# print(result)
		resultRecord.append(result);
		printlog = checkState(resultRecord)
		if printlog != '':
			print(printlog)

def test():
	#测试
	# 基本信息
	lastpoint = [1314,50]
	card_width = 47
	trueColor = [201,124,33]
	#


	fullpostionlist = genPostionList(lastpoint,card_width,14)
	print(fullpostionlist)
	# pointList = [[680,50],[756,50],[798,50],[845,50],[893,50],[940,50],[987,50],[1034,50],[1081,50],[1127,50],[1173,50],[1221,50],[1267,50],[1314,50],]


#main
test()
# mainfun()