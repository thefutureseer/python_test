## If you need to get set up go to [picREADMe.md](./picREADMe.md)

## If your already set up and want to make videos. Lets string pics together:
To incorporate a video generator into the existing GUI-driven workflow, you need to integrate the video generation functionality within the GUI interface. The goal is to allow the user to generate a video from a sequence of frames using the GUI.

Here’s how to set it up:

## Modify the GUI Backend (Python Code)
Add an endpoint or GUI button in your main.py or equivalent backend logic that performs the following:

1. Accept User Input for Frame Directory:

Allow the user to specify the directory containing the frames.
Allow customization of frame rate, output filename, etc.  

2. Run FFmpeg to Generate the Video:

Use the specified frame directory and settings to generate the video using FFmpeg.

## Add a Button to the GUI
Modify the GUI frontend to include a button for video generation. When clicked, it should:

1. Prompt the user to enter the frame directory and output video filename.
2. Send a POST request to the /generate_video endpoint with the necessary data.

## Steps to Use
1. Run the Backend: Launch main.py with the updated backend code.

2. Access the GUI: Use the TryCloudflare URL to access the GUI.

3. Generate Video:

- Fill out the form with the frame directory, output filename, and frame rate.
- Click the "Generate Video" button to initiate the process.
4. Video Output:

- The generated video will appear in the working directory or as specified.