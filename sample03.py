def main():
    f = open("fruits.txt", mode="w")

    fruits = ["リンゴ", "オレンジ", "バナナ"]

    f.write(",".join(fruits))

    # f.write("リンゴ,")
    # f.write("オレンジ,")
    # f.write("バナナ")

    f.close()


if __name__ == "__main__":
    main()
    
