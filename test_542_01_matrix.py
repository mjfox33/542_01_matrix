import code_542_01_matrix as c

def test_example_1():
    s = c.Solution()
    assert s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]

def test_example_2():
    s = c.Solution()
    assert s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]