from textwrap import dedent
from crewai import Task

class DevTasks():
    def code_task(self, agent, page_code, expected_output):
        return Task(
            description=dedent(f"""You will create a page_code using HTML and JavaScript, these are the instructions:

            Instructions
            ------------
            {page_code}

            Your Final answer must be the full HTML and JavaScript code, only the HTML and JavaScript code and nothing else.
            """),
            agent=agent,
            expected_output=expected_output
        )

    def review_task(self, agent, page_code, expected_output):
        return Task(
            description=dedent(f"""\
                You are helping create a page_code using HTML and JavaScript, these are the instructions:

                Instructions
                ------------
                {page_code}

                Using the code you got, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your Final answer must be the full HTML and JavaScript code, only the HTML and JavaScript code and nothing else.
                """),
            agent=agent,
            expected_output=expected_output
        )

    def evaluate_task(self, agent, page_code, expected_output):
        return Task(
            description=dedent(f"""\
                You are helping create a page_code using HTML and JavaScript, these are the instructions:

                Instructions
                ------------
                {page_code}

                You will look over the code to insure that it is complete and
                does the job that it is supposed to do.

                Your Final answer must be the full HTML and JavaScript code, only the HTML and JavaScript code and nothing else.
                """),
            agent=agent,
            expected_output=expected_output
        )
