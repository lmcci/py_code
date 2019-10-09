# 内部if要多一个tab缩进

has_ticket = True
knife_length = 30

if has_ticket:
    if knife_length <= 20:
        print("可以带上车")
    else:
        print("刀长度%d不允许带上车" % knife_length)
else:
    print("不允许进站")
