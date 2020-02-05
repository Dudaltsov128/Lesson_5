from divisor_master import*

def test_prime_check1():
    assert prime_check(2) == True

def test_prime_check2():
    assert prime_check(4) == False

def test_divisor_master():
    assert divisor_master(10) == [2, 5]

def test_divisor_max():
    assert divisor_max(10) == 5

def test_divisor_list_full():
    assert divisor_list_full(12) == [1, 2, 3, 4, 6]