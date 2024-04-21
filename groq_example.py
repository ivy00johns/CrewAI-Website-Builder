import os
from crewai import Agent, Task, Crew, Process

os.environ['OPENAI_API_BASE'] = "https://api.groq.com/openai/v1"
os.environ['OPENAI_MODEL_NAME'] = "llama3-70b-8192"
os.environ['OPENAI_API_KEY'] = "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"

email = "Nigerian Prince sending some gold."
# email = "Hey, your neighbor John here, your house seems to be on fire. This is NOT A JOKE!"

classifier = Agent(
	role = "Email classifier",
	goal = "Accurately classify emails based on their importance. Give every email one of these ratings: important, casual, or spam.",
	backstory = "You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid to give emails bad rating if they are not important. Your job is to help the user manage their inbox.",
	verbose = True,
	allow_delegation = False
)

responder = Agent(
	role = "Email responder",
	goal = "Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal response, if the email is rated 'casual' write a casual response, if the email is rated 'spam' ignore the email. No matter what, be very concise.",
	backstory = "You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance will be provided to you by the 'classifier' agent.",
	verbose = True,
	allow_delegation = False
)

classify_email = Task(
	description = f"Classify the following email: '{email}",
	agent = classifier,
	expected_output = "One of these three options: 'important', 'casual', or 'spam'"
)

respond_to_email = Task(
	description = f"Raspond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
	agent = responder,
	expected_output = "A very concise response to the email based on the importance provided by the 'classifier' agent."
)

crew = Crew(
	agents = [classifier, responder],
	tasks = [classify_email, respond_to_email],
	verbose = 2,
	process = Process.sequential
)

output = crew.kickoff()
print(output)
