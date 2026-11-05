---
name: solve-problem
description: Solve physics problems step by step — homework, exam, olympiad or research-style — by identifying principles, setting up the model, solving symbolically, plugging in CODATA values, and checking units, limits and magnitude. Use whenever the user gives a physics problem, asks "calculate", "find", "how fast/far/long/much", "derive the expression for", or pastes an exercise; offer a hint ladder instead of a full solution when the user wants to learn.
argument-hint: "[problem statement]"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *)
---
# Solve a physics problem

Problem: $ARGUMENTS

## Mode
If the user signals they want to learn ("hint", "don't give the answer", "help me understand"), use the **hint ladder**: give hint 1 (which principle), stop, then hint 2 (setup), hint 3 (key step), solution only on request. Otherwise give the full solution.

## Steps
1. **Understand** — list givens with units, the unknown(s), and draw/describe the setup. Note implicit assumptions (frictionless, ideal gas, non-relativistic, $g=9.81$ m/s²).
2. **Model** — name the governing principles (conservation laws, Newton, Maxwell, Schrödinger, thermodynamic identities). Read the relevant topic README in `knowledge/` for the standard equations and conventions.
3. **Plan** — say which equations close the system and in what order.
4. **Solve symbolically** — keep symbols to the end; box the general result.
5. **Check the symbolic result** — dimensions, limiting cases, symmetry. For anything non-trivial run a sympy check (`python - <<'EOF' … EOF`) or use the `derive-check` skill.
6. **Numbers** — constants from `python -I scripts/physlib.py constants "<name>"`; carry units; round only at the end; significant figures match the inputs.
7. **Sanity check** — compare with a known scale ("faster than sound?", "bigger than the atom?").
   **Self-consistency:** every approximate statement you make ("the correction is ≈ K/4mc²", "scales as $T^{3/2}$") must be *derived* — expand with `sympy.series`, don't recall the coefficient — and must reproduce the numbers you computed. Recalled prefactors are the most common error in otherwise-correct solutions.
8. **Answer** — final value with units and uncertainty if inputs had one; one sentence interpreting it.

## Output template
```
**Given:** … **Find:** … **Assume:** …
**Principles:** …
**Solution:** (numbered steps with equations)
**Result:** $$\boxed{…}$$  ≈ <number with units>
**Checks:** units ✓, limit … ✓, magnitude ✓
```
