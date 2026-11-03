"""Ask your own model a question, from Python instead of the terminal.

Needs Ollama running and llama3.2:1b pulled, both from lecture 12.

    pip install openai
    python3 ask_local.py
"""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # the library insists on one; Ollama ignores it
)

questions = ["Who was the first U.S. president?",
             "Why does the ocean have waves but bays don't have them?", 
             "Why do trees sometimes have green leaves, sometimes have orange or red leaves, sometimes grow flowers, and sometimes have no leaves?"]

for question in questions:
    response = client.chat.completions.create(
        model="llama3.2:1b",
        messages=[
            # user: the question you are asking
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    print(response.choices[0].message.content)
    print()  # an empty line, to separate the answer from the usage line
    print(response.usage)
