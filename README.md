# CsMT — CryoSPARC Microtubule Processing Workflow

<p align="center">
  <img src="https://img.shields.io/badge/CryoSPARC-Compatible-blue?style=for-the-badge" alt="CryoSPARC Compatible"/>
  <img src="https://img.shields.io/badge/Microtubule-Processing-green?style=for-the-badge" alt="Microtubule Processing"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/DOI-Zenodo-orange?style=for-the-badge" alt="Zenodo DOI"/>
</p>

<p align="center">
  A structured CryoSPARC workflow for high-resolution cryo-EM processing of microtubule datasets, including particle picking, 2D/3D classification, CTF refinement, and masked refinement using optimized microtubule masks.
</p>

---

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Workflow Overview](#workflow-overview)
  - [Step 1 — Data Import & Preprocessing](#step-1--data-import--preprocessing)
  - [Step 2 — CTF Estimation](#step-2--ctf-estimation)
  - [Step 3 — Microtubule Picking](#step-3--microtubule-picking)
  - [Step 4 — Particle Extraction](#step-4--particle-extraction)
  - [Step 5 — 2D Classification](#step-5--2d-classification)
  - [Step 6 — 3D Reconstruction & Refinement](#step-6--3d-reconstruction--refinement)
  - [Step 7 — Masked Refinement](#step-7--masked-refinement)
  - [Step 8 — Post-processing](#step-8--post-processing)
- [Masks](#masks)
- [Video Guides](#video-guides)
- [References & Citation](#references--citation)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**CsMT** (*CryoSPARC Microtubule*) is a community-developed, step-by-step processing guide and resource collection for cryo-EM structural analysis of microtubules using [CryoSPARC](https://cryosparc.com/). Microtubules present unique challenges for single-particle analysis — including their inherent helical symmetry, seam localisation, and decorated states — and this workflow addresses each step with tailored parameters and masks.

> This repository accompanies the Zenodo dataset and mask archive. If you use these resources in your research, please cite accordingly (see [References](#references--citation)).

---

## Requirements

| Dependency | Version | Notes |
|---|---|---|
| [CryoSPARC](https://cryosparc.com/) | v4.0+ | Lane or cluster install |
| CTFFIND / Patch CTF | v4.1+ | Bundled with CryoSPARC |
| UCSF ChimeraX | v1.6+ | For mask inspection |
| RELION (optional) | v4+ | For helical refinement cross-check |
| Python | 3.8+ | For helper scripts |

**Hardware:** GPU with ≥16 GB VRAM recommended. All refinement steps were benchmarked on NVIDIA A100 (80 GB).

---

## Installation & Setup

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/CsMT.git
cd CsMT

# (Optional) Create a Python environment for helper scripts
conda create -n csmt python=3.10
conda activate csmt
pip install -r requirements.txt
```

Download the pre-made masks and reference volumes from Zenodo (see [Masks](#masks)) and place them in the `masks/` directory:

```
CsMT/
├── masks/
│   ├── mt_monomer_mask.mrc
│   ├── mt_tubulin_dimer_mask.mrc
│   └── mt_decorated_mask.mrc
├── scripts/
├── docs/
└── README.md
```

---

## Workflow Overview

The diagram below summarises the full CsMT pipeline:

```
Raw Micrographs
      │
      ▼
 Motion Correction (Patch Motion)
      │
      ▼
 CTF Estimation (Patch CTF)
      │
      ▼
 Filament / MT Picking
      │
      ▼
 Particle Extraction (boxsize 512 Å recommended)
      │
      ▼
 2D Classification ──► Reject bad classes
      │
      ▼
 Ab initio / Import reference
      │
      ▼
 Homogeneous Refinement (C1)
      │
      ▼
 Non-Uniform Refinement
      │
      ▼
 Masked Local Refinement (MT mask)
      │
      ▼
 CTF Refinement → Global/Local
      │
      ▼
 Final Post-Processing (DeepEMhancer / LocScale)
```

---

### Step 1 — Data Import & Preprocessing

Import your raw movies and run **Patch Motion Correction** with the following recommended settings:

| Parameter | Recommended Value |
|---|---|
| Output F-crop factor | 0.5 |
| Number of patches | 5 × 5 |
| B-factor | 500 |
| EER fractionation | Dataset-dependent |

> **Tip:** For EER data, group frames to achieve ~1.0 e⁻/Å² per fraction.

---

### Step 2 — CTF Estimation

Use **Patch CTF Estimation** (bundled in CryoSPARC). Key parameters:

| Parameter | Recommended Value |
|---|---|
| Min resolution | 30 Å |
| Max resolution | 5 Å |
| Min / Max defocus | 0.5 – 3.5 µm |

Filter micrographs by CTF fit resolution < 5 Å before proceeding.

---

### Step 3 — Microtubule Picking

Microtubules require **filament-mode picking**. In CryoSPARC, use the **Filament Tracer** job:

| Parameter | Recommended Value |
|---|---|
| Filament diameter | 250 Å |
| Separation distance | 82 Å (1× tubulin dimer) |
| Min filament length | 6 segments |
| NMS radius | 80 Å |

> For decorated microtubules (e.g., kinesin, dynein, tau), increase the separation distance to match the repeat unit of the decoration.

---

### Step 4 — Particle Extraction

Extract particles with a generous box size to retain low-frequency signal:

| Parameter | Recommended Value |
|---|---|
| Box size | 512 px (at raw pixel size) |
| Extraction box size | 384 px (after downsampling) |
| Fourier crop to | 256 px for initial rounds |

---

### Step 5 — 2D Classification

Run **2D Classification** with 100–200 classes. Select classes that show clear tubulin protofilament features and lateral contacts:

- ✅ Accept: classes showing 8 nm periodicity, clear PF ridges
- ❌ Reject: ice, carbon edges, aggregates, end-on views

---

### Step 6 — 3D Reconstruction & Refinement

1. **Ab initio reconstruction** (C1, 3–5 classes) to generate an unbiased starting model.
2. **Homogeneous Refinement** with C1 symmetry — do **not** impose helical symmetry at this stage.
3. **Non-Uniform Refinement** to improve map quality at MT-ligand interfaces.

> **Seam identification:** After an initial refinement, use the seam-search protocol (see `scripts/seam_search.py`) to identify the seam location before applying pseudo-helical refinement.

---

### Step 7 — Masked Refinement

Download the appropriate mask from Zenodo (see [Masks](#masks)) and run **Local Refinement** in CryoSPARC:

```
Jobs → Local Refinement
  └─ Input: particles + volume from Non-Uniform Refinement
  └─ Mask: mt_monomer_mask.mrc  (or decorated variant)
  └─ Dynamic mask: OFF
  └─ Search extent (Å): 20
  └─ Search range (°): 5
```

| Mask | Use Case |
|---|---|
| `mt_monomer_mask.mrc` | α/β-tubulin monomer focus |
| `mt_tubulin_dimer_mask.mrc` | Full dimer asymmetric unit |
| `mt_decorated_mask.mrc` | MT + MAPs / motor proteins |

---

### Step 8 — Post-processing

- **Global CTF Refinement** → **Local CTF Refinement** (beam-tilt, trefoil, anisotropic magnification)
- **Bayesian Polishing** (if transferring to RELION) or **Patch-based motion** re-extraction
- Sharpening with **DeepEMhancer** or **LocScale** for interpretation

---

## Masks

All masks were generated in UCSF ChimeraX from PDB structures and are available for download on Zenodo:

> 📦 **Zenodo Archive — CsMT Masks & References**
> [https://doi.org/10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)

The archive contains:
- Pre-made `.mrc` masks at multiple pixel sizes (1.0 Å, 1.5 Å, 2.0 Å/px)
- Reference half-maps for supervised refinement
- ChimeraX session files for mask inspection
- A template CryoSPARC project `.json` export

To inspect a mask locally:

```bash
# Open mask alongside your map in ChimeraX
open mt_monomer_mask.mrc
open your_refined_map.mrc
```

---

## Video Guides

Step-by-step video tutorials are available on YouTube. Click a thumbnail to watch:

| # | Topic | Link |
|---|---|---|
| 1 | Introduction & Project Setup | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |
| 2 | Motion Correction & CTF Estimation | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |
| 3 | Filament Picking & Particle Extraction | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |
| 4 | 2D & 3D Classification | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |
| 5 | Masked Local Refinement | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |
| 6 | CTF Refinement & Polishing | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |
| 7 | Post-processing & Visualisation | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX) |

> 💡 All videos are also linked in the [docs/](docs/) folder with timestamps and supplementary notes.

---

## References & Citation

If you use **CsMT**, the provided masks, or reference volumes in your work, please cite:

### This Workflow

```bibtex
@misc{csmt2024,
  author       = {YOUR NAME},
  title        = {{CsMT}: A CryoSPARC Workflow for Microtubule Processing},
  year         = 2024,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

> 📄 Zenodo record: [https://doi.org/10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)

### CryoSPARC

> Punjani, A., Rubinstein, J. L., Fleet, D. J. & Brubaker, M. A. (2017). cryoSPARC: algorithms for rapid unsupervised cryo-EM structure determination. *Nature Methods*, 14, 290–296. https://doi.org/10.1038/nmeth.4169

### Relevant Microtubule Structural References

> Alushin, G. M. et al. (2014). High-resolution microtubule structures reveal the structural transitions in αβ-tubulin upon GTP hydrolysis. *Cell*, 157(5), 1117–1129. https://doi.org/10.1016/j.cell.2014.03.053

> Zhang, R. & Bharat, T. A. M. (2019). Microtubule structure at 2.2 Å resolution. *Nature*, 570(7761), 339–343. https://doi.org/10.1038/s41586-019-1202-x

---

## Contributing

Contributions are welcome! Please open an **issue** or submit a **pull request** for:

- Bug fixes in helper scripts
- Improved parameter recommendations
- New masks or reference volumes
- Additional tutorial videos

Please follow the [contribution guidelines](CONTRIBUTING.md) and ensure any new masks are deposited to Zenodo and linked here.

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

Masks and reference volumes deposited on Zenodo are released under [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

<p align="center">
  Made with ❤️ for the cryo-EM community · <a href="https://doi.org/10.5281/zenodo.XXXXXXX">Zenodo</a> · <a href="https://www.youtube.com/channel/XXXXXXX">YouTube</a>
</p>
