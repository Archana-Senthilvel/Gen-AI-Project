import streamlit as st
import google.generativeai as genai

# Function to generate vision statement based on company name and description
def get_vision_statement(company_name, company_description):
    prompt = f"""
    Based on the following company name and description, list the clear and impactful vision statements for the company:

    Company Name: {company_name}
    Description: {company_description}

    The vision statement should be professional, inspiring, future-oriented, and reflective of the company's goals and values.
    dont include sub headings. only list it in the bulletin points.
    """

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([prompt])
    return response.text

# Main Streamlit app
def app():
    # Configure the API key
    genai.configure(api_key="AIzaSyB46sAin3C4rTXYCmXkmfQho4fzNUMH6Rw")

    # Streamlit page layout
    st.title("Vision Statement Generator for Companies")

    # Input fields for company name and description
    company_name = st.text_input("Enter the company name:", "")
    company_description = st.text_area("Enter what the company does:", "")

    # Button to generate vision statement
    if st.button("Generate Vision Statement"):
        if company_name and company_description:
            # Fetch vision statement from the Gemini API
            vision_statement = get_vision_statement(company_name, company_description)
            st.write(f"Generated Vision Statement:\n\n{vision_statement}")
        else:
            st.warning("Please enter both company name and description.")

if __name__ == "__main__":
    app()
