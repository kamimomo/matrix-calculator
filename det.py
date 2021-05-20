class det:
    def func(arr):
        if(len(arr)!=len(arr[0])):
            return 0
        elif(len(arr)==2):
            return (arr[1][1]*arr[2][2])-(arr[1][2]*arr[2][1])
        else:
            res = 0
            for i in range (0, len(arr)):
                temp = 1
                for j in range(0, len(arr[0])):
                    temp *= arr[(i+j)%len(arr[0])][(i+j)%len(arr[0])]
                res += temp