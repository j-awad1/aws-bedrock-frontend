
import streamlit as st
from BedrockResponse import BedrockProcessing
br=BedrockProcessing()

#import streamlit as st

st.header("Bedrock Knowledgebase Example")

def display_local_image(image_path, max_width=None, caption=None):
    """Displays a local image on the Streamlit UI with customization options.

    Args:
        image_path (str): The path to the local image file.
        max_width (int, optional): The maximum width for the image. Defaults to None.
        caption (str, optional): A caption for the image. Defaults to None.
    """

    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
            st.image(image_data, caption=caption, width=max_width)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
    except Exception as e:
        st.error(f"An error occurred displaying the image: {e}")

# Choose the image path based on your environment
image_path = 'bedrock-example.jpg'  # Replace with the actual path

# Optional: Apply customization options
max_width = 300  # Set a maximum width
caption = "AWS Bedrock Architecture Pattern"  # Add a caption

display_local_image(image_path, max_width, caption)




#with st.chat_message("user"):
#    st.write("Hello 👋")
    
#prompt = st.chat_input("Say something")
#if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")

    
# Display a text box for input
#col1, col2 = st.columns(2)

# Input elements placed in separate columns
#prompt = col1.text_input("Enter your query:", key="query")
#model_name = col2.selectbox("Select Model:", ["","Llama2_13B", "Claude21"], key="Model")
prompt = st.text_input("Please enter your query", max_chars=2000)
model_name = st.selectbox("Select Model:", ["","Llama2_13B", "Claude21"], key="Model")
max_gen_len = st.slider("Maximum Length Generation:", min_value=0, max_value=4096, value=(2048))
temperature = st.slider("Temperature:", min_value=0.0, max_value=1.0, value=(0.1))
top_p = st.slider("Top_p:", min_value=0.0, max_value=1.0, value=(0.5))
# print(f"Model name Selected = {model_name}")
# print(f"Max Length Selected = {max_gen_len}")
# print(f"Temperature Selected = {temperature}")
st.write('TEMP: ', temperature)
# print(f"Top P Selected = {top_p}")
prompt = prompt.strip()

#print(prompt)

# Display a primary button for submission
submit_button = st.button("Submit", type="primary")

# Display a button to end the session
end_session_button = st.button("End Session")


# Session State Management
if 'history' not in st.session_state:
    st.session_state['history'] = []

    
    
# Handling user input and responses
if submit_button and prompt:
    event = {
        "sessionId": "MYSESSION",
        "question": prompt
    }

    print(event)
    #llama_response, location = br.get_response_from_becrock_model_llama2(prompt)
    
    bedrock_response =br.get_bedrock_model_response(prompt, model_name, max_gen_len, temperature, top_p)
    print(f"bedrock_response type ={type(bedrock_response)}")
    print(f"response keys = {bedrock_response.keys()}")
    #print(bedrock_response)
    response = bedrock_response['response']
    #claude21_response = bedrock_response['claude21_response']
    location=bedrock_response['location']
    # Use trace_data and formatted_response as needed
    #st.sidebar.text_area("Trace Data", value=all_data, height=300)
    st.session_state['history'].append({"question":prompt, "answer":response, "model":model_name, "max_gen_len":max_gen_len, "temperature":temperature, "top_p":top_p, "refrences":','.join(location)})
    st.session_state['trace_data'] = response

    
if end_session_button:
    st.session_state['history'].append({"question": "Session Ended", "answer": "Thank you for using Enterprise Architect Agent!"})
    event = {
        "sessionId": "MYSESSION",
        "question": "placeholder to end session",
        "endSession": True
    }
    #agenthelper.lambda_handler(event, None)
    st.session_state['history'].clear()


# Display conversation history
st.write("## Conversation History")


for chat in reversed(st.session_state['history']):
    
    # Creating columns for Question
    print (f"chat keys = {chat.keys()}")
    st.text_area("Q:", value=chat["question"], height=50, key=str(chat)+"q", disabled=True)
    st.text_area(f"{chat['model']}:", value=chat["answer"], height=100, key=str(chat)+"a")
    st.text_area("References:", value=chat["refrences"], height=20,key=str(chat)+"r", disabled=True)





st.write("## Test Knowledge Base Prompts")
st.markdown("""
- "summarise different phases of cloud adoption and migration"

- "what is saga"

""")
