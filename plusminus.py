class plusminus :
    def plus(arr1, arr2):
        answer = []
        for i in range(0, len(arr1)):
            temp_row = []
            for j in range(0, len(arr2[0])):
                value = 0
                value += arr1[i][j] + arr2[i][j]
                temp_row.append(value)
            answer.append(temp_row)
        return answer

    def minus(arr1, arr2):
        answer = []
        for i in range(0, len(arr1)):
            temp_row = []
            for j in range(0, len(arr2[0])):
                value = 0
                value += arr1[i][j] - arr2[i][j]
                temp_row.append(value)
            answer.append(temp_row)
        return answer