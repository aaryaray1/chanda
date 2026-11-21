# Numerical audit of the connection registry

Generated 2026-11-21 14:46 from 20 audit packets (12 done). Records audited: 480.
- 5 error, 0 minor, 294 ok, 181 with nothing to check.
- 0 more have an arithmetic mismatch that the auditor did not call an error: either the record or the auditor's check is wrong.
- Every record in a finished packet has a verdict.

Nothing here is applied automatically. Check a record, preview its fix with `python -I scripts/connections_pipeline.py apply-audit C0123 --dry-run`, then run it without `--dry-run`.

## Errors to check (0)


## Arithmetic mismatches to look at (0)


## Fixed in the registry (5)

- **C0064** Fictitious forces as connection coefficients: sign convention mixed: the Coriolis term is written as a force (-2 Omega x v) but the centrifugal term as the equation-of-motion term (+Omega x (Omega x r)); as a force it is -Omega x (Omega x r)
  - fix: {"map": "\\ddot x^i+\\Gamma^i_{\\mu\\nu}\\dot x^\\mu\\dot x^\\nu=F^i/m,\\ x^0=t;\\ \\Gamma^i_{0j}=\\epsilon_{ijk}... \\Rightarrow -2\\boldsymbol\\Omega\\times\\mathbf v,\\ \\Gamma^i_{00}\\Rightarrow-\\boldsymbol\\Omega\\times(\\boldsymbol\\Omega\\times\\mathbf r)"}
- **C0657** Lighthill's acoustic quadrupole and GW quadrupole: The acoustic far-field p expression lacks the factor 1/c0², so its dimensions do not balance (it gives Pa·m²/s² instead of Pa); the correct form is p ≈ x̂ᵢx̂ⱼ/(4π c0² r) ∂ₜ²∫Tᵢⱼ dV.
  - ∫T_ij dV = ½ d²I_ij/dt², so 4G/(c⁴r)·½ = 2G/(c⁴r): `4*0.5` = 2.0 vs stated 2 1 → agrees
  - fix: {"map": "\\partial_t^2\\rho-c_0^2\\nabla^2\\rho=\\partial_i\\partial_jT_{ij}\\Rightarrow p\\approx\\frac{\\hat x_i\\hat x_j}{4\\pi c_0^2 r}\\partial_t^2\\!\\int T_{ij}\\,dV\\ \\leftrightarrow\\ h_{ij}=\\frac{4G}{c^4r}\\int T_{ij}\\,dV=\\frac{2G}{c^4r}\\ddot I_{ij}"}
- **C1506** Wilson's numerical RG solves the Kondo problem: convention mismatch by a factor 2: for H = J S.s with s = psi^dag (sigma/2) psi, one-loop scaling is dg/dlnD = -g^2 and T_K ~ D e^{-1/g} (Affleck 2008, arXiv:0809.3474, eqs 1.15, 1.23, 1.25); -2g^2 and e^{-1/2g} hold for the Pauli form J S.(psi^dag sigma psi) (Hewson)
  - fix: {"map": "\\frac{dg}{d\\ln D}=-g^2,\\quad k_BT_K\\sim D\\,e^{-1/g},\\quad g=\\rho J\\ (H=J\\,\\mathbf S\\cdot\\mathbf s,\\ \\mathbf s=\\psi^\\dagger\\tfrac{\\boldsymbol\\sigma}{2}\\psi)"}
- **C1737** Proton radius from hydrogen and muonic hydrogen: m_r^3 c^4/(hbar c)^2 <r^2> has dimensions of mass (sympy, 2026-11-21); an energy needs c^6. The c^6 form gives 5.1975 meV/fm^2 for the muonic-hydrogen 2S shift, the leading finite-size term
  - muonic-hydrogen 2S finite-size coefficient from the corrected map, (1/12) alpha^4 m_r^3 c^6/(hbar c)^2, CODATA 2022: `(1/12)*(7.2973525643e-3)**4*(105.6583755*938.27208943/(105.6583755+938.27208943))**3/197.3269804**2*1e9` = 5.1975 vs stated 5.2 meV/fm^2 → agrees
  - fix: {"map": "\\Delta E_{\\rm fs}=\\frac{2}{3n^3}(Z\\alpha)^4\\frac{m_r^3c^6}{(\\hbar c)^2}\\langle r_p^2\\rangle\\,\\delta_{\\ell0}"}
- **C2021** Hadronization as Unruh radiation: the summary has a ~ sqrt(sigma), giving 64-71 MeV; the map and the source have a ~ sqrt(2 pi sigma), giving 160-180 MeV (see connections/frontier/results/C2021-unruh-hadronization.md)
  - registry summary: T = sqrt(sigma)/2pi with sigma = 0.16-0.20 GeV^2, vs the stated 160 MeV: `sqrt(0.18)/(2*pi)` = 0.0675237 vs stated 0.16 GeV → MISMATCH
  - source eqs 57-58 (arXiv:0704.1426): T = sqrt(sigma/(2 pi)) with sigma = 0.18 GeV^2: `sqrt(0.18/(2*pi))` = 0.169257 vs stated 0.17 GeV → agrees
  - fix: {"summary": "Thermal hadron yields with a universal T near 160 MeV in e+e-, pp and AA have been modelled as Unruh radiation from quarks decelerated by the string tension at a confinement horizon, with T = a/2π and a ≃ √(2πσ), so T ≃ √(σ/2π) ≈ 160–180 MeV."}

## Dismissed after a hand check (6)

- **C0229** VLBI: heterodyne receivers, maser clocks and correlators: false alarm, 2026-11-21: the auditor's expression has stray unit factors; 1.3e-3/1.27e7 rad = 1.02e-10 rad = 21.1 μas, as the record states
- **C0245** Planck-suppressed dispersion and GRB time-of-flight bounds: false alarm, 2026-11-21: for E^2 = p^2c^2(1 + xi E/E_P) the group velocity is c(1 + xi E/E_P) (sympy), so Delta t = xi (E/E_P)(D/c) as the record states; the auditor's factor 1/2 is wrong
- **C0455** Scaling laws in cell and membrane mechanics: false alarm, 2026-11-21: 'Re ~ 10^-4' is an order-of-magnitude claim; 1000*30e-6*1e-6/1e-3 = 3e-5 is within it (the auditor used a 15% tolerance)
- **C0865** Plateau–Rayleigh and membrane shape instabilities: false alarm, 2026-11-21: the record states no number; the auditor compared against a value it supplied itself
- **C1107** Ultrastrong magnetic fields in heavy-ion collisions: false alarm, 2026-11-21: eB = m_pi^2 is B = 3.3e14 T (3.3e18 G); '~10^14 T' is the order-of-magnitude form used in the literature ('~10^18 G'), not a 15% claim
- **C1178** Interferometry and direct imaging of exoplanets: false alarm, 2026-11-21: the auditor used full phase, when the planet is behind the star; at quadrature A_g (R/a)^2/pi = 1.2-2.1e-10 for A_g = 0.2-0.37, so 'about 1e-10' stands
