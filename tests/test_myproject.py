from helloworld import main

def test_function1():
    r = main.result
    assert r == "hellow world"

def test_function2():
    r = main.result
    assert r != "Pakistan"

   
   