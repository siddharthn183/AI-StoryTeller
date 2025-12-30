from src.pipeline import run_pipeline

if __name__ == "__main__":

    # Input type could be anything(File or Text), Here we use Text for simplicity
    source_story = """
    Romeo and Juliet fall in love despite family rivalry,
    and tragedy follows from loyalty and miscommunication.
    """
    
    target_world = "futuristic AI research labs"

    final_story, meta, bp = run_pipeline(source_story, target_world)

    print("\n===== FINAL STORY =====\n")
    print(final_story)

    print("\n===== INTERMEDIATE DATA =====\n")
    print(meta)

    print("\n===== BLUEPRINT =====\n")
    print(bp)
