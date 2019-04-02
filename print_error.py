def printer_error(s):
    arr = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    x = len(s)
    count = 0
    for i in s:
        if i in arr:
            count += 1
    return str(count) + '/' + str(x)