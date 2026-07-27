# CsMT — CryoSPARC Microtubule Processing Workflow

<p align="center">
  <img src="https://img.shields.io/badge/CryoSPARC-v5.0.6-blue?style=for-the-badge" alt="CryoSPARC 5.0.6"/>
  <img src="https://img.shields.io/badge/ChimeraX-Compatible-green?style=for-the-badge" alt="ChimeraX Compatible"/>
<img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="License: GPL v3"/>
</p>

<p align="center">
  CsMT: a minimal CryoSPARC workflow for cryo-EM reconstruction of microtubule.
</p>

---

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Workflow Import & Set up](#workflow-import--set-up)
- [Tutorial](#tutorial)
- [Video Guides](#video-guides)
- [References & Citation](#references--citation)
- [Contributing](#contributing)

---

## Overview

**CsMT** is a minimal [CryoSPARC](https://cryosparc.com/)-workflow for cryo-EM reconstruction of decorated and undecorated microtubules developed by the Bui Lab & Cianfrocco Lab. Microtubules present unique challenges for single-particle analysis — including their inherent pseudo-helical symmetry, seam localisation, and decorated states. CsMT workflow uses a protofilament-based classification approach to solve MT structures.

---

## Requirements

The required software dependencies for this workflow are:

| Software | Required Version | Purpose |
|---|---|---|
| **[CryoSPARC](https://cryosparc.com/)** | `v5.0.6` | Primary processing framework |
| **[UCSF ChimeraX](https://www.rbvi.ucsf.edu/chimerax/)** | Recommended latest | Ref/mask generation & map inspection |

---

## Workflow Import & Set up

For the full detailed explanation of Workflow features, refer to the [CryoSPARC Workflow Guide](docs/cryosparc_workflow_guide.md).

### Quick Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/builab/CsMT.git](https://github.com/builab/CsMT.git)
   cd CsMT
   ```
   
2. Import Workflow into CryoSPARC:

Open your CryoSPARC instance (v5.0.6).

Navigate to your target project and creation menu.

Import the pre-configured workflow JSON file located in workflows/csmt_v1.0.8_workflow.json.

The detail workflow

![CsMT Workflow Diagram](images/CsMT_workflow.png)

## Video guideline

To come

## Citation

Alagha. T., Arin, A., Vangos, N. et al. BioRxiv, 2026


