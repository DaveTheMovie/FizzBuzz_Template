


import FizzBuzz

def test_FizzBuzz():
    x = FizzBuzz.FizzBuzz(40,45)
    assert x[0] == "buzz"
    assert x[1] == 41
    assert x[5] == "fizzbuzz"