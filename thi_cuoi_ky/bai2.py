with open("input.txt", "r+", encoding="utf-8") as f:
    # đọc nội dung
    f1 = f.read()
    print(f1)
    # đếm số từ duy nhất
    words = f1.replace(",", "").replace(".", "").split()
    unique_words = set(words)
    print("Số lượng từ duy nhất:", len(unique_words))
    alphabetical_order = sorted(unique_words, key=str.casefold)
    alp_lst = ", ".join(alphabetical_order)
    print(alp_lst)

# tạo output.txt
f2 = open("output.txt", "a+")
f2.write(alp_lst)
