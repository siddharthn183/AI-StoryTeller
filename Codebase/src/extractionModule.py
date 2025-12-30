import json
from langchain.prompts import PromptTemplate
from .llm import llm
from .utils import clean_json
from langchain_core.runnables import RunnableParallel

theme_plot_prompt = PromptTemplate(
    input_variables=["story"],
    template="""
You are a senior story analyst.

Task: extract THEME, MORAL, and PLOT BEATS without inventing new events.

Rules:
- Themes = abstract ideas (love vs duty, betrayal, ambition, sacrifice)
- Moral = implied lesson
- Plot beats must follow real story events
- If unsure, write "unknown"
- RETURN ONLY JSON

Example:
story: "Two rivals fall in love despite warnings."
output:
{{
 "themes": ["forbidden love", "conflict between loyalty and desire"],
 "moral": "Unresolved rivalry destroys what matters most.",
 "plot": {{
   "setup": "Rival factions are introduced.",
   "rising_action": "They begin meeting secretly.",
   "climax": "Their relationship is exposed.",
   "resolution": "It ends in tragedy."
 }}
}}

Now analyze:

story: {story}

Return JSON only:
{{
 "themes": ["..."],
 "moral": "...",
 "plot": {{
   "setup": "...",
   "rising_action": "...",
   "climax": "...",
   "resolution": "..."
 }}
}}
"""
)


characters_prompt = PromptTemplate(
    input_variables=["story"],
    template="""
You are a narrative structure expert. Identify characters and their roles.

Allowed roles:
- protagonist
- antagonist
- support
- mentor

Rules:
- Only include characters clearly mentioned
- Relationships only if implied
- RETURN ONLY JSON

Example:
story: "A rebel challenges a tyrant while guided by a mentor."
output:
{{
 "characters": [
   {{ "name": "rebel", "role": "protagonist" }},
   {{ "name": "tyrant", "role": "antagonist" }},
   {{ "name": "mentor", "role": "mentor" }}
 ],
 "relationships": [
   "rebel opposes tyrant",
   "mentor guides rebel"
 ]
}}

Now analyze:

story: {story}

Return JSON only:
{{
 "characters": [
   {{ "name": "...", "role": "protagonist/antagonist/support/mentor" }}
 ],
 "relationships": ["..."]
}}
"""
)

tone_style_prompt = PromptTemplate(
    input_variables=["story"],
    template="""
You are a literary critic.

Task: determine TONE and NARRATIVE STYLE.

Definitions:
- Tone = emotional feel (tragic, hopeful, tense, melancholic, inspiring, etc.)
- Style = voice (descriptive, poetic, reflective, fast-paced, cinematic, etc.)
- Do not summarize plot.
- RETURN ONLY JSON.

Example:
story: "A lone traveller wanders a ruined city."
output:
{{
 "tone": "melancholic",
 "style": "slow and reflective"
}}

Now analyze:

story: {story}

Return JSON only:
{{
 "tone": "...",
 "style": "..."
}}
"""
)

theme_plot_runnable = theme_plot_prompt | llm
characters_runnable = characters_prompt | llm
tone_style_runnable = tone_style_prompt | llm

parallel_chain = RunnableParallel(
    theme_plot=theme_plot_runnable,
    characters=characters_runnable,
    tone_style=tone_style_runnable,
)

def extract_all(story: str):
    raw = parallel_chain.invoke({"story": story})

    theme_plot = json.loads(clean_json(raw["theme_plot"].content))
    characters = json.loads(clean_json(raw["characters"].content))
    tone_style = json.loads(clean_json(raw["tone_style"].content))

    return {
        "themes": theme_plot["themes"],
        "moral": theme_plot["moral"],
        "plot": theme_plot["plot"],
        "characters": characters,
        "tone_style": tone_style,
    }

