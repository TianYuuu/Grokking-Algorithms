def countdown(i):
    print i
    if i <= 0:
        return
    #这里返回原值，如果返回非负数，会无限循环
    else:
        countdown(i-1) 
