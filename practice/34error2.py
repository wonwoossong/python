class bignumbererror(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    print("한자리 숫자 전용 계삭ㄴ기 입니다")
    num1 = int(input("첫 번쪠 숫자를 입력하세요:"))
    num2 = int(input("두번쪠 숫자를 입력하세요"))
    if num1 >= 10 or num2>=10:
        raise bignumbererror("입력값 : {0}, {1} ".format(num1,num2)) 
    print("{0}/{1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 일벽하였습니다 한자리 숫자만 입력하세요 ")
except bignumbererror as err:
    print("에러가 발생하였습니다 한자리 숫자만 입력하세요")
    print(err)