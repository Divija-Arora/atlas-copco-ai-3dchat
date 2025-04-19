# atlas-copco-ai-3dchat
This project aims to build an AI-powered chat interface that allows users to create and edit 3D CAD models using natural language. 

How to Use
1.	Install required libraries:
pip install openai streamlit
2.	Set your OpenAI API key.
3.	Run the app:
streamlit run app.py
4.	Enter a natural language prompt in the chat interface.
5.	The app generates a .scad file based on your input.
6.	Open the .scad file using OpenSCAD to view the model.
7.	To convert to .stl:
openscad -o model.stl model.scad
