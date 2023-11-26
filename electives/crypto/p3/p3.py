from random import SystemRandom


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

        k += 1

    return ((-1) ** (k - 1)) * x[k - 1]


def euklid(c, d, m):
    if c >= 0 and d >= 0 and m > 0:
        g = gcd(c, m)
        if (d % g == 0):
            xDach = getXdach(c, m, g)
            return ((d / g) * xDach) % m

    return -1


def gcd(a, b):
    return gcd_run(a, b)


def gcd_run(a, b):
    if a % b == 0:
        return b
    return gcd_run(b, (a % b))


def getWitness(n):
    cryptogen = SystemRandom()
    return cryptogen.randint(1, n - 1)


# calculates m ^ e mod n
def modexp(m, e, n):
    if e == 0:
        return 1
    if e % 2 == 1:
        return m * modexp(m, e - 1, n) % n
    x = modexp(m, e // 2, n)
    p = x * x % n
    if p == 1 and x != 1 and x != n - 1:
        raise
    return p


def isCompositeWitness(a, n):
    try:
        p = modexp(a, n - 1, n)
    except:
        return True
    return p != 1


def isCompositeMillerRabin(n, k):
    if n == 2:
        return False
    for i in range(k):
        a = getWitness(n)
        if isCompositeWitness(a, n):
            return True
    return False


def getNextPrim(n, it):
    while isCompositeMillerRabin(n, it):
        n = n + 1

    return n


def encrypt(m, e, n):
    c = pow(m, e, n)
    return c


def decrypt(c, d, n):
    m = pow(c, d, n)
    return m


# Public Prof
e_prof = 23
n_prof = 80838935643632347602689406251916492097256843104786631171171136456894311297084228755070725430240723776343069111225050752902571341583566366600578313441710584699499981601286903467954723125645821950643557

# Private Student
d_student = 2356507607497722805221704027106554086987709373241893292773350026575281249928942040721938872428135679303223646337601272361039189505827263850754138514432452268282791652291957380023588558378809735459460084348720015149513557
n_student = 4993977088673899617945645970224821274948475280315390584131209195195015050936748731238441935278119391732327211009956455799929205757456300436982211390998471005527202341115944446758821094590475528086362962424793472891006317

print(euklid(17, 1, 1200))

###Key generator:

cryptogen = SystemRandom()

p = getNextPrim(cryptogen.randint(10 ** 98, 10 ** 110), 10)
q = getNextPrim(cryptogen.randint(10 ** 98, 10 ** 110), 10)
f = (p - 1) * (q - 1)
e = cryptogen.randint(10 ** 3, 10 ** 5)

while gcd(e, f) != 1:
    e = cryptogen.randint(10 ** 3, 10 ** 5)

d = euklid(e, 1, f)

print("p=" + str(p))
print("q=" + str(q))
print("f=" + str(f))
print("e=" + str(e))
print("d=" + str(d))
