from matrix.easy import EasyMatrix


class HardMatrix(EasyMatrix):
    matmul_hashes = {}

    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key in self.matmul_hashes:
            return self.matmul_hashes[key]
        result = super().__matmul__(other)
        self.matmul_hashes[key] = result
        return HardMatrix(result.data)

    def __hash__(self):
        return sum([sum(row) for row in self.data])
