import streamlit as st

# Your iframe URL
iframe_url = "https://app.relevanceai.com/agents/d7b62b/d8e031532058-4c36-a678-816264b41fe1/db7693e8-311c-43b6-8005-a2ff7fa8cff8/share?hide_tool_steps=false&hide_file_uploads=false&hide_conversation_list=false&bubble_style=agent&primary_color=%23685FFF&bubble_icon=pd%2Fchat&input_placeholder_text=Type+your+message...&hide_logo=true"

# Custom CSS to hide Streamlit elements and style the iframe
custom_css = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        margin: 0;
        padding: 0;
    }
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        width: 100%;
        height: 100%;
        border: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display the iframe
st.markdown(f'<iframe src="{iframe_url}"></iframe>', unsafe_allow_html=True)
