import json
from .utils import load_metadata
from .extractionModule import extract_all
from .transformationModule import transform_story
from .generationModule import generate_story
from .validationModule import validate_story, rewrite_story


def run_pipeline(source_story, target_world):

    print("\n[1/6] Starting Extraction Module...")
    extracted = extract_all(source_story)
    print("     ✔ Extraction complete")

    print("\n[2/6] Loading World Information...")
    metadata = load_metadata().get(target_world.lower(), {})
    print("     ✔ Metadata loaded")

    print("\n[3/6] Starting Transformation Module...")
    blueprint = transform_story(extracted, target_world, metadata)
    print("     ✔ Transformation complete")

    print("\n[4/6] Starting Generation Module...")
    story = generate_story(json.dumps(blueprint), extracted["tone_style"]["tone"])
    print("     ✔ First draft generated")

    print("\n[5/6] Starting Validation Loop...")
    for i in range(3):
        print(f"    Validation attempt {i+1}...")
        review = validate_story(story)

        if review["ok"]:
            print("     ✔ Story approved!")
            print("\n[6/6] Pipeline Complete")
            return story, extracted, blueprint

        print("  Rewriting based on feedback...")
        story = rewrite_story(story, review["rewrite_guidance"])

    print("\n Validation stopped after max iterations.")
    print("[6/6] Pipeline Complete (best effort)")
    return story, extracted, blueprint
