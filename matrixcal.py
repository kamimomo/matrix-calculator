import numpy

mod = int(input("어떤 계산을 수행하시겠습니까? 1.덧셈 2.뺄셈 3.행렬곱 4.행렬식"))
        
if mod == 1:
    n = int(input("행렬의 행의 개수를 입력하시오: "))
    m = int(input("행렬의 열의 개수를 입력하시오: "))
    print("첫번째 행렬을 입력하세요")
    arr1=numpy.mat([list(map(int, input().split())) for _ in range(n)])
    print("두번째 행렬을 입력하세요")
    arr2=numpy.mat([list(map(int, input().split())) for _ in range(n)])
    print("행렬의 합: {0}".format(arr1+arr2))

if mod == 2:
    n = int(input("행렬의 행의 개수를 입력하시오: "))
    m = int(input("행렬의 열의 개수를 입력하시오: "))
    print("첫번째 행렬을 입력하세요")
    arr1=numpy.mat([list(map(int, input().split())) for _ in range(n)])
    print("두번째 행렬을 입력하세요")
    arr2=numpy.mat([list(map(int, input().split())) for _ in range(n)])
    print("행렬의 합: {0}".format(arr1-arr2))

if mod == 3:
    n1 = int(input("행렬의 행의 개수를 입력하시오: "))
    m1 = int(input("행렬의 열의 개수를 입력하시오: "))
    print("첫번째 행렬을 입력하세요")
    arr1=numpy.mat([list(map(int, input().split())) for _ in range(n1)])
    n2 = int(input("두번쩨 행렬의 행의 개수를 입력하시오: "))
    m2 = int(input("두번째 행렬의 열의 개수를 입력하시오: "))
    print("두번째 행렬을 입력하세요")
    arr2=numpy.mat([list(map(int, input().split())) for _ in range(n2)])
    if m1==n2:
        print("행렬곱: {0}".format(numpy.dot(arr1, arr2)))
    else:
        print("계산 불가능!")

if mod==4:
    n = int(input("행렬의 행의 개수를 입력하시오: "))
    m = int(input("행렬의 열의 개수를 입력하시오: "))
    print("행렬을 입력하세요")
    arr=numpy.mat([list(map(int, input().split())) for _ in range(n)])
    print("행렬식의 값은 %d입니다." %numpy.linalg.det(arr))