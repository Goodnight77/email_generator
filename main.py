#from langchain_community.llms import Ollama 
from crewai import Agent , Task , Crew , Process
import os 
#model = Ollama(model= 'mistral')


os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'  
os.environ["OPENAI_API_KEY"] ='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'

User_Name= 'Mohamed Arbi'
email= 'bonjour mr adel , merci pour avoir consacree une partie de votre temps precieux pour notre stage mais je regrette de vous annoncer que je quitte'
is_verbose= True
classifier = Agent(
    role= "email classifier", 
    goal = "accuratly classify emails based on their importance . give every email one of these ratings: important, casual or spam", 
    backstory = "You are an AI assistant whose only job is to classify emails accuratly and honestly .Do not be afraid to give emails bad ratings if they are not important. your job is to help the user manage their inbox",
    verbose = True, 
    allow_delegation = False, 
)

responder= Agent(
    role= "email responder",
    goal = f"based on the importance of the email, respond to emails but to not mention that you are an ai assistant in the email answer as if you are the userand his name is '{User_Name}'. if the email is rated 'important' write a formal response , if the email is rated 'casual' write a casual response, and if the email is rated 'spam' ignore the email. no matter what, be very concnise.",
    backstory = "You are an AI assistant whose only job is to write short repoonses to emails based on their importance. the importance will be provided to you by the 'classifier' agent",
    verbose = True,
    allow_delegation = False,

)


classify_email = Task(
    description= f"classify the following email: '{email}' based on the importance provided by the 'classifier' agent", 
    agent= classifier, 
    expected_output = "one of these three options 'important', 'casual', or 'spam'",

)

respond_to_email= Task(
    description= f"respond to the email '{email}' based on the importance provided by the 'classifier' agent.", 
    agent= responder,
    expected_output = "a very concise response to the email based on the importance provided by the 'classifier' agent.",

)

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_email, respond_to_email],
    verbose= 2, 
    process = Process.sequential
)

output = crew.kickoff()
print(output)


