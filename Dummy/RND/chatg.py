import openai

# Set your OpenAI API key
openai.api_key = "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"

# Generate a response from GPT-3
prompt = "Once upon a time"
response = openai.Completion.create(
    engine="davinci",  # Choose the engine (davinci, curie, etc.)
    prompt=prompt,
    max_tokens=50  # Adjust the number of tokens in the response
)

print(response.choices[0].text.strip())
