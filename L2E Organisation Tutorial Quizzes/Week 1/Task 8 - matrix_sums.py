def matrix_sums(matrix):
    rows = []
    cols = []

    if len(matrix) == 0:
        return ([], [])
    
    for items in matrix:
        num = 0
        for n in items:
            num += n
        rows.append(num)

    if len(matrix) == 1:
        for n in matrix[0]:
            cols.append(n)
        return rows, cols
    else:
        cols = [0] * len(matrix[0])

        for i in range(len(cols)):
            for j in range(len(matrix)):
                cols[i] += matrix[j][i]
                continue

        return rows, cols