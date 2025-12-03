from openai import OpenAI
import os

# Client uses OPENAI_API_KEY environment variable automatically
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) 

class PromptEngine:
    """Uses GPT-4 to synthesize a high-fidelity image generation prompt."""
    def synthesize(self, brief: str, retrieved: list[str]) -> str:
        """Combines the brief and retrieved prompts into an optimized DALL-E 3 prompt."""
        retrieved_prompts_str = "\n".join([f"- {p}" for p in retrieved])
        
        system_content = (
            "You are an expert Ad Image Prompt Generator. Your task is to generate "
            "a single, optimized, detailed, and visually stunning prompt for DALL-E 3. "
            "Use the 'Brief' as the core instruction and incorporate stylistic elements "
            "from the 'Retrieved Prompts' to maintain brand continuity."
        )

        user_content = (
            f"--- Marketing Brief ---\n{brief}\n\n"
            f"--- Retrieved Successful Prompts for Style Reference ---\n{retrieved_prompts_str}\n\n"
            "Generate the final, single DALL-E 3 prompt now:"
        )
        
        response = client.chat.completions.create(
            # Using GPT-4 turbo for best reasoning
            model="gpt-4-turbo", 
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
        )
        return response.choices[0].message.content