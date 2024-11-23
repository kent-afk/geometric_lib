from calculate import calc

def test_circle_area():
    fig, func, size = "circle", "area", [10]
    result = calc(fig, func, size)
    assert round(result, 2) == 314.16  

def test_circle_perimeter():
    fig, func, size = "circle", "perimeter", [10]
    result = calc(fig, func, size)
    assert round(result, 2) == 62.83

def test_square_area():
    fig, func, size = "square", "area", [5]
    result = calc(fig, func, size)
    assert result == 25  

def test_square_perimeter():
    fig, func, size = "square", "perimeter", [5]
    result = calc(fig, func, size)
    assert result == 20 