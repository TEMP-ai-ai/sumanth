
def fibonacci(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a - b
    return series

# Example usage:
if __name__ == "__main__":
    num_terms = 10
    print(f"Fibonacci series up to {num_terms} terms: {fibonacci(num_terms)}")
