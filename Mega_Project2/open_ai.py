from groq import Groq


# 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 --> API key free.
# Initialize Groq client with your API key
client = Groq(api_key="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")

command = '''
[10:37 PM, 8/26/2025] Fahad Khalil: yes
[10:37 PM, 8/26/2025] Fahad Khalil: you
[10:37 PM, 8/26/2025] Fahad Khalil: what
[10:37 PM, 8/26/2025] Fahad Khalil: are
[10:37 PM, 8/26/2025] Fahad Khalil: you
[10:37 PM, 8/26/2025] Fahad Khalil: doing
[12:15 PM, 8/27/2025] Self: hello
[12:15 PM, 8/27/2025] Self: how are you
'''

# Correct messages format
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are Naruto from Pakistan. You speak English, and Urdu(but in english typing) and remeber dont reply by typing pure urdu okay!. You are also a coder. Analyze the chat history and respond like Naruto. Just reply the message dont go in deep and straight forward."},
        {"role": "user", "content": command}
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
)

# Print streaming response
for chunk in completion:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
