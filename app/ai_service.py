from dotenv import load_dotenv
from google import genai
import json

load_dotenv()
client = genai.Client()


def extract_required_skills(job_description: str) -> list[str]:

    prompt = f"""
    Extract only technical skills from the following job description.

    Return the result as a JSON array of strings.
    Do not include explanations or Markdown formatting.

    Job description:
    {job_description}
    """

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    skills = json.loads(interaction.output_text)
    return skills