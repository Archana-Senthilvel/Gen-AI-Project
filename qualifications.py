import streamlit as st
import google.generativeai as genai

# Function to generate job description based on job title
def get_job_description_from_title(job_title):
    prompt = f"""
    Based on the job title '{job_title}', generate a detailed qualifications needed for this job title including:
    - Qualifications
    
    The qualifications should be clear, concise, and relevant to the given job title.
    """

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([prompt])
    return response.text

# Main Streamlit app
def app():
    # Configure the API key
    genai.configure(api_key="AIzaSyB46sAin3C4rTXYCmXkmfQho4fzNUMH6Rw")

    # Streamlit page layout
    st.title("Job Description Generator from Job Title")

    # Input field for job title
    job_title = st.text_input("Enter the job title:", "")

    # Button to generate job description
    if st.button("Generate Job Description"):
        if job_title:
            # Fetch job description from the Gemini API
            job_description = get_job_description_from_title(job_title)
            st.write(f"Generated Job Description:\n\n{job_description}")
        else:
            st.warning("Please enter a job title.")

if __name__ == "__main__":
    app()
