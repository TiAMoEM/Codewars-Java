def land_perimeter(arr):
    """
    Codewars练习题: Land perimeter
    :param arr:
    :return:
    """

    # 方法一
    p = 0
    for i in range(len(arr)):                # up and bottom
        if arr[i][0]  == 'X': p += 1
        if arr[i][-1] == 'X': p += 1
    for i in range(len(arr[0])):             # left and right
        if arr[0][i]  == 'X': p += 1
        if arr[-1][i] == 'X': p += 1
    for y in range(len(arr)):                # inside
        for x in range(len(arr[0])):
            if arr[y][x] == 'O':
                if y + 1 < len(arr   )  and arr[y+1][x] == 'X': p += 1
                if x + 1 < len(arr[0])  and arr[y][x+1] == 'X': p += 1
                if 0 <= y - 1 and arr[y-1][x] == 'X': p += 1
                if 0 <= x - 1 and arr[y][x-1] == 'X': p += 1
    # return 'Total land perimeter: {}'.format(p)

    # 方法二
    s, m = len(grid), len(grid[0])
    ans = 0
    for x in range(s):
        for y in range(m):
            if grid[x][y] == 'X':
                ans += 4
                if x < s - 1 and grid[x + 1][y] == 'X':
                    ans -= 2
                if y < m - 1 and grid[x][y + 1] == 'X':
                    ans -= 2

    return ('Total land perimeter: {}'.format(ans))