---
title: Medical imaging
summary: Imaging the body — projection radiography, computed tomography and reconstruction, MRI physics and contrast, functional MRI, image quality and dose.
query: medical imaging physics; computed tomography; magnetic resonance imaging
---
# Medical imaging
> [Interdisciplinary and Applied Physics](../../README.md) › [Medical physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** X-ray production and spectra, attenuation and contrast, CT acquisition and filtered back-projection, iterative and deep-learning reconstruction, photon-counting CT, NMR physics (precession, T1/T2 relaxation, spin echo), MRI gradients and k-space, pulse sequences, BOLD fMRI and diffusion MRI, SNR and resolution, patient dose and SAR.

**Core ideas.**
- CT reconstructs attenuation maps from line integrals — the Radon transform inverted.
- MRI encodes position in precession frequency via field gradients; images are Fourier transforms of k-space data.
- Contrast comes from relaxation-time differences between tissues, not density.

**Key equations.**
$$p(\theta,s)=\int\mu(x,y)\,\delta(x\cos\theta+y\sin\theta-s)\,dx\,dy,\qquad M_z(t)=M_0\left(1-e^{-t/T_1}\right),\quad M_{xy}(t)=M_0e^{-t/T_2}$$

**Landmarks.** Hounsfield (1973); Lauterbur (1973); Ogawa et al. (1990) — see [subfield landmarks](../README.md).

**See also.** [Fourier optics](../../../02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging/README.md) · [Angular momentum and spin](../../../04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md)
