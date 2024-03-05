from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import DevTasks
from agents import DevTeam

def build_page_code():
    tasks = DevTasks()
    agents = DevTeam()

    print("## Welcome to the page_code Crew")
    print('-------------------------------')
    page_code = input("What is the page code you would like to build?\n")

    # Create Agents
    senior_engineer_agent = agents.senior_engineer_agent()
    qa_engineer_agent = agents.qa_engineer_agent()
    chief_qa_engineer_agent = agents.chief_qa_engineer_agent()
    writer_agent = agents.writer_agent()

    # Define the expected output for the page code task
    expected_output = "Implement the page code with appropriate mechanics."

    # Create Tasks
    code_page_code = tasks.code_task(senior_engineer_agent, page_code, expected_output)
    review_page_code = tasks.review_task(qa_engineer_agent, page_code, expected_output)
    approve_page_code = tasks.evaluate_task(chief_qa_engineer_agent, page_code, expected_output)
    write_page_code = tasks.evaluate_task(writer_agent, page_code, expected_output)

    # Create Crew responsible for Copy
    crew = Crew(
        agents=[
            senior_engineer_agent,
            qa_engineer_agent,
            chief_qa_engineer_agent,
            writer_agent,
        ],
        tasks=[
            code_page_code,
            review_page_code,
            approve_page_code,
            write_page_code
        ],
        verbose=True
    )

    # Kick off the tasks
    page_code_result = crew.kickoff()

    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("final code for the page code:")
    print(page_code_result)

# Loop to continuously ask if there's anything else to do
while True:
    build_page_code()
    # Ask if the user wants to continue
    continue_input = input("\nWould you like to build another page code? (yes/no): ").lower()
    if continue_input == 'no':
        break  # Exit the loop if the input is 'no'
