import random


def random_motifs(dna: list[str], k: int, rng: random.Random) -> list[str]:
    """Select one uniformly random k-mer window from every DNA string."""
    motifs = []

    for sequence in dna:
        start = rng.randint(0, len(sequence) - k)
        motifs.append(sequence[start:start + k])

    return motifs

def profile_randomly_generated_kmer(
    text: str,
    k: int,
    profile: dict[str, list[float]],
    rng: random.Random,
) -> str:
    """Select a k-mer randomly, with probability proportional to its profile weight."""
    kmers = [
        text[i:i + k]
        for i in range(len(text) - k + 1)
    ]

    weights = []
    for kmer in kmers:
        probability = 1.0
        for i, nucleotide in enumerate(kmer):
            probability *= profile[nucleotide][i]
        weights.append(probability)

    return rng.choices(kmers, weights=weights, k=1)[0]

