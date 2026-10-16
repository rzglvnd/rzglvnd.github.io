export function primeSieve(limit: number): Uint8Array {
  const prime = new Uint8Array(limit + 1).fill(1);
  prime[0] = prime[1] = 0;
  for (let p = 2; p * p <= limit; p++) {
    if (prime[p]) for (let n = p * p; n <= limit; n += p) prime[n] = 0;
  }
  return prime;
}

export function goldbachPairs(n: number, prime: Uint8Array): [number, number][] {
  if (!Number.isInteger(n) || n < 4 || n % 2 || n >= prime.length) return [];
  const pairs: [number, number][] = [];
  for (let p = 2; p <= n / 2; p++) if (prime[p] && prime[n - p]) pairs.push([p, n - p]);
  return pairs;
}

export function bounded(x: number, scale: number, center = 0): number {
  return (x - center) / (scale + Math.abs(x - center));
}

export function ulamPoints(side: number) {
  const prime = primeSieve(side * side);
  const points: { n: number; x: number; y: number }[] = [];
  let x = 0, y = 0, n = 1, length = 1, direction = 0;
  const steps = [[1, 0], [0, -1], [-1, 0], [0, 1]];
  while (n < side * side) {
    for (let twice = 0; twice < 2; twice++) {
      const [dx, dy] = steps[direction++ % 4];
      for (let i = 0; i < length && n < side * side; i++) {
        x += dx; y += dy; n++;
        if (prime[n]) points.push({ n, x, y });
      }
    }
    length++;
  }
  return points;
}
