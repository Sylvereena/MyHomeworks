def big_words(text, reserved_words):
    for word in reserved_words:
        text = text.replace(word, word.upper())
    return text

input_text = input("Введите текст: ")

reserved_words = []
print("Введите зарезервированные слова:")
while True:
    word = input()
    if word.strip() == "":
        break
    reserved_words.append(word.strip())
res_text = big_words(input_text, reserved_words)

print(f"Измененный текст: '{res_text}'")