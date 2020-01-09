def fn(kind,*args,**keywords):
    print(len(args))
    for arg in args:
        print("arg " , arg)
    for kw in keywords:
        print(kw,"=",keywords[kw])



fn("aa","aaa",a=23,b=45,c=123)
