# print("나누기 전용 계산기 입니다")
# num1= int(input("첫번쪠 숫자를 입력하세요"))
# num2= int(input("두번쪠 숫자를 입력하세요"))
# print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
#근데 만약에 내가 여기서 문자를입력하면 오류가 떠
try: 
    print("나누기 전용 계산기 입니다")
    nums = []
    nums.append(int(input("첫번쪠 숫자를 입력하세요")))
    nums.append(int(input("두번쪠 숫자를 입력하세요")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError: #문자를 넣었을때
    print("에러가 발생했어요")
except ZeroDivisionError as err:#0을 넣었을때
    print(err)
except Exception as err:
    print(err)
except:#위에 두 에러가 아니면 여기에서 발생 
    print("알수 없는 오류 발생")
