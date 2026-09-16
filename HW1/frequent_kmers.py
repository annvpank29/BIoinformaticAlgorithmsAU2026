from neighbors import neighbors
from reverse_complement import reverse_complement


def frequent_words_with_mismatches_and_reverse_complements(
    text: str,
    k: int,
    d: int
) -> set[str]:
    freq = {}

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        for neighbor in neighbors(kmer, d):
            freq[neighbor] = freq.get(neighbor, 0) + 1

    candidates = set(freq.keys())
    for pattern in list(freq.keys()):
        candidates.add(reverse_complement(pattern))

    max_score = -1
    result = set()

    for pattern in candidates:
        rc = reverse_complement(pattern)
        score = freq.get(pattern, 0) + freq.get(rc, 0)

        if score > max_score:
            max_score = score
            result = {pattern}
        elif score == max_score:
            result.add(pattern)

    return result
