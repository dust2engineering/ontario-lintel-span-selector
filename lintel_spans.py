#!/usr/bin/env python3
"""Part 9 wood lintel span selector (OBC 9.23.12.3) - verified subset:
SPF No.1/No.2, non-structural sheathing, 2-ply, roof + ceiling only.
Usage:
  python3 lintel_spans.py --size 2-38x184 --snow 2.0
  python3 lintel_spans.py --size 2-38x184 --interior
  python3 lintel_spans.py --snow 1.5 --need-span 2.2
"""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(__file__), "lintel-span-table.json")))
T = D["max_span_m"]; SSL = [1.0, 1.5, 2.0, 2.5, 3.0]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", default=None)
    ap.add_argument("--snow", type=float, choices=SSL, default=None)
    ap.add_argument("--interior", action="store_true")
    ap.add_argument("--need-span", type=float, default=None)
    a = ap.parse_args()
    col = 5 if a.interior else SSL.index(a.snow or 2.0)
    where = "interior wall" if a.interior else f"exterior wall, specified snow load {a.snow or 2.0} kPa"
    if a.need_span:
        ok = [(s, T[s][col]) for s in T if T[s][col] >= a.need_span]
        print(f"Smallest 2-ply SPF lintel spanning {a.need_span} m ({where}): {ok[0][0]} - max span {ok[0][1]} m" if ok else f"No 2-ply SPF lintel in this table spans {a.need_span} m ({where}).")
        return
    print(f"{a.size}, {where}: maximum span {T[a.size][col]} m (SPF No.1/No.2, non-structural sheathing, roof + ceiling only)")
if __name__ == "__main__":
    main()
