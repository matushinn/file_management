def main():
    f = open("users.txt", mode="r")

    text = f.read()

    lines = text.split("\n")

    # print(lines)

    print(f"{lines[0][0:10] }さんは{lines[0][11:13]}歳です")
    print(f"{lines[1][0:8] }さんは{lines[1][10:11]}歳です")
    print(f"{lines[2][0:15] }さんは{lines[2][16:18]}歳です")

    for line in lines:
        # splitを使うとくぎれる

        out_put = line.split(",")
        print(f"{out_put[0]}さんは{out_put[1]}歳です")

    f.close()


if __name__ == "__main__":
    main()
