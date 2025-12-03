import argparse
from src.pipeline import Pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", required=True, help="Path to the marketing brief PDF.")
    args = parser.parse_args()

    # NOTE: Ensure your OPENAI_API_KEY environment variable is set
    print("--- Starting ADgentic AI Pipeline ---")
    try:
        url = Pipeline().run(args.brief)
        print("\n✅ Successfully Generated Image URL:")
        print(url)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Tip: Check your API key and file paths.")