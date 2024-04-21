from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import WebsiteTasks
from agents import FrontendAgents

# Initialize tasks and agents
tasks = WebsiteTasks()
agents = FrontendAgents()

print("## Welcome to the Website Development Crew")
print("-" * 40)

website_type = input("Choose website type (1 - Basic, 2 - Complete): ")

if website_type == "1":
	basic_website_description = input("Describe the basic website you want to create:\n")
	design_task = tasks.basic_design_task(agents.ui_ux_designer_agent(), basic_website_description)  
	development_task = tasks.basic_development_task(agents.senior_frontend_engineer_agent(), design_task.output)
	qa_task = tasks.basic_qa_task(agents.frontend_qa_engineer_agent(), development_task.output)
elif website_type == "2":
	website_description = input("Describe the complete website you want to create: What is its purpose and target audience?\n")
	design_task = tasks.design_task(agents.ui_ux_designer_agent(), website_description)
	development_task = tasks.frontend_development_task(agents.senior_frontend_engineer_agent(), design_task.output)  
	qa_task = tasks.frontend_qa_task(agents.frontend_qa_engineer_agent(), development_task.output)
else:
	print("Invalid choice. Exiting.")
	exit()

# Create Crew
website_crew = Crew(
	agents=[
		agents.ui_ux_designer_agent(),
		agents.senior_frontend_engineer_agent(),
		agents.frontend_qa_engineer_agent()
	],
	tasks=[
		design_task,
		development_task,
		qa_task
	],
	verbose=True
)

final_result = website_crew.kickoff()

# Print results
print("\n\n########################")
print("## Website Development Summary")
print("########################\n")

print("**Design Phase Output:**")
print(design_task.output)

print("\n**Development Phase Output:**")
print(development_task.output)

print("\n**QA Phase Output:**")
print(qa_task.output)
