from moviepy.editor import ImageClip, concatenate_videoclips

# Create 2 simple colored clips
clip1 = ImageClip(color=(255, 0, 0), size=(640, 480)).set_duration(2)
clip2 = ImageClip(color=(0, 255, 0), size=(640, 480)).set_duration(2)

# Concatenate clips
final_clip = concatenate_videoclips([clip1, clip2])

# Write output video
final_clip.write_videofile("/tmp/test_video.mp4", fps=24)

print("Video created successfully at /tmp/test_video.mp4")
