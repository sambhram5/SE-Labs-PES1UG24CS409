# Lab 2: Agile Backlog Creation & Sprint Simulation in Jira

**Institution:** PES University – Department of Computer Science and Engineering  
**Course:** Software Engineering (SE) Lab  
**Problem Statement #40:** Student Startup Crowdfunding Platform  
**Student Name:** Sambhram M  
**SRN:** PES1UG24CS409  

---

## 📌 Executive Summary & Objective

In this lab, the Functional Requirements established in **Lab 1 (FR-001 through FR-005)** were systematically converted into Agile backlog items (Epics, User Stories, and Tasks), prioritized, estimated using Fibonacci Story Points via Planning Poker, and simulated across two consecutive 1-week Sprints in **Atlassian Jira Software**. 

Sprint progress, velocity, and capacity were tracked and analyzed using Jira's **Burndown Charts**, followed by a comprehensive retrospective addressing estimation accuracy, prioritization, and sprint alignment.

---

## 📁 Lab 2 Deliverables Directory Structure

```text
Lab-2/
├── README.md                                          # Lab report and documentation
│
├── [Deliverables as specified in Handout]
├── EPICs.pdf                                          # Deliverable 1: Epics and User Stories (PDF)
├── Burndown_chart.pdf                                 # Deliverable 2: Burndown Chart and Analysis (PDF)
├── Reflection_Questions.pdf                           # Document answering the 4 reflection questions (PDF)
├── Reflection_Questions.docx                          # Document answering the 4 reflection questions (Word DOCX)
│
├── [Comprehensive Supporting Documents]
├── Lab2_Agile_Backlog_and_Sprint_Simulation.pdf       # Consolidated Master Submission PDF (7 pages)
├── EPICs_and_User_Stories.pdf                         # Epics & User Stories Detailed Specification (PDF)
├── EPICs_and_User_Stories.docx                        # Epics & User Stories Formatted Word Document
├── Burndown_Chart_Analysis.pdf                        # Burndown Chart & Sprint Analysis Detailed (PDF)
├── Burndown_Chart_and_Sprint_Analysis.docx            # Burndown Chart & Sprint Analysis Formatted Word Document
│
├── [Jira Workspace Assets]
├── Jira_Backlog_Import.csv                            # Ready-to-import CSV for Jira Cloud/Server
└── screenshots/
    ├── 01_jira_backlog_with_epics.png                 # Jira Backlog view with Epics panel & Sprints
    ├── 02_story_point_assignments.png                 # Planning Poker estimation & issue detail view
    ├── 03_sprint_1_active_board.png                   # Sprint 1 Active Scrum Board (Completed)
    ├── 04_sprint_1_burndown_chart.png                 # Sprint 1 Burndown Chart (29 Story Points)
    ├── 05_sprint_2_active_board.png                   # Sprint 2 Active Scrum Board (Completed)
    └── 06_sprint_2_burndown_chart.png                 # Sprint 2 Burndown Chart (32 Story Points)
```

---

## 🏗️ 1. Decomposition of Lab 1 Requirements into Epics & User Stories

All User Stories strictly follow the Agile template:  
> **"As a [user persona], I want [goal/action], So that [business benefit/outcome]."**

### Backlog Matrix

