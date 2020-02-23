height =input('請輸入你的身高(公尺)')
weight =input('請輸入你的體重(公斤)')
height =float(height)
weight =float(weight)
BMI = weight / height / height
if BMI < 18.5 :
	print('你的BMI值為', BMI, '屬體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('你的BMI值為', BMI, '屬於正常數值')
elif BMI >= 24 and BMI < 27:
	print('你的BMI值為', BMI, '屬於稍重')
elif BMI >= 27 and BMI < 30:	 
	print('你的BMI值為', BMI, '屬於輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI值為', BMI, '屬於中度肥胖')
elif BMI >= 35:
	print('你的BMI值為', BMI, '屬於重度肥胖')