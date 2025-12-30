import json
from langchain.prompts import PromptTemplate
from .llm import llm
from .utils import clean_json

validation_prompt = PromptTemplate(
    input_variables=["story"],
    template="""
Validate the story for:

1) cultural sensitivity
2) logic consistency
3) no deus ex machina ending

RETURN ONLY JSON:

{{
 "ok": true/false,
 "issues": ["..."],
 "rewrite_guidance": "..."
}}

Story:
{story}
"""
)

rewrite_prompt = PromptTemplate(
    input_variables=["story", "guidance"],
    template="""
Revise the story only where necessary according to this guidance:

{guidance}

Do NOT change the core blueprint or meaning unless required.

Story:
{story}
"""
)

validation_runnable = validation_prompt | llm
rewrite_runnable = rewrite_prompt | llm


def validate_story(story):
    return json.loads(
        clean_json(
            validation_runnable.invoke({"story": story}).content
        )
    )


def rewrite_story(story, guidance):
    return rewrite_runnable.invoke({
        "story": story,
        "guidance": guidance
    }).content
