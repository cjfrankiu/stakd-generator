from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔑 Replace with your OpenAI key
openai.api_key = os.environ.get("OPENAI_API_KEY")
print("Loaded API Key:", openai.api_key)

@app.route("/generate", methods=["POST"])
def generate_campaign():
    data = request.json
    brand = data.get("brand")
    product = data.get("product")
    audience = data.get("audience")
    tone = data.get("tone")

    prompt = f"""
You are The Reactor – a fearless, creative strategist known for delivering bold, attention-grabbing marketing campaigns.

Generate a Brand Shock Play using this format:

🧨 Campaign Name: [Creative name]

⚡️ Concept (1-liner): [Explain what it is, quick]

🎬 Execution Steps:
[Bullet 1]
[Bullet 2]
[Bullet 3]

🎯 Why It Works:
[Psych angle, culture tie-in, or emotional hook]

🧠 Optional Twist:
[Extra spice if they want to go all-in]

---

Brand: {brand}
What They Sell: {product}
Audience: {audience}
Tone or Style: {tone}
"""

    try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    idea = response['choices'][0]['message']['content']
    return jsonify({"campaign": idea})
except Exception as e:
    print("🔥 Error during OpenAI call:", str(e))
    return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
