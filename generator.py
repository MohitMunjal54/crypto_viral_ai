import subprocess
import json

class Generator:

    def ollama(self, prompt):
        cmd = ["ollama", "run", "llama3", prompt]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def create_ideas(self, patterns):
        prompt = f"""
You are an expert crypto content strategist.
Based on these keywords: {patterns['keywords']}

Generate:
- 5 viral Instagram reel ideas
- 3 YouTube ideas
- 3 Twitter thread ideas

Each idea must include:
- Hook
- Topic
- Unique angle
"""
        output = self.ollama(prompt)
        return output
