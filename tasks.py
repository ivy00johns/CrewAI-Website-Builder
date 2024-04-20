from textwrap import dedent
from crewai import Task

class WebsiteTasks:
	def basic_design_task(self, agent, website_description):
		return Task(
			description=dedent(f"""
				**Website Design Task**

				Design a basic website based on the following description:
					{website_description}"""),
			agent=agent,
			expected_output="A basic design layout for the website."
		)

	def basic_development_task(self, agent, design_mockups):
		return Task(
			description="Develop a basic website based on the provided design.",
			agent=agent,
			expected_output="HTML, CSS, and JavaScript code for the basic website."
		)

	def basic_qa_task(self, agent, website_code):
		return Task(
			description="Test the basic website to ensure it functions as expected.",
			agent=agent,
			expected_output="A report on the basic website's functionality and any identified issues."
		)

	def design_task(self, agent, website_description):
		return Task(
			description=dedent(f"""
				**Website Design Task**

				**Client Description**
					{website_description}

				**Your Role**
					UI/UX Designer

				**Objective**
					Create a visually appealing and user-friendly design concept for the website. Consider the target audience, website goals, and overall user experience. 

				**Deliverables**
				* Low-fidelity wireframes or sketches outlining the website layout and structure.
				* High-fidelity mockups showcasing the visual design, including colors, typography, and imagery.
				* A brief explanation of your design choices and how they address the client's needs and user experience considerations."""),
			agent=agent,
			expected_output="A description of the website design, including visual elements and user interface layout."
		)

	def frontend_development_task(self, agent, design_mockups):
		return Task(
			description=dedent("""\
				**Frontend Development Task**

				**Design Mockups**
					(Please refer to the provided design mockups.)

				**Your Role**
					Senior Frontend Engineer

				**Objective**
					Develop the frontend of the website using HTML, CSS, and JavaScript, bringing the provided design mockups to life. Ensure the website is responsive, interactive, and follows best practices for performance and accessibility.

				**Deliverables**
				* Clean and well-structured HTML, CSS, and JavaScript code.
				* Implementation of interactive elements and functionalities as per the design specifications.
				* A responsive layout that adapts seamlessly to different screen sizes and devices."""),
			agent=agent,
			expected_output="The HTML, CSS, and JavaScript code for the website's frontend, implementing the provided design."
		)

	def frontend_qa_task(self, agent, website_code):
		return Task(
			description=dedent("""\
				**Frontend Quality Assurance Task**

				**Website Code**
					(The frontend code will be provided for testing.)

				**Your Role**
					Frontend Quality Assurance Engineer

				**Objective**
					Thoroughly test the frontend of the website to identify and report any bugs, usability issues, or inconsistencies with the design specifications.

				**Deliverables**
				* A detailed report outlining any identified issues, including steps to reproduce them.
				* Screenshots or video recordings demonstrating the problems encountered.
				* Recommendations for fixing the issues and improving the overall quality of the frontend."""),
			agent=agent,
			expected_output="A report detailing the results of the frontend testing, including any identified issues and recommendations for improvement."
		)
