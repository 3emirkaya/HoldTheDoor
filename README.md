# 🚪 Hold the Door - 2D Zombie Tower Defense

[![Course](https://img.shields.io/badge/Course-YAM415%20Game%20Programming-blue.svg)](https://www.izu.edu.tr)
[![Group](https://img.shields.io/badge/Group-G01%20Aggro%20Games-red.svg)](#-development-team--roles)
[![Engine](https://img.shields.io/badge/Unity-6%20LTS%20(6000.x)-black.svg?logo=unity)](https://unity.com)
[![Render Pipeline](https://img.shields.io/badge/Pipeline-URP%202D-green.svg)](#-technical-specifications)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20WebGL-orange.svg)](#-technical-specifications)

> *"Stand your ground, spend your scrap wisely, and hold the wooden gate until dawn!"*

---

## 📌 Project Overview
**Hold the Door** is a 2D top-down tower defense strategy game developed for the **YAM415 Game Programming** course at **Istanbul Sabahattin Zaim University (İZÜ)**.

In an apocalyptic frontier outpost, aggressive zombie hordes are relentlessly pushing to breach the last defensive wooden fence gate (**"The Door"**). Players strategically construct and manage a triad of specialized defense turrets along the path, manage scrap currency, and hold the perimeter through progressively difficult zombie waves.

---

## 👥 Development Team & Roles (Aggro Games - Group 01)

| Name | Student ID | Project Role | Responsibilities |
| :--- | :--- | :--- | :--- |
| **Emir KAYA** | `030722013` | **CEO & Systems Lead** | Project management, system architecture, core game loop |
| **Ömer Faruk YÜCE** | `030722017` | **Lead Game Designer** | Game balance, difficulty pacing, zombie archetypes & wave design |
| **Metehan GERGİN** | `0307221017` | **Lead Programmer** | Mechanics scripting, tower shooting logic, UI implementation |

---

## 🎮 Core Game Mechanics

### 🏰 Defensive Towers Triad
1. **Single-Target Sentry (`100 Scrap`):**
   - Rapid-fire mechanical turret with medium range and balanced damage output. Ideal for consistent frontline defense.
2. **Sniper Tower (`175 Scrap`):**
   - High-caliber, extreme-range precision rifle. Features a slow reload time but deals devastating single-shot damage—essential against heavy **Tank Zombies**.
3. **Shotgun Tower (`150 Scrap`):**
   - Short-range defensive bunker firing a wide conical pellet spread. Delivers high burst Area-of-Effect (AoE) damage to shred swarms of **Runner Zombies**.

### 🧟 Zombie Types
- **Walker Zombie:** Standard speed and medium health; forms the bulk of early waves.
- **Runner Zombie:** Rapid sprint speed, low health; attempts to slip past defenses in packs.
- **Tank Zombie:** Massive health pool and high gate-attack damage; slow movement speed.

### 💰 Economy & Win/Loss Conditions
- **Starting Scrap:** $250$ scrap money.
- **Gate Health:** $20 / 20$ HP.
- **Victory:** Successfully eliminate all scheduled waves while Gate Health remains $\ge 1$.
- **Defeat:** Gate Health reaches $0$ and the wooden barricade breaks.

---

## 🛠️ Technical Specifications

- **Engine:** Unity 6 LTS (6000.3 / 6000.5)
- **Render Pipeline:** Universal Render Pipeline (URP 2D)
- **Target Platform:** Windows Standalone (64-bit) & WebGL (Modern Web Browsers)
- **Language / Architecture:** C# with modular decoupled Managers (`GameManager`, `WaveManager`, `EconomyManager`, `PathManager`)
- **Physics & Collisions:** 2D Physics Triggers & Object Pooling for projectiles and enemies

---

## 📂 Repository Structure

```text
HoldTheDoor/
├── .gitignore                      # Tailored Unity and LaTeX ignore rules
├── README.md                       # Main project documentation and overview
├── compute_hashes.py               # Midterm checksum generator (CRC32, MD5, SHA-1)
├── HoldTheDoor_Document/           # Official LaTeX Game Concept & Design Document (GCDD)
│   ├── main.tex                    # LaTeX root file
│   ├── style.tex                   # Academic styling and formatting macros
│   ├── figures/                    # Architectural diagrams, concept art, and logos
│   └── sections/                   # Modular document sections (2.1 to 4.12, Appendices A–E)
├── YAM415_G01_Midterm/             # Official Midterm submission package
│   ├── AI_Logs/                    # Detailed AI interaction logs (Antigravity ChatLog)
│   └── (PDFs & Checksums)
└── YAM415_G01_ProjectPlan.xlsx     # Work package breakdown & person-month distribution (WP1–WP6)
```

---

## 🌿 Version Control & Branch Strategy

As declared in Section 4.10 of our Technical Document:
- **`main`**: Production-ready, stable submission releases only.
- **`develop`**: Primary integration branch for active development and gameplay testing.
- **`feature/*`**: Isolated task branches for specific features (e.g. `feature/sentry-bullet-pool`, `feature/zombie-fsm`).

> **AI Assistance Declaration:**  
> AI tools (Google Antigravity / Gemini) are used in compliance with the course syllabus for planning, LaTeX structuring, and architectural consultation. All code or document commits assisted by AI are marked with the tag:  
> `AI-assisted: Google Antigravity`

---

## 🚀 How to Run the Project (For Evaluators)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/3emirkaya/HoldTheDoor.git
   ```
2. **Open in Unity Hub:**
   - Launch Unity Hub $\rightarrow$ click **Add** $\rightarrow$ select the project directory.
   - Ensure Unity 6 LTS is selected.
3. **Build & Run:**
   - Open `0_MainMenu.unity` in the Scenes folder.
   - Press **Play** in editor or navigate to `File -> Build Settings -> Build and Run`.

---

© 2026 **Aggro Games**. Developed for YAM415 Game Programming, Istanbul Sabahattin Zaim University.
