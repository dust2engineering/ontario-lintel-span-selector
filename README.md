# Ontario Lintel Span Selector (OBC 9.23.12.3) — Verified Subset

Maximum spans for built-up wood lintels under OBC Sentence 9.23.12.3.(1), for the subset that can be verified from readable public sources: SPF No. 1/No. 2, non-structural sheathing, 2-ply lintels supporting roof and ceiling only, by specified snow load for exterior walls plus the interior-wall column. The narrower scope is deliberate and is stated on the tool itself.

**Live web tool:** https://dust2engineering.github.io/ontario-lintel-span-selector/web/

## How it works

- Look up a span by lintel size and snow load (or the interior column), or enter an opening width and get the smallest 2-ply lintel that covers it.
- Check applicability first: residential occupancy, studs over 38 × 64, supported joist spans ≤ 4.9 m, truss spans ≤ 9.8 m.
- If your condition is 3-ply, roof-plus-storeys, or structural sheathing, this tool does not answer it — those tables are excluded, not estimated.

## Data in this repository

- `lintel-span-table.json` — the verified subset with its scope, applicability rules and provenance stated in the file.
- Read from the Table A-15 excerpt in the CSA Z240.2.1 technical paper; cross-checked against the City of Niagara Falls guide citing the same OBC table (two cells match exactly) and a 2024 Ontario permit lintel schedule. The 2024 Code renumbers these tables 9.23.12.3.-A to -D; the letter-to-condition mapping could not be verified publicly and is not asserted.

## Command line

```bash
python3 lintel_spans.py --size 2-38x184 --snow 2.0
```

## Worked examples

- [example-lookup.txt](examples/example-lookup.txt)
- [example-reverse.txt](examples/example-reverse.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Structural. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
