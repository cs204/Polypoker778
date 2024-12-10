from bank import value

def test_здравствуйте():
    assert value("Здравствуйте, Боооб!") == 0

def test_здрасти():
    assert value("Здрасти, Боооб!") == 20

def test_hello():
    assert value("Hell, Harry!") == 100
