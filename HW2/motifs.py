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

def score(motifs: list[str]) -> int:
    """Calculate the score of a collection of motifs."""
    total = 0

    for column in zip(*motifs):
        total += len(column) - max(column.count(nucleotide) for nucleotide in "ACGT")

    return total

def gibbs_sampler(
    dna: list[str],
    k: int,
    n_iterations: int,
    rng: random.Random,
) -> list[str]:
    """Run Gibbs sampling and return the best motifs found."""
    motifs = random_motifs(dna, k, rng)
    best_motifs = motifs.copy()

    for _ in range(n_iterations):
        i = rng.randrange(len(dna))

        other_motifs = motifs[:i] + motifs[i + 1:]

        profile = {
            nucleotide: []
            for nucleotide in "ACGT"
        }

        for position in range(k):
            counts = {
                nucleotide: 1
                for nucleotide in "ACGT"
            }

            for motif in other_motifs:
                counts[motif[position]] += 1

            total = len(other_motifs) + 4

            for nucleotide in "ACGT":
                profile[nucleotide].append(counts[nucleotide] / total)

        motifs[i] = profile_randomly_generated_kmer(
            dna[i], k, profile, rng
        )

        if score(motifs) < score(best_motifs):
            best_motifs = motifs.copy()

    return best_motifs

def repeated_gibbs_sampler(
    dna: list[str],
    k: int,
    n_iterations: int,
    n_restarts: int,
    seed: int,
) -> tuple[list[str], list[int]]:
    """Run GibbsSampler repeatedly and return best motifs and all scores."""
    rng = random.Random(seed)

    best_motifs = []
    best_score = float("inf")
    scores = []

    for _ in range(n_restarts):
        motifs = gibbs_sampler(dna, k, n_iterations, rng)
        current_score = score(motifs)
        scores.append(current_score)

        if current_score < best_score:
            best_motifs = motifs.copy()
            best_score = current_score

    return best_motifs, scores