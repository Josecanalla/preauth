def checkNumber(m, n):
    for i, x in enumerate(m):
        startIndex = i+1
        for j, y in enumerate(m[startIndex:], start=startIndex):
            if(x+y == n):
                return [m[i], m[j]]

    return []

resultado = checkNumber([6], 6)
print(resultado)