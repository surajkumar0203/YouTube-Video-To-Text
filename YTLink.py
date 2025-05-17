import streamlit as st
from YTLogic import videoToText
import streamlit.components.v1 as components

# header
st.header("""Convert YT Link To Text 👋 """)

label="Enter Valid YT URL"
title = st.text_input(label,placeholder="Enter Valid YT URL")
button = st.button(label="Click Here")

wait_msg = st.empty()
if button:
    if title:
        wait_msg.success("Please Wait....")
        try:
            streams=videoToText(title)
            if isinstance(streams, dict) and 'error' in streams:
                wait_msg.empty()
                st.error(streams['error'])
            else:
                wait_msg.empty()
                # Capture streamed output
                for index,stream in enumerate(streams):
                    temp_text=""
                    for st1 in stream:
                        if st1!="":
                            temp_text+=st1
                    
                    components.html(
                        f"""
                        <button class="button" id="btn_{index}">Copy</button>
                    
                        <script>
                            document.addEventListener("DOMContentLoaded", function() {{
                                let btn = document.getElementById("btn_{index}");
                                let container = document.getElementById("container_{index}");
                                if (btn) {{
                                    
                                    
                                    btn.addEventListener('click', function() {{
                                        
                                        navigator.clipboard.writeText(container.innerText);
                                        alert("Copied!")
                                    }});
                                }}
                            }});
                        </script>

                        <div style="
                            border: 1px solid #ccc;
                            padding: 15px;
                        margin-top:0;
                            border-radius: 6px;
                            background-color: #f8f8f8;
                            white-space: pre-wrap;
                            overflow-x: auto;
                            background-color:black;
                            color:white;
                            overflow-y: auto;
                            height: 100vh;
                            font-size:20px;
                            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                        "
                            id="container_{index}"
                        >
                        <p class="">{temp_text}</p>
                        </div>
                        """,
                        height=700
                    )
                    
               
        except Exception as e:
            st.error("Something Went Wrong!")
    else:
        wait_msg.empty()
        st.error("Please Check Your URL")

