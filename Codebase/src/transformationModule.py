import json
from langchain.prompts import PromptTemplate
from .llm import llm
from .utils import clean_json

transform_prompt = PromptTemplate(
    input_variables=["extracted", "target_world", "world_metadata"],
    template="""
Reimagine the story into the new world while preserving core essence.

Story elements:
{extracted}

World metadata (constraints, archetypes, rules):
{world_metadata}

Target world: {target_world}

RETURN ONLY JSON:

{{
 "world_rules": [...],
 "reimagined_characters": {{...}},
 "mapped_conflicts": "...",
 "plot_outline": [...]
}}
"""
)

transform_runnable = transform_prompt | llm

def transform_story(extracted, target_world, metadata):
    return json.loads(
        clean_json(
            transform_runnable.invoke({
                "extracted": json.dumps(extracted),
                "target_world": target_world,
                "world_metadata": json.dumps(metadata)
            }).content
        )
    )
