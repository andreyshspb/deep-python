import numpy as np

from matrix.easy import EasyMatrix
from matrix.medium import MediumMatrix
from matrix.hard import HardMatrix


def easy():
    np.random.seed(0)
    a_mat = EasyMatrix(np.random.randint(0, 10, (10, 10)))
    b_mat = EasyMatrix(np.random.randint(0, 10, (10, 10)))
    with open('artifacts/easy/matrix+.txt', 'w') as file:
        file.write(str(a_mat + b_mat))
    with open('artifacts/easy/matrix*.txt', 'w') as file:
        file.write(str(a_mat * b_mat))
    with open('artifacts/easy/matrix@.txt', 'w') as file:
        file.write(str(a_mat @ b_mat))


def medium():
    np.random.seed(0)
    a_mat = MediumMatrix(np.random.randint(0, 10, (10, 10)))
    b_mat = MediumMatrix(np.random.randint(0, 10, (10, 10)))
    with open('artifacts/medium/matrix+.txt', 'w') as file:
        file.write(str(a_mat + b_mat))
    with open('artifacts/medium/matrix*.txt', 'w') as file:
        file.write(str(a_mat * b_mat))
    with open('artifacts/medium/matrix@.txt', 'w') as file:
        file.write(str(a_mat @ b_mat))


def hard():
    a_mat = HardMatrix([[50, 50], [0, 0]])
    b_mat = HardMatrix([[100, 100], [100, 100]])
    c_mat = HardMatrix([[20, 30], [20, 30]])
    d_mat = HardMatrix([[100, 100], [100, 100]])
    with open('artifacts/hard/A.txt', 'w') as file:
        file.write(str(a_mat))
    with open('artifacts/hard/B.txt', 'w') as file:
        file.write(str(b_mat))
    with open('artifacts/hard/C.txt', 'w') as file:
        file.write(str(c_mat))
    with open('artifacts/hard/D.txt', 'w') as file:
        file.write(str(d_mat))
    ab_mat = a_mat @ b_mat
    HardMatrix.matmul_hashes = {}
    cd_mat = c_mat @ d_mat
    with open('artifacts/hard/AB.txt', 'w') as file:
        file.write(str(ab_mat))
    with open('artifacts/hard/CD.txt', 'w') as file:
        file.write(str(cd_mat))
    with open('artifacts/hard/hash.txt', 'w') as file:
        file.write(f'AB hash: {hash(ab_mat)}\n')
        file.write(f'CD hash: {hash(cd_mat)}\n')


if __name__ == '__main__':
    easy()
    medium()
    hard()
