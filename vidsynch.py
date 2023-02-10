import cv2

def synchronize_videos(video_list):
    # Step 1: Reading the frames
    frame_list = []
    for video in video_list:
        cap = cv2.VideoCapture(video)
        frames = []
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frames.append(frame)
            else:
                break
        frame_list.append(frames)

    # Step 2: Synchronizing the frames
    min_len = min([len(frames) for frames in frame_list])
    for i in range(len(frame_list)):
        frame_list[i] = frame_list[i][:min_len]

    # Step 3: Writing the synchronized video
    # Get the dimensions of the first video
    cap = cv2.VideoCapture(video_list[0])
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(width)
    print(height)

    print((frame_list[0][0].shape[1], frame_list[0][0].shape[0]))

    out = cv2.VideoWriter('synchronized_video.avi',cv2.VideoWriter_fourcc(*'XVID'), 25.0, (width, height), True) #needs final boolean?

    for i in range(min_len):   
        frame = []
        for j in range(len(frame_list)):
            frame.append(frame_list[j][i])
        out.write(cv2.vconcat(frame))
    out.release()

video_list = ['vid1.mp4', 'vid2.mp4', 'vid3.mp4']
#video_list = ['vid1_converted.mp4', 'vid2_converted.mp4', 'vid3_converted.mp4']
synchronize_videos(video_list)

print("Synchronized video is saved'")
