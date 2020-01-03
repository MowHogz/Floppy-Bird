import keyboard
def press(d):
    ok = ['w','s']#original key
    nk = ['u','d']
    for key in range(len(ok)):
        if not nk[key] in d and keyboard.is_pressed(ok[key]):
            d.append(nk[key])
    return d