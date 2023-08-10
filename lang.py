import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_text(prompt, max_tokens=50, temperature=0.7):
    response = openai.Completion.create(
        engine="davinci",  # Choose the language model engine
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

# Example prompt
prompt = "Once upon a time"

# Generate text based on the prompt
generated_text = generate_text(prompt)

# Print the generated text
print("Generated Text:")
print(generated_text)
