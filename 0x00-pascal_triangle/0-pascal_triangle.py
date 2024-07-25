def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # Every row starts with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)

    return triangle

# Example usage:
n = 5
print(pascal_triangle(n))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

