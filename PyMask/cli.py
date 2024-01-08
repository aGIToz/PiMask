import argparse
from PyMask.annotator import create_mask

def main():
    parser = argparse.ArgumentParser(description='Create a mask on an image.')
    parser.add_argument('--input', type=str, help='Path to the image to be annotated')
    parser.add_argument('--output', type=str, help='Path to the generated mask image')

    args = parser.parse_args()
    create_mask(args.input, args.output)

if __name__ == "__main__":
    main()
