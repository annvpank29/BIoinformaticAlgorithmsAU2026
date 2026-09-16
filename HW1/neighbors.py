def hamming_distance(first: str, second: str) -> int:
    return sum(1 for a, b in zip(first, second) if a != b)


def neighbors(pattern: str, d: int) -> set[str]:
    nucleotides = "ACGT"
    result = set()

    def backtrack(index: int, mismatches: int, current: list[str]):
        if mismatches > d:
            return

        if index == len(pattern):
            result.add("".join(current))
            return

        for nt in nucleotides:
            current.append(nt)
            backtrack(index + 1, mismatches + (nt != pattern[index]), current)
            current.pop()

    backtrack(0, 0, [])
    return result