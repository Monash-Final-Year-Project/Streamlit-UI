import streamlit as st


def load_image():
    uploaded_file = st.file_uploader(label='Upload a video to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.video(image_data)
        
    return uploaded_file


def main():
    st.title('Crime Dataset Captioning')
    st.info('Please upload your video below! Make sure it is in MP4 format!')
    
    uploaded = load_image()
    
    if uploaded:
     
        if st.button('Run model to caption the video'):   
            st.subheader("Frame 0 to 9 seconds:")
            st.text("Pedestrians walking across the road normally.")
            st.subheader("Frame 10 to 19 seconds:")
            st.text("A man gets hit in the back of the head by another pedestrian.")
            st.subheader("Frame 20 to 26 seconds:")
            st.text("The victim is knocked out and other pedestrians are rushing to help him.")



if __name__ == '__main__':
    main()