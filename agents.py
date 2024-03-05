from textwrap import dedent
from crewai import Agent
from tools import CustomWriterTool
from crewai_tools import BaseTool
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Instantiate tools
dir_tool = DirectoryReadTool(directory='./software')
file_read_tool = FileReadTool()
web_rag_tool = WebsiteSearchTool()

class DevTeam:
    def __init__(self):
        # Create an instance of the custom writer tool with the output_directory
        self.writer_tool = CustomWriterTool()

    def senior_engineer_agent(self):
        return Agent(
            role='Senior Web Developer',
            goal='Create responsive HTML front-end web pages. You are able to read the current development directory using the dir_tool. You can read the content of existig files using the file_read_tool. These tools will allow you too read existing files, and modify code as requested.',
            backstory=dedent("""\
                You are a Senior Web Developer.
                Your expertise in programming in HTML and JavaScript, using libraries such as JQuery, and BootStrap. You always do your best to
                produce complex, clean, and resusable code, that is well commented."""),
            allow_delegation=False,
            verbose=True,
            memory=False,
            tools=[file_read_tool,dir_tool]
        )

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
            goal='create prefect code, by analyzing the code that is given for errors',
            backstory=dedent("""\
                You are a software engineer that specializes in checking code
                for errors. You have an eye for detail and a knack for finding
                hidden bugs.
                You check for missing imports, variable declarations, mismatched
                brackets and syntax errors.
                You also check for security vulnerabilities, and logic errors"""),
            allow_delegation=False,
            verbose=True,
            memory=False
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role='You are the product owner on a software development scrum team.',
            goal='It is your job to communicate specific requests for new code, features, and modifications to the development team.  You will identify the files that need to be modified, provide clarity for what the acceptance requirements are, and even idenitfy which code blocks are being requested to be modified or added.',
            backstory=dedent("""\
                You feel that programmers always do only half the job, so you are
                super dedicated to making high quality code, delegating specific tasks to the programmers, and providing constuctive feedback."""),
            allow_delegation=True,
            verbose=True,
            memory=True,
            toos=[file_read_tool,dir_tool]
        )
    
    def writer_agent(self):
        return Agent(
        role='To write the final code to files for testing.',
        goal='output the final code to the correct file, with the proper file name and extension. You can view the current files using the dir_tool tool.',
        backstory=dedent("""\
            Your only job is to use the writer_tool to output code to the proper files, overwriting files as needed."""),
        allow_delegation=False,
        verbose=True,
        memory=False,
        tools=[CustomWriterTool()]  # Pass the instance of CustomWriterTool without arguments
    )
