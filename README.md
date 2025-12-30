# 🎬 AI-StoryTeller - An AI-Powered Story Re-Imagination Engine  

The goal of this project is to:

> Preserve the *essence* of a classic/public-domain story  
> while **re-engineering it into a completely new world**  

The result is a working system that:

- breaks stories into structured components  
- maps them into a new world context  
- generates a rewritten story  
- validates ethics, coherence, and narrative stability  
- loops back only when needed  

Built using **Python + LangChain + Gemini LLM**, with small local metadata for logic grounding.

---

## 📁 Repository Contents

| File / Folder | Description |
|--------------|-------------|
| `/src/` | Core pipeline modules (extraction, transformation, generation, validation) |
| `/run.py` | Entry script — runs the full pipeline end-to-end |
| `/data.json` | Local world metadata used for context grounding |
| `/docs/Reimagined_Story.pdf` | Final generated story (assignment deliverable) |
| `/docs/Solution_Documentation.pdf` | Architecture, approach, diagrams, alternatives, and design discussion |
| `README.md` | You are here |

> **Note:** Code is intentionally modular and explainable, demonstrating *system thinking*, not just prompting.

---

## 🚀 Project Goal

This system demonstrates how AI engineers:

- prototype creative systems
- enforce structure around LLMs
- separate logic from creativity
- design reusable, extensible transformations

It showcases:

✔ Prompt engineering  
✔ Chained reasoning  
✔ Retrieval-augmented grounding  
✔ Validation & feedback loops  
✔ Reproducibility over randomness  

---

## 🛠 Tech Stack

- **Python**
- **LangChain**
- **Google Gemini API**
- JSON-based metadata (local retrieval)
- Modular pipeline architecture

---

## The Steps to setup and Run the Codebase is provide in the README.md file inside the Codebase Folder.
