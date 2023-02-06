'''
滑动方法
'''

def swipeUp(driver: object, t: object = 500, n: object = 1) -> object:
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.75
    y2 = l['height'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.25
    y2 = l['height'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)