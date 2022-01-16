jumin="960403-1234567"
#slicing= 필요한 정보만 가져오는거
print("성별 :"+jumin[7])
print("연 :"+jumin[0:2])#[0:2]->0 번째 1 번째 가져오는거 
print("월:"+jumin[2:4])
print("일:"+jumin[4:6])

print("앞자리"+jumin[0:6])

print("앞자리"+jumin[:6])

print(" 뒤 자리 "+jumin[7:14])

print(" 뒤 자리 "+jumin[7:])