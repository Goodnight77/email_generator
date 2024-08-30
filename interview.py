from crewai import Agent , Task , Crew , Process
import os 
import pandas as pd 
import streamlit as st 
os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'  
os.environ["OPENAI_API_KEY"] ='api key here'


st.title("interview email generator")
calendly_link= st.text_input("Calendly link","https://calendly.com/example")
HR_Name= st.text_input("HR Name",'Mohamed Arbi')
job_type= st.text_input("Job Type","AI Engineer")
csv_file = st.file_uploader("upload csv file with candidtes names", type= "csv")
is_verbose= True




if st.button("generate emails"):

    if HR_Name and calendly_link and job_type and csv_file:
        df = pd.read_csv(csv_file)
        names= df['name']


        cols = st.columns(min(3, len(names)))

    for idx, name in enumerate(names): 
        backstory = f"""Write a professional and personalized interview invitation email. Include the candidate’s name {name}, 
                job type {job_type}. Politely invite the candidate to an interview, providing a calendly virtual link {calendly_link}, and expected duration which is 30 minutes. 
                Request that he can choose the spot that he can be available in, and offer to reschedule if needed. 
                Maintain a warm and professional tone throughout, ending with a positive closing. 
                your job is to help the user write emails to invite selected candidates for an interview"""


        interviewer = Agent(
                    role= "email generator", 
                    goal = f"generate emails for the candidate whose name is {name} inviting him for an interview", 
                    backstory= backstory,
                    verbose = True, 
                    allow_delegation = False, 
                )


        generate_email= Task(
                    description= f"generate the email to invite {name} for an interview for the {job_type}",
                    agent= interviewer,
                    expected_output = f"a very concise generated email inviting candidate in warm and professional tone,providing all the details about the meeting, and the calendly link and ending with a positive closing add the sender name {HR_Name}in the end of the email",

                )

        crew = Crew(
                    agents = [interviewer],
                    tasks = [generate_email],
                    verbose= 1, 
                    process = Process.sequential
                )

        result = crew.kickoff()
        print(result)
        email_content = generate_email.output

        col_idx = idx % len(cols)
        with cols[col_idx]:
            #st.subheader(f"email for {name}")
            st.text_area(f"{name}_interview_email", value= str(email_content), height= 200, max_chars= None)

        st.success(f"Generated and saved email for {name}.")
else:
    st.error("Please fill in all the fields and upload the CSV file.")


