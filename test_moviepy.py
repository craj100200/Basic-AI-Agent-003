from moviepy.video.VideoClip import ColorClip
from moviepy import concatenate_videoclips

def main():
    # Create two simple color clips
    clip1 = ColorClip(size=(640, 480), color=(255, 0, 0)).set_duration(2)
    clip2 = ColorClip(size=(640, 480), color=(0, 255, 0)).set_duration(2)

    # Concatenate them
    final = concatenate_videoclips([clip1, clip2])

    # Write the result
    output_path = "/tmp/test_video.mp4"
    final.write_videofile(output_path, fps=24)
    print("✔ Video created at:", output_path)

if __name__ == "__main__":
    main()
