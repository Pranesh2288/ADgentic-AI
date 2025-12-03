from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class ImageGenerator:
    """Generates the final image using the DALL-E 3 model."""
    def generate(self, prompt: str) -> str:
        """Generates an image and returns the hosted URL."""
        result = client.images.generate(
            model="dall-e-3", 
            prompt=prompt,
            size="1792x1024", # Standard size for high-quality ad images
            quality="hd",
            n=1
        )
        return result.data[0].url