def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(text):
    text = str(text)
    width = 80
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# call the function
center_text("Spam and eggs")
center_text("Spam, spam and eggs")
center_text("Spam, spam, spam and spam")
center_text(12)

print("first", "second", 3, 4, "spam")