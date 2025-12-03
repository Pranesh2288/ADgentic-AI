from .brief_loader import BriefLoader
from .retriever import PromptRetriever
from .prompt_engine import PromptEngine
from .image_generator import ImageGenerator

class Pipeline:
    """The main orchestration class for the ADgentic AI workflow."""
    def run(self, brief_path: str) -> str:
        print("1. Loading Brief...")
        brief = BriefLoader().load(brief_path)
        
        print("2. Retrieving successful prompt patterns via RAG...")
        retrieved = PromptRetriever().query(brief)
        
        # Simple check for demo purposes
        if not retrieved:
            print("   (Warning: No retrieved prompts found in ChromaDB. Using brief only.)")
        
        print("3. Synthesizing optimized DALL-E 3 prompt with GPT-4...")
        prompt = PromptEngine().synthesize(brief, retrieved)
        print(f"   [Generated Prompt: {prompt[:80]}...]")
        
        print("4. Generating image with DALL-E 3...")
        image_url = ImageGenerator().generate(prompt)
        
        return image_url