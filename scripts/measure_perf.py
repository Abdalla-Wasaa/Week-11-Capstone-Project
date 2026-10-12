#!/usr/bin/env python3
"""Change for your project: nothing. Times N calls to a URL and writes perf_stub.json."""
import argparse
import json
import math
import time
import urllib.error
import urllib.request


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://localhost:8080/health")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--out", default="perf_stub.json")
    args = ap.parse_args()

    if args.n < 1:
        ap.error("--n must be at least 1")

    samples = []
    for _ in range(args.n):
        start = time.perf_counter()
        try:
            with urllib.request.urlopen(args.url, timeout=5):
                pass
        except (urllib.error.URLError, TimeoutError) as exc:
            ap.error(f"Health request failed: {exc}")
        samples.append(time.perf_counter() - start)

    samples.sort()
    idx = max(0, math.ceil(len(samples) * 0.95) - 1)
    p95 = samples[idx] if samples else 0.0

    out = {
        "endpoint": args.url,
        "p95_seconds": round(p95, 4),
        "caption": "laptop teaching stub; not a production SLA",
        "n_samples": args.n,
    }
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {args.out}: p95={out['p95_seconds']}s over {args.n} samples")


if __name__ == "__main__":
    main()
