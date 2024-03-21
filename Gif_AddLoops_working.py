import imageio

AddLoopsTimes = 10

# Load the GIF file
input_gif_path = "Gif_Mods\winbootlogo-current.gif"
output_gif_path = "C:/Users/shaik/OneDrive/Desktop/current codes/Gif_Mods/output10.gif"

with imageio.get_reader(input_gif_path) as reader:
    # Extract frames and frame durations
    frames = [frame for frame in reader]
    durations = [reader.get_meta_data()['duration'] for _ in range(len(frames))]

    # Append frames 5 times
    repeated_frames = frames * AddLoopsTimes
    repeated_durations = durations * AddLoopsTimes

# Write the modified frames to a new GIF file with adjusted durations
with imageio.get_writer(output_gif_path, mode='I', duration=repeated_durations) as writer:
    for frame in repeated_frames:
        writer.append_data(frame)

print("GIF file with increased loops created successfully!")