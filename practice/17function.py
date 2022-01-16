# def 함수이름():
def open_account():
    print("new account is made")# 호출 전까지는 실행 x

open_account()
#리턴이해
#만약에 밑에 함수들이 return 없이 그냥 프린트 문만 있다면 
#메인 함수에서 balance 금액에는 어떤한 영향도 주지못하는 
#프린트만 할수 있는 함수이다 
# def deposit(balance,money):
#     print("입금이 완료되었습니다 잔액은 {0} 입니다".format(balance+money))
#     return balance+money#총 금액을 반환 리턴을 통해서 반환된 금액을
# def withdraw(balance,money):
#     if balance>= money:
#         print("출금이 완료되었습니다 잔액은 {0} 원 입니다".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다 잔액은 똑같이 {0}입니다".format(balance))
#         return balance
# def withdraw_night(balance,money): # 저녁출금 수수료
#     commission=100
#     return commission,balance-money-commission
# balance=0
# balance= deposit(balance,1000)#이 단계에서 함수로 간다       여기에 발란스에 반환
# # balance= withdraw(balance,2000)
# balance= withdraw(balance,200)
# commission, balance=withdraw_night(balance,500)
# print("수수료는 {0} 원이며 잔액은 {1} 원 입니다".format(commission,balance))

# def deposit(balance,money):
#     print("입금할 금액은 {0}원이며 잔액은 {1} 원 입니다".format(money,balance+money))
#     return balance+money
# def withdraw(balance,money):
#     if balance<money:
#         print("현재 잔액이 출금액보다 작기 때문에 출금할수 없습니다")
#     else:
#         print("출금할 금액은 {0}원이며 잔액은 {1} 원 입니다".format(money,balance-money))
#     return balance-money
# def night_withdraw(commission,balance,money):
#     print("출금 금액은 {0}원이고 수수료는 {1} 원 이고 잔액은 {2}원 입니다".format(money,commission,balance-money-commission))
#     return balance-money-commission

# balance=500
# balance=deposit(balance,1000)
# balance=withdraw(balance,500)
# print(balance)
# balance=night_withdraw(400,balance,300)
# 이게 더 깔끔한데 .