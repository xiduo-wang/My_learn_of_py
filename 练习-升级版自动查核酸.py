def tem(x):
    if x <= 37.5:
        print(f"体温测量中，您的体温是:{x}度，体温正常请进")
    else:
        print(f"体温侧量中，您的体温是:{x}度，需要隔离")
tem(36)