| Epic ID & Name | Story ID | User Story Summary | Agile User Story Statement | Priority | Points | Target Sprint |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| **Epic 1: Campaign Creation** *(FR-002, UC-01)* | `SSCP-1` | Campaign Target & Info | **As a** Student Founder, **I want to** define my campaign title, pitch, category, and total funding target, **So that** potential backers understand the venture proposition and capital needs. | High | 5 | Sprint 1 |
| **Epic 1: Campaign Creation** *(FR-002, UC-01)* | `SSCP-2` | Campaign Duration | **As a** Student Founder, **I want to** set the start and end dates for my campaign, **So that** the fundraising campaign is time-bound and builds momentum. | High | 3 | Sprint 1 |
| **Epic 1: Campaign Creation** *(FR-002, UC-01)* | `SSCP-3` | Milestone & Tranche Breakdown | **As a** Student Founder, **I want to** divide my project roadmap into distinct sequential milestones with individual funding tranches, **So that** funds can be disbursed in structured, verifiable phases. | High | 8 | Sprint 1 |
| **Epic 2: Backer Pledging & Escrow** *(FR-003, UC-02, UC-03)* | `SSCP-4` | Reward Tier Selection | **As a** Campaign Backer, **I want to** view available reward tiers and select one (or opt out) during checkout, **So that** I receive tangible incentives and perks for my contribution. | Medium | 5 | Sprint 1 |
| **Epic 2: Backer Pledging & Escrow** *(FR-003, UC-02, UC-04)* | `SSCP-5` | Escrow Pledge Processing | **As a** Campaign Backer, **I want to** authorize my payment via a PCI-DSS compliant gateway into platform escrow, **So that** my funds are protected until milestones are formally verified. | High | 8 | Sprint 1 |
| **Epic 3: Milestone Review** *(FR-004, UC-05, UC-06)* | `SSCP-6` | Evidence Submission | **As a** Student Founder, **I want to** upload completion evidence (code repos, demo links, reports) for a due milestone, **So that** the faculty committee can evaluate actual progress. | High | 5 | Sprint 2 |
| **Epic 3: Milestone Review** *(FR-004, UC-06)* | `SSCP-7` | Faculty Review & Decision | **As a** Faculty Committee Member, **I want to** inspect submitted deliverables and record an Approve or Reject decision with comments, **So that** fund disbursement is justified by verified work. | High | 5 | Sprint 2 |
| **Epic 3: Milestone Review** *(FR-004, UC-06)* | `SSCP-8` | Revision Workflow | **As a** Student Founder, **I want to** review faculty rejection feedback and resubmit revised evidence before the deadline, **So that** I can rectify deficiencies without forfeiting the campaign. | Medium | 3 | Sprint 2 |
| **Epic 4: Tranche Disbursement** *(FR-001, UC-07, UC-04)* | `SSCP-9` | Escrow Balance Check | **As a** System Service, **I want to** verify that the escrow balance is sufficient and conditions are satisfied prior to release, **So that** fund releases never exceed collected pledges. | High | 3 | Sprint 2 |
| **Epic 4: Tranche Disbursement** *(FR-001, UC-07, UC-04)* | `SSCP-10` | Automated Disbursement | **As a** Student Founder, **I want** approved milestone funds to be transferred directly to my linked bank account, **So that** I have the required capital to execute the next project phase. | High | 8 | Sprint 2 |
| **Epic 5: Automated Notifications** *(FR-005, UC-08)* | `SSCP-11` | Multi-Channel Alerts | **As a** Student Founder and Backer, **I want to** receive automated email and in-app alerts whenever a milestone is approved, rejected, or a tranche is released, **So that** I stay informed within 5 minutes of each event. | Medium | 5 | Sprint 2 |
| **Epic 5: Automated Notifications** *(FR-005, UC-08)* | `SSCP-12` | Public Campaign Ledger | **As a** Campaign Backer, **I want to** view a transparent milestone timeline and fund disbursement ledger, **So that** I can audit venture progress and fund allocation in real time. | Low | 3 | Sprint 2 |

---

## 🎯 2. Story Point Estimation & Planning Poker Rationale

Story points were estimated using the **Fibonacci Sequence (1, 2, 3, 5, 8, 13)** through a simulated team **Planning Poker** exercise.

### Why Fibonacci Scale?
The exponential growth of the Fibonacci series models the non-linear increase in **uncertainty, technical complexity, and architectural dependencies** as task scope expands:
* **3 Story Points (Low Complexity):** Straightforward validation rules, standard form controls, or read-only database queries (e.g., Campaign duration validation `SSCP-2`, Escrow balance checks `SSCP-9`).
* **5 Story Points (Medium Complexity):** Multi-step workflows requiring database persistence, role-based authorization, and external communications (e.g., Evidence submission `SSCP-6`, Faculty approval state machine `SSCP-7`, Reward tier binding `SSCP-4`).
* **8 Story Points (High Complexity):** High risk and architectural integration requirements involving financial transactions, distributed escrow state synchronization, and PCI-DSS compliance (e.g., Milestone-tranche decomposition `SSCP-3`, Escrow pledge payment authorization `SSCP-5`, Automated banking disbursement `SSCP-10`).

---

## ⚡ 3. Sprint Simulation & Execution

The team completed **2 timeboxed 1-week Sprints**:

### Sprint 1: Campaign Foundation & Escrow Pledging
* **Timebox:** 1 Week (Oct 01, 2026 – Oct 08, 2026)
* **Goal:** Enable student founders to launch campaigns with staged milestone tranches and allow backers to commit pledged funds to secure escrow.
* **Committed Capacity:** 29 Story Points (5 User Stories)
* **Delivered Velocity:** 29 Story Points (100% completion)
* **Board Progress:** All items progressed from `To Do` ➔ `In Progress` ➔ `Done`.

### Sprint 2: Milestone Verification & Disbursement Engine
* **Timebox:** 1 Week (Oct 09, 2026 – Oct 16, 2026)
* **Goal:** Implement the faculty review mechanism, automated tranche release from escrow, and multi-channel backer notifications.
* **Committed Capacity:** 32 Story Points (7 User Stories)
* **Delivered Velocity:** 32 Story Points (100% completion)
* **Board Progress:** All items progressed from `To Do` ➔ `In Progress` ➔ `Done`.

