import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a, b = s.split("to")
        a_ampm = 0
        b_ampm = 0


        if "am" in a.lower():
            a = a.lower().replace(" am", "").strip()
        elif "pm" in a.lower():
            a_ampm = 12
            a = a.lower().replace(" pm", "").strip()

        if "am" in b.lower():
            b = b.lower().replace(" am", "").strip()
        elif "pm" in b.lower():
            b_ampm = 12
            b = b.lower().replace(" pm", "").strip()

        if ":" in a:
            ha, ma = a.split(":")
            if int(ma) > 59:
                raise ValueError
        else:
            ma = 0
            ha = a

        if ":" in b:
            hb, mb = b.split(":")
            if int(mb) > 59:
                raise ValueError
        else:
            mb = 0
            hb = b

        if int(ha) > 12:
            raise ValueError
        if int(hb) > 12:
            raise ValueError

        if int(ha) == 12:
            ha= int(ha) - 12
        if int(hb) == 12:
            hb= int(hb) - 12


        h1 = int(ha)+a_ampm
        m1 = int(ma)
        h2 = int(hb)+b_ampm
        m2 = int(mb)
        time = (f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}")
        return time



    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()