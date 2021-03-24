"""
Python YouTube video downloader
"""
import os
import argparse
from pytube import YouTube


parser = argparse.ArgumentParser(
    prog=__file__,
    description="A YouTube video downloader. Pass URL of video or playlist.",
)
parser.add_argument("url", type=str, help="An URL to video or playlist.")
parser.add_argument("--name", type=str, help="New name for video")
parser.add_argument("--out", type=str, default=".", help="Where to download video")

args = parser.parse_args()

if args.url:
    options = {}
    if args.out == ".":
        options.update({"output_path": os.getcwd()})
    elif os.path.exists(args.out):
        options.update({"output_path": args.out})
    else:
        raise FileNotFoundError(f"No such directory {args.out}")
    if args.name:
        options.update({"filename": args.name})

    video = YouTube(url=args.url)
    video.streams.first().download(**options)