---

## 📉 4. Burndown Chart Analysis

| Metric | Sprint 1 | Sprint 2 |
| :--- | :---: | :---: |
| **Initial Committed Points** | 29 pts | 32 pts |
| **Final Remaining Points** | 0 pts | 0 pts |
| **Sprint Duration** | 7 Days (5 working + 2 weekend) | 7 Days (5 working + 2 weekend) |
| **Average Burn Rate** | 4.14 pts / day | 4.57 pts / day |
| **Trajectory Observation** | Discrete staircase drop; weekend flattening; on-target finish | Mid-sprint plateau during review state machine design; burst completion on Days 5-7 |

---

## 💡 5. Reflection Questions and Answers

### Q1: Did your estimations reflect the actual effort?
> **Yes.** The Planning Poker estimates aligned closely with actual technical effort, although key differences emerged across story point tiers:
> * **Low-point stories (3 pts):** Highly predictable. Standard CRUD operations and input field boundary checks had few unexpected hurdles.
> * **High-point stories (8 pts):** While they were completed on schedule, they required disproportionate cognitive effort. For instance, `SSCP-5` (Escrow Pledge Processing) and `SSCP-10` (Automated Disbursement) involved handling asynchronous payment gateway webhooks, idempotency keys, and transaction rollbacks.
> The Fibonacci scale successfully accounted for this additional risk by forcing the estimate from 5 to 8 points rather than linear scaling.

### Q2: Was your backlog well-prioritized?
> **Yes.** The product backlog was prioritized based on **architectural dependencies** and **MoSCoW criteria**:
> * **Sprint 1** prioritized foundation dependencies (`FR-002` Campaign Creation and `FR-003` Pledging/Escrow). Without campaigns and escrowed pledges, faculty verification and fund disbursement cannot functionally occur.
> * **Sprint 2** completed the verification and release loop (`FR-004` Milestone Review and `FR-001` Tranche Disbursement), followed by audit notifications (`FR-005`).
> This sequence eliminated blocker wait times and delivered a shippable increment at the end of each sprint.

### Q3: How did your simulated sprint align with your plan?
> **The simulated sprints closely matched our planned trajectory**, delivering 100% of committed story points (29 pts in Sprint 1 and 32 pts in Sprint 2) by Day 7.
> In contrast to the continuous diagonal guideline, the actual burndown exhibited a realistic **step-down staircase pattern** reflecting discrete story completions. Both sprints experienced horizontal plateaus during non-working weekend days (Oct 04–05 and Oct 10–11). In Sprint 2, a temporary lag occurred on Day 3 while formalizing the faculty review state machine, but task re-allocation enabled dual story completions on Day 5, restoring alignment with the release plan.

### Q4: What insights did the burndown chart give about your team’s capacity?
> The burndown charts yielded three key operational insights:
> 1. **Velocity Baseline:** A stable team velocity of approximately **29–32 story points per 1-week sprint** was established, giving leadership a reliable forecasting metric for future sprints.
> 2. **Batch Completion vs. Flow:** Large 8-point stories remain "In Progress" for multiple days before dropping, creating sharp vertical drops. Breaking 8-point items into smaller 3-point sub-tasks in future planning will generate smoother flow and reduce sprint-end integration risk.
> 3. **Controlled Scope:** The remaining effort curve hovered closely around the ideal guideline without upward steps (which indicate unmanaged scope creep) or early stalls (which indicate over-commitment).

---

## 🚀 6. Jira Cloud Setup & Instructor Demonstration Guide

To demonstrate the live project on Jira Software to your instructor:

1. **Create Project in Jira:**
   * Select **Software Development** ➔ **Scrum** ➔ **Company-managed project**.
   * **Project Name:** `Student Startup Crowdfunding Platform`
   * **Key:** `SSCP`
2. **Import Backlog via CSV:**
   * Click **Settings (Gear icon)** ➔ **System** ➔ **External System Import** ➔ **CSV**.
   * Upload `Lab-2/Jira_Backlog_Import.csv`.
   * Map fields:
     * `Summary` ➔ `Summary`
     * `Issue Type` ➔ `Issue Type`
     * `Description` ➔ `Description`
     * `Priority` ➔ `Priority`
     * `Story Points` ➔ `Story Points`
     * `Epic Name` ➔ `Epic Name`
     * `Epic Link` ➔ `Epic Link`
     * `Sprint` ➔ `Sprint`
   * Complete import.
3. **Showcase Views:**
   * **Backlog:** Press `E` to toggle the Epic Panel on the left.
   * **Active Sprints:** Open active sprint board to view `To Do`, `In Progress`, and `Done` columns.
   * **Reports:** Navigate to **Reports ➔ Burndown Chart** to demonstrate the velocity curve and non-working day indicators.
