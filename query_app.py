import streamlit as st

st.set_page_config(page_title="Multimodal RAG Demo", layout="wide")

st.title("📄 Multimodal RAG System UI")

st.sidebar.header("Upload Documents")
text_files = st.sidebar.file_uploader("Upload Text/PDF Files", type=["txt", "pdf"], accept_multiple_files=True)
image_files = st.sidebar.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

tab1, tab2 = st.tabs(["Ingestion", "Chatbot"])

with tab1:
    st.header("Document Ingestion Status")
    if text_files or image_files:
        st.success("Files uploaded successfully!")
        st.write("### Uploaded Text Files")
        for file in text_files:
            st.write(f"- {file.name}")
        st.write("### Uploaded Images")
        for img in image_files:
            st.image(img, width=200)
    else:
        st.info("Upload files from the sidebar to start ingestion.")

with tab2:
    st.header("Chat with Your Documents")
    user_query = st.text_input("Ask a question about the documents:")
    if st.button("Generate Answer"):
        if user_query:
            # Placeholder for model response
            st.write("### Answer:")
            st.write("This is where the model's response will appear.")
        else:
            st.warning("Please enter a question.")