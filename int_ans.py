import streamlit as st
import google.generativeai as genai

# Function to generate answers using the Gemini API
def generate_answer(job_title, interview_question):
    """
    Generate an answer to an interview question based on the job title.
    
    Args:
        job_title (str): The job title provided by the user.
        interview_question (str): The interview question provided by the user.

    Returns:
        str: The generated answer.
    """
    prompt = f"""
    You are applying for the role of {job_title}. Provide a professional, detailed, and thoughtful answer to the following interview question:
    
    Question: {interview_question}
    
    Ensure the answer demonstrates relevant skills, experience, and alignment with the job responsibilities.
    only list all the perfect and clear answers for the candidate to answer the interview question. Dont include subheadings.Only use bulletin points.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error generating answer: {e}"

# Main Streamlit app
def main():
    # Configure the Gemini API key
    genai.configure(api_key="AIzaSyB46sAin3C4rTXYCmXkmfQho4fzNUMH6Rw")

    st.title("Interview Answer Generator")
    st.subheader("Generate tailored answers for your interview questions.")

    # Input fields for the user
    job_title = st.text_input("Enter the Job Title (e.g., Software Engineer, Web Developer):")
    interview_question = st.text_area("Enter the Interview Question:")

    # Button to generate an answer
    if st.button("Generate Answer"):
        if not job_title or not interview_question:
            st.warning("Please fill out both fields!")
        else:
            st.info(f"Generating an answer for the job title '{job_title}' and the given question...")
            answer = generate_answer(job_title, interview_question)
            
            if answer.startswith("Error"):
                st.error(answer)
            else:
                st.success("Here's your tailored answer:")
                st.write(answer)

# Run the app
if __name__ == "__main__":
    main()
