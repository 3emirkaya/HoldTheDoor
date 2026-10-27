# YAM415 Game Programming - AI Interaction & Assistance Log
**Course:** YAM415 Game Programming  
**University:** Istanbul Sabahattin Zaim University  
**Group Code:** G01  
**Group Name:** Aggro Games  
**Members:** Emir KAYA (030722013), Ömer Faruk YÜCE (030722017), Metehan GERGİN (0307221017)  
**Game Title:** Hold the Door  
**AI Assistant Tool:** Google Antigravity (Model: Gemini 3.8 Flash)  
**Session Date:** 27.10.2026  
**Allowed Usage Level:** Level 2 - Editing Support (Ideas, planning, language and spelling support)

---

## 1. Summary of AI Assistance
In accordance with Istanbul Sabahattin Zaim University YAM415 Game Programming Midterm Announcement (Section 7 - AI Use Policy):
1. **Purpose:**
   - Structuring the Game Concept and Design Document (GCDD) according to the official `YAM415_Game_Document_Template_v2026_LaTeX` template.
   - Assisting in mathematical balance curves and matrix structuring for Tower Defense mechanics (Archer, Bombard, Frost, Barracks vs Goblin, Orc, Brute, Boss).
   - Drafting the system flowchart and software architecture models in native TikZ format.
   - Inspecting the Midterm Submission requirements, deadlines, file naming schemes, and checksum verification rules.
2. **Review & Verification:**
   - All generated texts, mechanical values, and architectural diagrams were thoroughly verified, modified, and validated by the team members (Emir KAYA, Ömer Faruk YÜCE, Metehan GERGİN).
   - Core decisions, game vision, rules, lore, and task allocations remain 100% authored and approved by Aggro Games.

---

## 2. Interaction Transcript Summary

### Interaction 1: Project Proposal & Theme Analysis
- **User Prompt:** Submitted the approved YAM415 Game Programming Project Proposal for "Hold the Door" (2D Tower Defense Strategy).
- **Assistance Provided:** Analyzed the inspirations (*Kingdom Rush, Plants vs. Zombies, Bloons TD 6, Thronefall*) and proposed core system decoupling (GameManager, EconomyManager, WaveManager, WaypointPath, Tower targeting, Enemy FSM).

### Interaction 2: LaTeX Game Document Template Integration
- **User Prompt:** Requested a complete document based on the `YAM415_Game_Document_Template_v2026_LaTeX.zip` template in a new folder.
- **Assistance Provided:** Extracted template, adapted `main.tex`, populated `2-concept-document.tex`, `3-design-document.tex`, `4-technical-document.tex`, created native TikZ diagrams for `7-appendix-c.tex` (Flowchart) and `8-appendix-d.tex` (Architecture), and drafted the `6-appendix-b.tex` Game Matrix and `9-appendix-e.tex` AI Use Declaration.

### Interaction 3: Midterm Submission Announcement Analysis
- **User Prompt:** Provided the 4-page midterm submission announcement document for analysis.
- **Assistance Provided:** Extracted critical deadlines (31.10.2026 14:00 printed in EGB02, 23:59 on OYS), printed submission requirements (all members present, signing every page by hand, hand-written Declaration of Originality), hash calculation procedures (CRC32, MD5, SHA-1), and project plan formatting.

### Interaction 4: Project Plan & Group Code Configuration
- **User Prompt:** Provided group code `G01`.
- **Assistance Provided:** Configured `G01` across `main.tex` and documents, created the `YAM415_G01_Midterm` packaging structure, populated `YAM415_G01_ProjectPlan.xlsx` with balanced person-month allocations across WP1–WP6, and prepared the Declaration of Originality templates with PowerShell hash generation scripts.

### Interaction 5: Core Game Design Customization (Zombies & Three-Tower Triad)
- **User Prompt:** Redefined the exact core game design:
  - 3 Towers: (1) Single-Target Sentry (high damage, single target), (2) Sniper Tower (extreme range, massive damage, slow reload), (3) Shotgun Tower (short range, wide conical AoE spread).
  - 3 Zombie Archetypes: (1) Tank Zombie (high health, slow), (2) Runner Zombie (low health, fast), (3) Walker Zombie (balanced median).
  - Environment: Left-to-right path leading to a wooden fence gate on the far right ("The Door").
- **Assistance Provided:** Updated Sections 2, 3, 4, Appendix B (Game Balance Matrix), and Appendix C/D diagrams to reflect this design with mathematical consistency and academic formatting.

### Interaction 6: Gameplay Outline Alignment & Difficulty Mode Calibration
- **User Prompt:** Aligned Section 2.7 Game Play with the mandatory 11-item outline from the course template; incorporated cinematic intro with survivor holding the door, 250 starting scrap, 20/20 fence health, and calibrated Normal (Medium) vs. Hard modes (with enhanced zombie health, speed, and damage).
- **Assistance Provided:** Restructured Section 2.7 strictly according to the 11 outline headings (Opening, Options, Story, Modes, Elements, Levels, Controls, Winning, Losing, End, Why is all this fun), simplified language to natural undergraduate English (B1/B2), and updated project archives.

