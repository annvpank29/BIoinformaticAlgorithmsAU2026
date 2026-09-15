def reverse_complement(pattern: str) -> str:
    return pattern.translate(str.maketrans("ACGT", "TGCA"))[::-1]