from langchain.prompts import PromptTemplate
from .llm import llm

generate_prompt = PromptTemplate(
    input_variables=["blueprint", "tone"],
    template="""
Write the complete reimagined story using the blueprint below:

{blueprint}

Maintain tone: {tone}
Avoid stereotypes. Avoid deus ex machina.
Ensure internal world logic is consistent.
Approximate length: 2 page.

Return ONLY the final narrative.
"""
)
generate_runnable = generate_prompt | llm

def generate_story(blueprint, tone):
    return generate_runnable.invoke({
        "blueprint": blueprint,
        "tone": tone
    }).content
