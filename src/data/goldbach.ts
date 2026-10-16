// Public, curated summaries from “Explore the Goldbach conjecture”.
// Keep private conversation content and local Codex links out of the public site.
export const research = {
  updated: "2026-10-16",
  phase: "Foundations & exploration",
  next: "Compare midpoint-centered geometry with modular divisibility constraints, then record reproducible experiments.",
};

export const directions = [
  { id: "bounded", number: "01", title: "Bounded number axes", status: "Construction defined", formula: "bₛ(x) = x / (s + |x|)", text: "Place every integer inside (−1, 1). Investigate how compression changes distances, and how centering the map at a Goldbach midpoint preserves reflection.", question: "Can a midpoint-adapted geometry expose a useful bound on prime pairs?" },
  { id: "coordinates", number: "02", title: "Geometry of divisibility", status: "Proposed", formula: "θℓ(n) = (n mod ℓ) / ℓ", text: "Give each small prime its own circular coordinate. Divisibility becomes alignment at zero; addition becomes angular addition modulo one turn.", question: "What can interactions between these constraints tell us about surviving pairs?" },
  { id: "operators", number: "03", title: "Arithmetic through operators", status: "Identity checked", formula: "D(m, d) = Ω(m² − d²) − 2", text: "Prime-exponent vectors turn multiplication into addition. A factor-count operator vanishes exactly when both reflected candidates are prime, for integer m ≥ 2 and 0 ≤ d ≤ m − 2.", question: "Can we estimate this operator without moving the difficulty into factorization?" },
  { id: "symmetry", number: "04", title: "Symmetry & mathematical constants", status: "Exploring", formula: "C(t) = ((1−t²)/(1+t²), 2t/(1+t²))", text: "Revisit rotated Ulam spirals, alternative grids, and rational circle coordinates. Track which patterns come from arithmetic and which are imposed by the representation.", question: "Which relationships survive a change of coordinates, and where do constants enter?" },
];

// Newest first. These describe project milestones, never a percentage toward proof.
export const milestones = [
  { id: "factor-count", date: "2026-10-16", kind: "Identity checked", title: "An exact factor-count reformulation", summary: "For the stated integer domain, D(m, d) ≥ 0 and D(m, d) = 0 precisely when m − d and m + d are both prime.", detail: "Ω counts prime factors with multiplicity. Since m² − d² = (m − d)(m + d), and both factors are at least 2, each contributes at least one prime factor. The total is 2 exactly when both factors are prime. This is an equivalent restatement of the pair condition; computing Ω still requires arithmetic work." },
  { id: "midpoint", date: "2026-10-16", kind: "Construction defined", title: "Compression that preserves midpoint symmetry", summary: "A bounded coordinate centered at m sends m − d and m + d to exact reflections. Centering at zero generally changes their spacing around the transformed midpoint.", detail: "The map x ↦ (x − m)/(s + |x − m|), with s > 0, sends the pair to −d/(s+d) and d/(s+d). The global map x ↦ x/(s+|x|) is injective but nonlinear, so it does not generally preserve arithmetic midpoints. The coordinate identity is exact; an advantage for proving Goldbach remains an open question." },
  { id: "research-program", date: "2026-10-16", kind: "Research agenda", title: "A program built around representations", summary: "Earlier visual work on rotated prime spirals and alternative grids informs four directions: bounded axes, divisibility coordinates, new operators, and the role of constants.", detail: "The guiding question is what addition looks like in each representation. For Goldbach, p + q = 2m is a reflection about m on the ordinary number line. Experiments should preserve enough information to recover the original arithmetic and distinguish imposed symmetry from a new prime relationship." },
];

export const references = [
  { title: "Empirical verification of the even Goldbach conjecture and computation of prime gaps up to 4 · 10¹⁸", authors: "T. Oliveira e Silva, S. Herzog & S. Pardi · Mathematics of Computation, 2014", url: "https://www.ams.org/mcom/2014-83-288/S0025-5718-2013-02787-1/", note: "A published computational verification bound; it is external work, not a result of this project." },
  { title: "The ternary Goldbach conjecture is true", authors: "Harald Andrés Helfgott · 2013", url: "https://arxiv.org/abs/1312.7748", note: "The three-prime theorem concerns odd integers greater than 5. It is distinct from the binary conjecture studied here." },
  { title: "Rational Curves", authors: "Ching-Kuang Shene · Michigan Technological University", url: "https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/curves/rational.html", note: "Background for expressing circle geometry with rational functions." },
];
