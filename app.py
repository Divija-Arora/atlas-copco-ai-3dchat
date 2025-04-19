import streamlit as st
from openai import OpenAI

st.title("AI 3D CAD Chat 🛠️🤖")

# User input widget
user_input = st.text_input("Enter your prompt (e.g., 'Create a 3D bracket')")

if user_input:
    # OpenRouter client setup
    client = OpenAI(
        api_key="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",  # <-- Yahan apni actual API key daal
        base_url="https://openrouter.ai/api/v1"
    )
    
    # API call with system instruction and user prompt
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            # System instruction: only return valid OpenSCAD code without extra explanation.
            {"role": "system", "content": "You are an expert in OpenSCAD. Provide only valid OpenSCAD code, no explanations."},
            # User prompt (jo bhi tum input karte ho)
            {"role": "user", "content": user_input}
        ]
    )
    
    # Extract and display the result
    result = response.choices[0].message.content
    st.subheader("Generated OpenSCAD Code:")
    st.code(result, language="scad")
else:
    st.write("Please enter your prompt above and press Enter.")
