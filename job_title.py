import streamlit as st
import google.generativeai as genai

# Function to get a suitable job title from the job description
def get_suitable_job_title_from_description(job_description):
    prompt = f"""
    Based on the following job description, analyze and generate the most suitable job title for the role:
    
    Job Description: '{job_description}'
    
    Please suggest all the most relevant job title that perfectly fits the given job description.
    only mention all the job titles only in a bulletin points
    """

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([prompt])
    return response.text

# Main Streamlit app
def app():
    # Configure the API key
    genai.configure(api_key="AIzaSyB46sAin3C4rTXYCmXkmfQho4fzNUMH6Rw")

    # Streamlit page layout
    st.title("Job Title Generator from Job Description")

    # Input field for job description
    job_description = st.text_area("Enter the job description:", "")

    # Button to generate job title
    if st.button("Generate Suitable Job Title"):
        if job_description:
            # Fetch suitable job title from the Gemini API
            job_title = get_suitable_job_title_from_description(job_description)
            st.write(f"Suggested Job Title: {job_title}")
        else:
            st.warning("Please enter a job description.")

if __name__ == "__main__":
    app()
