from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

CHARSET = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-+~<>i!lI;:,\"^`'. "


def get_filler(r, g, b, a=256):
    if a == 0:
        return '  '
    length = len(CHARSET)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    return CHARSET[int(length*gray/(257.0))] + CHARSET[int(length*gray/(257.0))]


if __name__ == "__main__":
    image = Image.open(args.filename)
    w = raw_input("please input the width:\n")
    w=int(w)
    h = raw_input("please input the height:\n")
    h=int(h)
    image = image.resize((w, h), Image.NEAREST)

    txt = ""

    for i in range(h):
        for j in range(w):
            txt += get_filler(*image.getpixel((j, i)))
        txt += '\n'

    with open(args.filename[:-4] + ".txt", 'w') as f:
        f.write(txt)
    print 'Finished,you can find the file *.txt(* is your picture name).'
