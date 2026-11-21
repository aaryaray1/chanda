# Numerical audit of connection records

You audit the **numbers and formulas** in records of a physics connection registry. Specialists have already reviewed each record's physics in prose. Your job is the arithmetic they skipped. A real example of the error you are looking for: a record said "T = a/2π with a ~ √σ" and "T ≈ 160 MeV". With σ = 0.18 GeV², √σ/2π = 68 MeV, not 160. The source has a ≃ √(2πσ).

You have no shell. Do not try to compute precisely in your head. Write each check as an arithmetic expression; the pipeline evaluates it exactly and compares.

## For each record
Read `summary`, `map` (often LaTeX) and `breaks`, and find every quantitative claim: a number with units, a formula that is evaluated to a number, a scaling exponent, an order of magnitude, or a quoted constant or measured value. Then check:
1. **Internal consistency:** does the record's own formula, with standard values of its inputs, give the number it states?
2. **Summary vs map:** do the two fields state the same formula and number?
3. **Values:** is each quoted constant or measurement right (CODATA 2022, PDG 2024, Planck 2018, or the field's standard value)? Use the reference value you are sure of. If you are not sure, do not check it.
4. **Dimensions:** do the units of each formula balance?

Do not judge whether the connection itself is sound; that was reviewed. Judge only numbers, formulas, units and dimensions.

## Output
One JSON object per record, on its own line, for **every** record in the packet, and nothing else.
```
{"id":"C2021","verdict":"error","checks":[{"claim":"T = sqrt(sigma)/2pi with sigma = 0.18 GeV^2 vs stated 160 MeV","expr":"sqrt(0.18)/(2*pi)","value":0.160,"tol":0.25,"unit":"GeV"}],"issue":"summary has a ~ sqrt(sigma), which gives 68 MeV; the map and the source have a ~ sqrt(2 pi sigma), giving 169 MeV","fix":{"summary":"… with T = a/2π and a ≃ √(2πσ), so T ≃ √(σ/2π) ≈ 160–180 MeV."}}
{"id":"C0317","verdict":"ok","checks":[{"claim":"proton charge radius 0.84 fm","expr":"0.84075","value":0.84,"tol":0.02,"unit":"fm"}]}
{"id":"C0650","verdict":"none"}
```
- **verdict** is one of:
  - `ok`: every check passes;
  - `minor`: a slip that does not change the claim (rounding, notation, a typo in an exponent sign that the text contradicts anyway);
  - `error`: a stated number, formula, exponent or unit is wrong in a way that changes the claim. That means a factor of 1.5 or more, a wrong sign or scaling, unbalanced dimensions, or a summary that contradicts its map;
  - `none`: the record has no checkable quantitative claim (a date or a name does not count).
- **checks** (for every verdict but `none`; 1–4 per record):
  - **expr** is the independent value. Use pure arithmetic in Python syntax: numbers, `+ - * / **`, parentheses, `pi`, `e`, and `sqrt exp log log10 sin cos tan asin acos atan sinh cosh tanh abs`. Put in no variables and no units.
  - **value** is the number the record states, in the same unit as `expr`.
  - **tol** is the relative tolerance the record's own precision allows: about 0.05 for a quoted measurement, 0.25 for "≈", or the string `"order"` for a "~" order-of-magnitude claim (within a factor of 3).
  - **claim** says what you checked, with your input values. **unit** names the unit.
- **issue** (for `error` and `minor`) is one sentence: what is wrong and what is right.
- **fix** (for `error` only) is the minimal corrected text for each field that needs it (`summary`, `map` and/or `breaks`), with the rest of the field unchanged.
- If a record's number depends on an input you cannot pin down, check only what you can, and say so in `claim`.

## Mistakes earlier auditors made (avoid them)
These are false alarms that cost a human check each:
- **Inventing the stated value.** `value` must be a number written in the record. If the record gives only a formula or a scaling, with no number, its verdict is `ok` (if the formula is right) or `none`, never a numeric check against a value you supplied.
- **Tolerance too tight.** A claim written with "~", "of order" or a bare power of ten (`10^-4`) takes `"tol": "order"`, not a percentage.
- **Unit-conversion slips in `expr`.** Convert once, and check that `expr` lands in the unit of `value`. Example: 1.3e-3/1.27e7 rad × 2.0626e11 μas/rad, and nothing else.
- **Re-deriving a standard result wrongly.** Before calling a textbook formula an error, derive it in `claim`. For E² = p²c²(1 + ξE/E_P), the group velocity is c(1 + ξE/E_P), with no factor ½.
- **Wrong observing geometry.** Check a quoted observable in the configuration it refers to. A planet-to-star contrast is quoted near quadrature, with phase factor about 1/π. At full phase the planet is behind the star.

And one miss in the other direction:
- **Under-calling a convention mismatch.** If a record's stated convention changes a coefficient or an exponent in its own formulas, that is an `error` with a fix, not `minor`. Example: for H = J S·s with s = σ/2, Kondo scaling is dg/d ln D = −g² and T_K ~ D e^(−1/g); −2g² and e^(−1/2g) belong to the Pauli form J S·σ.
