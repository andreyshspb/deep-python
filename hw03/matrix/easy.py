class EasyMatrix:
    def __init__(self, data):
        self.data = data
        for row in self.data:
            if len(row) != self.columns():
                raise Exception('Incorrect dimensions')

    def rows(self):
        return len(self.data)

    def columns(self):
        assert len(self.data) != 0
        return len(self.data[0])

    def __add__(self, other):
        if self.rows() != other.rows() or self.columns() != other.columns():
            raise Exception('Incompatible dimensions of matrices')
        data = [list(map(sum, zip(*rows))) for rows in zip(self.data, other.data)]
        return EasyMatrix(data)

    def __mul__(self, other):
        if self.rows() != other.rows() or self.columns() != other.columns():
            raise Exception('Incompatible dimensions of matrices')
        data = [[a * b for a, b in zip(*rows)] for rows in zip(self.data, other.data)]
        return EasyMatrix(data)

    def __matmul__(self, other):
        if self.columns() != other.rows():
            raise Exception('Incompatible dimensions of matrices')
        data = [[sum(a * b for a, b in zip(A_row, B_col))
                 for B_col in zip(*other.data)]
                for A_row in self.data]
        return EasyMatrix(data)

    def __str__(self):
        return str(self.data).replace('], ', ']\n ')
