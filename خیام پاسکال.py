def generate_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

# تعداد ردیف‌های مثلث خیام پاسکال را مشخص کنید
num_rows = int(input())


pascal_triangle = generate_pascal_triangle(num_rows)
print_pascal_triangle(pascal_triangle)

