def balance_status(balance):
    
    if balance < 0:
        print("마이너스 잔액")
    elif balance == 0:
        print("잔액 없음")
    else:
        print("정상 잔액")
    return balance