try:
    print("한자리 숫자 전용 계삭ㄴ기 입니다")
    num1 = int(input("첫 번쪠 숫자를 입력하세요:"))
    num2 = int(input("두번쪠 숫자를 입력하세요"))
    if num1 >= 10 or num2>=10:
        raise ValueError #여기서 의도적으로 에러 발생시켜서  except 부분으로 내려오게 만든다
    print("{0}/{1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 일벽하였습니다 한자리 숫자만 입력하세요 ")