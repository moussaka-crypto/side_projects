from random import SystemRandom


def gcd(a, b):
    return gcd_run(a, b, 1)


def gcd_run(a, b, rounds):
    if a % b == 0:
        return b, rounds
    return gcd_run(b, (a % b), rounds + 1)


def sim(anz, n):
    middle = 0
    cryptogen = SystemRandom()

    for a in range(1, anz):
        [a, b] = [cryptogen.randrange(n - 1) for i in range(2)]
        while b == 0 and len(str(a)) < n - 1 and len(str(b)) < n - 1:
            [a, b] = [cryptogen.randrange(n - 1) for i in range(2)]
        [result, rounds] = gcd(a, b)
        middle += rounds

    return middle / anz


def getXdach(a, b, g):
    r = [a, b]
    x = []
    q = [0, 0]
    k = 2

    x.append(1)
    x.append(0)

    while r[k - 1] != g:
        r.append(r[k - 2] % r[k - 1])
        q.append(r[k - 2] // r[k - 1])
        x.append(q[k] * x[k - 1] + x[k - 2])

        # print "Round " + str(k)
        # print "rk=" + str(r[k])
        # print "rk-1=" + str(r[k-1])
        # print "rk-2=" + str(r[k-2])
        # print "qk=" + str(q[k])
        # print "xk=" + str(x[k])
        # print "xk-1=" + str(x[k-1])

        k += 1

    # return x[k-1]
    return ((-1) ** (k - 1)) * x[k - 1]


def euklid(c, d, m):
    if c >= 0 and d >= 0 and m > 0:
        [g, rounds] = gcd(c, m)
        if (d % g == 0):
            xDach = getXdach(c, m, g)
            # print "d=" + str(d) + "   g=" + str(g) +  "   xDach=" + str(xDach)
            return ((d / g) * xDach) % m

    return -1


print("Exercise 1 and 2:")
[result1, rounds1] = gcd(282, 240)
print("gcd(282,240) = " + str(result1) + " in " + str(rounds1) + " rounds.")

[result2, rounds2] = gcd((9 ** 100) + 1, (10 ** 100) + 1)
print("gcd(9^100+1,10^100+1) = " + str(result2) + " in " + str(rounds2) + " rounds.")

print("Exercise 3 and 2:")
print("Simulation with count = 50 and n between 1-199")
fobj_out = open("generated_files/50_sims", "w")
for i in range(1, 200):
    fobj_out.write(str(len((str(100 ** i)))) + "\t" + str(sim(50, 100 ** i)) + "\n")

fobj_out.close()


print("Simulation with count = 100 and n between 1-199")
fobj_out = open("generated_files/100_sims", "w")
for i in range(1, 200):
    fobj_out.write(str((i * 2 + 1)) + "\t" + str(sim(100, 100 ** i)) + "\n")

fobj_out.close()


print("Simulation with count = 200 and n between 1-199")
fobj_out = open("generated_files/200_sims", "w")
for i in range(1, 200):
    fobj_out.write(str((i * 2 + 1)) + "\t" + str(sim(200, 100 ** i)) + "\n")

fobj_out.close()


print("Exercise 5:")
tmp = euklid(25, 13, 61)
print("euklid(25, 13, 61) = " + str(tmp))
print("Sample: 25 * " + str(tmp) + " mod 61 = 13 ?")
print("       " + str((25 * tmp) % 61) + " = 13")

tmp = euklid(86, 13, 61)  # Ergebnis = 42
print("euklid(86, 13, 61) = " + str(tmp))
print("Sample: 86 * " + str(tmp) + " mod 61 = 13 ?")
print("       " + str((86 * tmp) % 61) + " = 13")

tmp = euklid(19, 14, 61)  # Ergebnis = 20
print("euklid(19, 14, 61) = " + str(tmp))
print("Sample: 19 * " + str(tmp) + " mod 61 = 14 ?")
print("       " + str((19 * tmp) % 61) + " = 14")

tmp = euklid(6, 3, 15)  # Ergebnis = 13
print("euklid(6, 3, 15) = " + str(tmp))
print("Sample: 6 * " + str(tmp) + " mod 15 = 3 ?")
print("       " + str((6 * tmp) % 15) + " = 3")

tmp = euklid(6, 3, 18)  # Ergebnis = -1
print("euklid(6, 3, 18) = " + str(tmp))

tmp = euklid(9 ** 100 + 1, 8 ** 100 + 1, 10 ** 100 + 1)
print("euklid(9**100+1, 8**100+1, 10**100+1) = " + str(tmp))
print("Sample : 9**100+1 * " + str(tmp) + " mod 10**100+1 = 8**100+1 ? ")
print("       " + str(((9 ** 100 + 1) * tmp) % (10 ** 100 + 1)))
print("      =" + str(8 ** 100 + 1))


# Exercise 5 und 6
print(euklid(9, 13, 25))

print(euklid(25, 13, 61))
print(euklid(252, 48, 282))
print(euklid(9, 13, 25))
print(euklid(24, 9, 42))

print(gcd(25, 61))
print(gcd(252, 282))
print(gcd(9, 25))
print(gcd(24, 42))
print(gcd(87, 20))

# Exercise 7
for i in range(0, 25):
    print(str(i) + "    " + str(((7 * i) + 7) % 26))
