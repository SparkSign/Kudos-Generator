import random, pyperclip, os, dotenv
from openai import OpenAI

# create a .env file that has OPENAI_API_KEY="Put Your API Key Here" in it and the program should work. 
dotenv.load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

# Variables
fullName = input("Please enter the full name person you would like to make a Kudo for ")
name = fullName.split()[0]
randomNumber = random.randrange(0,5)
kudoLength = random.randrange(3,6)

#dictionaries
awards = ["Be a Winner", "Bring Your A-Game", "Do the Right Thing", "Have Fun", "Make Someone's Day", "Respect Each Other"]
kudoPrompt = [f"Write a kudo about {name} being a winner at work", f"Write a kudo about {name} bringing their A-Game at work", f"Write a kudo about {name} doing the right thing at work", f"Write a kudo about {name} having fun at work", f"Write a kudo about {name} making someone's day at work", f"Write a kudo about {name} respecting their coworkers"]

selectedAward = awards[randomNumber]

print(selectedAward)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"You are an office worker that is professional and positive. You will not exceed {kudoLength} sentences"},
    {"role": "user", "content": f"{kudoPrompt[randomNumber]}"}
  ]
)

print(completion.choices[0].message.content)
pyperclip.copy(completion.choices[0].message.content)