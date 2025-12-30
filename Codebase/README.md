# AI-StoryTelling

**AI-StoryTelling** is a small pipeline that analyzes an input story, extracts its narrative elements (themes, characters, plot beats, tone), transforms the story to fit a target world, and generates a reimagined narrative using AI-backed LLM via LangChain.

---

## Quick start

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment (Windows example):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install langchain langchain-google-genai python-dotenv
```

4. Create a `.env` file in the project root and add your Google Generative AI credentials. Example:

```
GOOGLE_API_KEY=your_api_key_here
# Or follow langchain-google-genai instructions for the proper auth method
```

5. Run the example pipeline:

```powershell
python run.py
```

You should see the pipeline steps printed and the final reimagined story, extracted metadata, and blueprint.

---

## Project structure 🔧

```
README.md                  # (this file)
run.py                     # example runner that executes the pipeline
src/
  ├─ llm.py                # LLM configuration (langchain-google-genai)
  ├─ extractionModule.py   # extract themes, characters, tone/style, plot beats
  ├─ transformationModule.py# transform extracted elements for a target world
  ├─ generationModule.py   # generate final narrative using the LLM and prompt
  ├─ validationModule.py   # validate and optionally rewrite the story
  ├─ pipeline.py           # orchestrates the full pipeline
  └─ utils.py              # helpers (JSON cleaning, metadata loader)

data/
  └─ data.json             # target world metadata (constraints, rules)

---
