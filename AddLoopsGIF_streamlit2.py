import streamlit as st
import imageio
import os
from PIL import Image

def increase_gif_loops(input_gif_path, output_gif_path, num_loops):
    with imageio.get_reader(input_gif_path) as reader:
        # Extract frames and frame durations
        frames = [frame for frame in reader]
        durations = [reader.get_meta_data()['duration'] for _ in range(len(frames))]

        # Append frames multiple times
        repeated_frames = frames * num_loops
        repeated_durations = durations * num_loops

    # Write the modified frames to a new GIF file with adjusted durations
    with imageio.get_writer(output_gif_path, mode='I', duration=repeated_durations) as writer:
        for frame in repeated_frames:
            writer.append_data(frame)

def main():
    st.title("Increase GIF Loops - App")
    
    # Display instructions
    st.write("""
    ## Instructions:
    1. Upload a GIF file using the upload button below.
    2. Enter the number of loops you want for the GIF.
    3. Click the "Increase Loops" button to modify the GIF.
    4. Once modified, you can download the modified GIF using the download button.
    Note: Increasing loops count increases the file size of the GIF.
    """)

    # Upload GIF file
    uploaded_file = st.file_uploader("Upload GIF file", type=["gif"])
    
    if uploaded_file is not None:
        # Display uploaded GIF
        st.image(uploaded_file, caption="Uploaded GIF", use_column_width=True)

        # Number of loops input
        num_loops = st.number_input("Enter the number of loops", min_value=1, value=5)

        if st.button("Increase Loops"):
            # Save uploaded GIF locally
            with open("input.gif", "wb") as f:
                f.write(uploaded_file.getvalue())

            # Increase loops
            increase_gif_loops("input.gif", "output.gif", num_loops)

            # Display modified GIF
            modified_gif = open("output.gif", "rb").read()
            st.image(modified_gif, caption="Modified GIF", use_column_width=True)

            # Download button for modified GIF
            st.download_button(label="Download Modified GIF", data=modified_gif, file_name="ModdedGIF.gif", mime="image/gif")

            # Display output sizes
            original_size = os.path.getsize("input.gif") / 1024
            modified_size = os.path.getsize("output.gif") / 1024
            st.write(f"Original GIF Size: {original_size:.2f} KB")
            st.write(f"Modified GIF Size: {modified_size:.2f} KB")
    #else:
        # image = Image.open('input.gif')
        #st.video("https://github.com/shaikamirgh/Custom-Boot-Animation/blob/main/input.gif")
        #st.video("input.gif", format='video/mp4')
        #st.markdown("![Default GIF for you to try! Drag and Drop!](https://github.com/shaikamirgh/Custom-Boot-Animation/blob/main/input.gif)")
        #st.markdown("![Default GIF for you to try! Drag and Drop!](https://media.giphy.com/media/og52So0BUmZVe/giphy.gif)")

if __name__ == "__main__":
    main()
