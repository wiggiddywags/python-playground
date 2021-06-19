
# Udacity Exercise: Write a function to produce the next layer of Pascal's triangle
# Each layer is one larger than the previous layer, and each element in
# the new layer is the sum of the two elements above it in the previous
# layer. For example, `(1, 3, 3, 1) -> (1, 4, 6, 4, 1)`.


# Add a layer/row to Pascal's triangle.
# Each layer should be a tuple.
def add_layer(triangle):
    new_row = list()
    last_row = triangle[-1]
    for a, b in zip(last_row + (0,), (0,) + last_row):
        new_row.append(a + b)
    triangle.append(tuple(new_row))




pascals_triangle = [
    (1,),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers to test.
for _ in range(7):
    add_layer(pascals_triangle)

# Print Triangle
for row in pascals_triangle:
    print(row)
