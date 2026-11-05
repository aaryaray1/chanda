---
name: derive-check
description: Check a physics derivation, formula, numerical result or quantitative claim for errors using dimensional analysis, limiting cases, symmetry, sympy re-derivation and CODATA-based numerics. Use whenever the user asks "is this right?", "check my derivation", "verify this formula", pastes working, or before presenting any non-trivial derivation of your own — and whenever a number looks surprising.
argument-hint: "[derivation, formula or claim]"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *) Bash(python - *)
---
# Derivation and claim checker

Target: $ARGUMENTS

For long or subtle derivations, delegate to the `derivation-checker` agent; for a single formula, run the checks below directly.

## Checks
1. **Dimensions.** Assign dimensions to every symbol and check each term. With sympy:
```python
from sympy.physics.units.systems.si import dimsys_SI
from sympy.physics.units.definitions.dimension_definitions import mass, length, time
expr_dim = mass * (length / time)**2  # kinetic energy
print(dimsys_SI.get_dimensional_dependencies(expr_dim))  # {M: 1, L: 2, T: -2}
```
2. **Limits.** Evaluate in regimes with known answers (small angle, $v\ll c$, $\hbar\to0$, weak coupling, high temperature). Use `sympy.limit` and `sympy.series`.
3. **Symmetry.** Behaviour under exchange of identical inputs, parity, time reversal, gauge transformations; sign of energies and probabilities.
4. **Re-derivation.** Reproduce the key steps symbolically; differentiate integrals back; substitute solutions into the original equation and simplify to zero.
```python
import sympy as sp
t, w, g = sp.symbols('t omega gamma', positive=True)
x = sp.exp(-g*t)*sp.cos(sp.sqrt(w**2-g**2)*t)
print(sp.simplify(sp.diff(x, t, 2) + 2*g*sp.diff(x, t) + w**2*x))
```
5. **Numbers.** Recompute with CODATA values (`python -I scripts/physlib.py constants "<name>"`) and numpy; compare to the claimed value and significant figures.
6. **Literature cross-check.** If the formula is "standard", compare with the topic README in `knowledge/` or a cited source; note convention differences (units, signature, normalization).

Run sympy with plain `python - <<'EOF' … EOF` (not `-I`, so the user-site sympy imports).

## Verdict format
For each claim: ✅ verified · ⚠️ correct with caveats (state them) · ❌ wrong (show the error, the corrected result, and how the check caught it). Include the code output that supports each verdict.
