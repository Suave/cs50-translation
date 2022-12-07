def main():
    t = input("What time is it? ") # t = "7:43"
    g = convert(t)
    if g >= 7 and g <= 8:
        print("breakfast time")
    elif g >= 12 and g<= 13:
        print("lunch time")
    elif g >= 18 and g <= 19:
        print("dinner time")

def convert(time):
    a = time.split(":")
    return float(a[1]) / 60 + float(a[0])
     


if __name__ == "__main__":
    main()

