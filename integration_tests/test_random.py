from ltypes import i32, f64
import random


def test_random():
    r: f64
    r = random.random()
    print(r)
    assert r >= 0.0 and r < 1.0
    r = random.random()
    print(r)
    assert r >= 0.0 and r < 1.0

def test_randrange():
    r: i32
    r = random.randrange(0, 10) # [0, 10)
    print(r)
    assert r >= 0 and r < 10
    r = random.randrange(-50, 76) # [-50, 76)
    print(r)
    assert r >= -50 and r < 76

def test_randint():
    ri1: i32
    ri2: i32
    ri1 = random.randint(0, 10) # [0, 10]
    print(ri1)
    assert ri1 >= 0 and ri1 <= 10
    ri2 = random.randint(-50, 76) # [-50, 76]
    print(ri2)
    assert ri2 >= -50 and ri2 <= 76

def test_paretovariate():
    r: f64
    r = random.paretovariate(2.0)
    print(r)
    r = random.paretovariate(-5.6)
    print(r)

test_random()
test_randrange()
test_randint()
test_paretovariate()
