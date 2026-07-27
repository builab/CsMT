# CsMT — a minimal CryoSPARC workflow for microtubule reconstruction

<p align="center">
  <img src="https://img.shields.io/badge/CryoSPARC-v5.0.6-blue?style=for-the-badge" alt="CryoSPARC 5.0.6"/>
  <img src="https://img.shields.io/badge/ChimeraX-Compatible-green?style=for-the-badge" alt="ChimeraX Compatible"/>
<img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="License: GPL v3"/>
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

For the full detailed explanation of Workflow features, refer to the [CryoSPARC Workflow Guide](https://guide.cryosparc.com/application-guide/workflows).

### Quick Setup

1. **Clone the Repository:** 

   ```bash
   git clone https://github.com/builab/CsMT.git
   ```
   
2. Import Workflow into CryoSPARC:

   In your CryoSPARC instance, navigate to Workflow sidebar panel.
   Click Import to import the pre-configured workflow Json from CsMT
   The csmt_13pf_v1.X.X is now appearing in your Workflow panel.
   Now, for your MT reconstruction project, create a Project and a Workspace.
   In that Workspace, click the workflow, then click Apply the CsMT workflow.


3. The detailed workflow

   You can see the detailed workflow here.

   ![CsMT Workflow Diagram](images/CsMT_workflow.png)

## Video guideline

   To come: 
   Reference generating
   Mask generations

## Citation

Tina Alagha, Asuva Arin, Nicolas Vangos, Helena Goodey-Parfitt, Hai Nguyen Ngo, Nhat Nam, Dau, Minh Hoa Nguyen, Thibault Legal, Michael Cianfrocco, Khanh Huy Bui. BioRxiv, 2026


