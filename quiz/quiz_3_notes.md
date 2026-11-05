# DATASCI 350 - Quiz 3
## AI-Assisted Programming and Cloud Computing

### Quiz Day Setup
- **Fork** the quiz repository on the GitHub website
- Open the terminal and clone the fork
    - cd ~/Desktop
    - git clone https://github.com/mollym425/datasci350-quiz03.git
- In VS Code: File --> Add Folder to Workspace --> select quiz folder
- In the terminal, move to the quiz folder and check:
    - cd ~/Desktop/datasci350-quiz03
    - pwd
    - git status
- Open **commands.txt** in VS Code or create it with:
    - touch commands.txt
- Commit and push all required files, including commands.txt, then submit the fork’s URL on Canvas

## Local Models and Ollama (Lecture 12 & Assignment 6)

### Ollama Basics
- **ollama --version** - tells you the version of ollama software (program that runs the model)
- **ollama run llama3.2:1b** - run the model
- **ollama ls** - list what you have downloaded
- **ollama ps** - show what is downloaded in memory now
- **ollama show llama3.2:1b** - print's a model's details
- **ollama stop llama3.2:1b** - unload the model from memory
- **ollama rm llama3.2:1b** - remove the model from disk
- **>>> /set parameter <name> <value>** - change a setting
- **>>> /set parameter temperature 0** - changes the temperature of the model
- **>>> /set think/nothink** - reasoning on/off (thinking models only)
- **>>> /show parameters** - show what you changed
- **>>> /clear** - forget the conversation so far
- **>>> /bye** - leaves  

### Creating a Chatbot
- **System prompt parts** - persona, task, context, format
- **Modelfile** - plain text file, no extension
```{text}
FROM llama3.2:1b

PARAMETER temperature 1.2

SYSTEM """
# Persona
You are Coach, an overly motivational and enthusiastic 
basketball coach.

# Task
Your primary task is to answer the user's questions.

# Context
The user is your confused athlete asking general questions 
about the world.

# Format
Respond to every request using sports analogies.
Address the user as 'Champ'.
"""

MESSAGE user What is a Git branch?
MESSAGE assistant Champ, a Git branch is like a separate practice court where you can try new plays without affecting the main game!

MESSAGE user Can you check my inbox?
MESSAGE assistant Champ, I can't access your inbox. You're the player with the ball here, so open your email app to check!
```

- **ollama create chatbotname -f modelfile** - build the model
- **ollama run chatbotname** - run the model
- **PARAMETER num_ctx 4096** - sets how much conversation the model remembers
- **PARAMETER repeat_penalty 1.3** - discourages repeated phrases
- **ollama run llama3.2:1b --format json \ "question"** - valid JSON every time

## Calling Models through an API (Lecture 14 & Assignment 7)
- **Calling Ollama from Python:**
```{text}
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # the library insists on one; Ollama ignores it
)

response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        # user: the question you are asking
        {"role": "user", "content": "Why is the sky blue?"},
    ],
    temperature=0,
    max_tokens=40,
)

print(response.choices[0].message.content)
print()  # an empty line, to separate the answer from the usage line
print(response.usage)
print()
print(response.choices[0].finish_reason) # says why the model stopped
```

- **"finish_reason:" "length"** - it hit max_tokens, and the text is cut off mid-sentence 
- **"finish_reason:" "stop"** - model finished

## Cloud Computing (Lecture 16 & Lecture 17)
- **Saas (Software as a Service)** - a finished application, used through your browser; ex: Gmail, Microsoft365
- **PaaS (Platform as a Service)** - a place to run code you wrote; ex: GitHub Pages, Google App Engine
- **FaaS (Function as a Service)** - you run code without setting up or managing servers; you pay only for the time your function runs; ex: AWS Lambda
- **IaaS (Infrastructure as a Service)** - you rent virtual machines, storage, and networking over the internet; you pay for the resources you use; ex: AWS EC2
- **Amazon EC2** - rents you virtual machines, called instances
    - Sign into AWS Console
    - Search EC2 and click dashboard
    - Click "Launch Instance"
    - Enter a name
    - Click Ubuntu under "Application and OS Images"
    - Under "Network Settings," click allow on everything
    - Click "Launch Instance"
- Logging in to the EC2 instance through SSH
    - Click "Connect to Instance"
    - Open terminal on Desktop
    - Copy, paste, and run the 2 commands from the page
    - Type "yes" in the terminal and hit enter
- **sudo apt update** - refresh the package list
- **sudo apt upgrade** - install the latest updates
- **sudo apt install package/software** - install python, jupyter-notebook, etc.
- **scp -i key.pem myfile ubuntu@public-dns:~** - moves file from laptop to instance (DNS copied from instance page on AWS Console)
- **scp -i key.pem ubuntu@public-dns:~/myfile .** - moves file from instance to laptop (still run on mac)
- **ssh -i datasci350b.pem ubuntu@<public-DNS> -L 8000:localhost:8888** - connect with port forwarding