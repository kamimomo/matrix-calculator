import numpy
import plusminus
import cross
import det

mod = int(input("어떤 계산을 수행하시겠습니까? 1.덧셈 2.뺄셈 3.행렬곱 4.행렬식"))
if mod==4:
    n = int(input("행렬의 행의 개수를 입력하시오: "))
    m = int(input("행렬의 열의 개수를 입력하시오: "))
    arr=[[0 for col in range(0, m)]for row in range(0, n)]
    for j in range(0, m):
        for k in range(0, n):
            arr[j][k] = int(input("%d, %d 위치 원소 입력: "%j,k))
    print("행렬식의 값은 %d입니다." %det.func(arr))
        
else:
    if mod == 1 | mod == 2:
        n = int(input("행렬의 행의 개수를 입력하시오: "))
        m = int(input("행렬의 열의 개수를 입력하시오: "))
        arr1=[[0 for col in range(0, m)]for row in range(0, n)]
        arr2=[[0 for col in range(0, m)]for row in range(0, n)]
        for j in range(0, m):
            for k in range(0, n):
                arr1[j][k] = int(input("첫번째 행렬의 %d, %d 위치 원소 입력: " %j,k))
                arr2[j][k] = int(input("첫번째 행렬의 %d, %d 위치 원소 입력: " %j,k))
    else:
        n1 = int(input("행렬의 행의 개수를 입력하시오: "))
        m1 = int(input("행렬의 열의 개수를 입력하시오: "))
        arr1=[[0 for col in range(0, m)]for row in range(0, n)]
        for j in range(0, m1):
            for k in range(0, n1):
                arr1[j][k] = int(input("첫번째 행렬의 %d, %d 위치 원소 입력: " %j,k))
        n2 = int(input("두번쩨 행렬의 행의 개수를 입력하시오: "))
        m2 = int(input("두번째 행렬의 열의 개수를 입력하시오: "))
        arr2=[[0 for col in range(0, m2)]for row in range(0, n2)]
        for j in range(0, m2):
            for k in range(0, n2):
                arr2[j][k] = int(input("첫번째 행렬의 %d, %d 위치 원소 입력: " %j,k))
        if m1==n2:
            print("행렬곱: {0}".format(cross.func(arr1, arr2)))
        else:
            print("계산 불가능!")