# CsMT — a robust and streamlined CryoSPARC workflow for microtubule reconstruction

<p align="center">
  <img src="https://img.shields.io/badge/CryoSPARC-v5.0.6-blue?style=for-the-badge" alt="CryoSPARC 5.0.6"/>
  <img src="https://img.shields.io/badge/ChimeraX-v1.7-green?style=for-the-badge" alt="ChimeraX 1.7"/>
<img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="License: GPL v3"/>
</p>

---

## Table of Contents

- [Overview](#overview)
- [Release Notes](#release-notes)
- [Requirements](#requirements)
- [Workflow Import & Set up](#workflow-import--set-up)
- [Guideline](#guideline)
- [Citation](#citation)

---

## Overview

**CsMT** is a minimal [CryoSPARC](https://cryosparc.com/)-workflow for cryo-EM reconstruction of decorated and undecorated microtubules developed by the Bui Lab & Cianfrocco Lab. Microtubules present unique challenges for single-particle analysis — including their inherent pseudo-helical symmetry, seam localisation, and decorated states. CsMT workflow uses a protofilament-based classification approach to solve MT structures.

---

## Release Notes

### Current version

   * csMT_13pf_v1.0.9: Add Volume Tools for mask creation for Local Refinement after Symmetry Expansion
   * csmt_13pf_1pf_v1_0_9_single_pf_refinement_branch: Branch for 1-PF refinement

### Old version

   * csMT_13pf_v1.0.8: First version of undecorated 13-PF analysis
   
---

## Requirements

The required software dependencies for this workflow are:

| Software | Tested Version | Purpose |
|---|---|---|
| **[CryoSPARC](https://cryosparc.com/)** | `v5.0.6` | Primary processing framework |
| **[UCSF ChimeraX](https://www.rbvi.ucsf.edu/chimerax/)** | `v1.7` | Ref/mask generation & map inspection |

---

## Workflow Import & Set up

For the full detailed explanation of Workflow features, refer to the [CryoSPARC Workflow Guide](https://guide.cryosparc.com/application-guide/workflows).

1. **Clone the Repository:** 

   ```bash
   git clone https://github.com/builab/CsMT.git
   ```
   
2.  **Import Workflow into CryoSPARC:**

   * In your CryoSPARC instance, navigate to the **Workflow** sidebar panel.
   * Click **Import** to load the pre-configured workflow JSON from **CsMT**.
   * The `csmt_13pf_v1.X.X` workflow will now appear in your Workflow panel.
   * For your microtubule reconstruction project, create a **Project** and a **Workspace**.
   * Inside that Workspace, select the workflow and click **Apply** to run the CsMT workflow.


3.  **The workflow**

   ![CsMT Workflow Diagram](images/CsMT_workflow.png)

## Guideline

If you have any questions regarding the workflow, please put in the Issues in Github.

   * [CsMT Guideline](CsMT_Guideline_v0.1.pdf) 
   * YouTube Tutorial of Making References (To come)
   * YouTube tutorial of Making Masks (To come)

## Citation

If you use our workflow, please cite:

   > Tina Alagha, Asuva Arin, Nicolas Vangos, Helena Goodey-Parfitt, Hai Nguyen Ngo, Nhat Nam, Dau, Minh Hoa Nguyen, Thibault Legal, Michael Cianfrocco, Khanh Huy Bui. (2026). CsMT: a robust and streamlined CryoSPARC workflow for cryo-EM reconstruction of microtubules. bioRxiv 2026.07.31.741890; doi: https://doi.org/10.64898/2026.07.31.741890

