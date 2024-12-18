import streamlit as st
import google.generativeai as genai

# Function to get skills from Gemini API based on job title
def get_skills_from_gemini(job_title):
    prompt = f"""
    Based on the job title '{job_title}', generate a comprehensive list of skills required for the role. 
    The skills should be categorized into:
    1. Technical Skills
    2. Soft Skills
    Make sure to include relevant skills based on the job title and provide a brief explanation where necessary.
    
    """

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([prompt])
    return response.text

# Main Streamlit app
def app():
    # Configure the API key
    genai.configure(api_key="AIzaSyB46sAin3C4rTXYCmXkmfQho4fzNUMH6Rw")

    # Streamlit page layout
    st.title("Skills Generator for Job Roles")

    # Input field for job title
    job_title = st.text_input("Enter the job title:", "")

    # Button to generate skills
    if st.button("Generate Skills"):
        if job_title:
            # Fetch skills from the Gemini API
            skills = get_skills_from_gemini(job_title)
            st.write(skills)
        else:
            st.warning("Please enter a job title.")

if __name__ == "__main__":
    app()
