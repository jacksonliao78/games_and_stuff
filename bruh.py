from random import randint
import time
import matplotlib.pyplot as plt

def solve(A, b):
    A = [[float(thing) for thing in A[i]] for i in range(len(A))]
    b = [float(x) for x in b]

    for i in range(len(A)):
        pivot = A[i][i]
        if pivot == 0:
            pivot += 1 #sorry i just didn't want to deal with 0s
        A[i] = [ x / pivot for x in A[i] ]
        b[i] /= pivot

        

        for j in range( i + 1, len(A)):
            num = A[j][i]
            A[j] = [A[j][k] - num * A[i][k] for k in range(len(A))]
            b[j] -= num * b[i]

    sol = [0] * len(A)

    for i in range(len(A) - 1, -1, -1):
        sol[i] = b[i] - sum(A[i][j] * sol[j] for j in range(i + 1, len(A)))

    return sol

def gen_matrix( N ):
    b = [randint(-10, 10) for _ in range(N)]
    A = [ [randint(-10, 10) for _ in range(N)] for _ in range(N)]

    return A, b

#gen_matrix( 10 )


test = [[1, 2, 3], [2, -3, -5], [-6, -8, 1]]
b = [-7, 9, -22]

print(solve(test, b))

sizes = [1, 5, 20, 100, 500, 1000]

times = []

for size in sizes:
    A, b = gen_matrix( size )
    start_time = time.time() 
    solve(A, b)
    times.append(time.time() - start_time)




plt.plot(sizes, times, marker='o')
plt.xlabel('size (N)')
plt.ylabel('seconds')
plt.title('size vs time: Gaussian Elimination')
plt.grid(True)
plt.show()

print(f"{'N':<20} {'seconds'}")
print("-" * 40)
for N, time_taken in zip(sizes, times):
    print(f"{N:<20} {time_taken:.6f}")