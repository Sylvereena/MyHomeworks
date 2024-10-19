def censure(text, censured_words):
    new_text = text
    for word in censured_words:
        while word in new_text:
            start_index = new_text.find(word)
            end_index = start_index + len(word)

            firs_section = new_text[:start_index]
            second_section = new_text[end_index:]
            new_text = firs_section + second_section

    return new_text

test = "слово слово слово остаток."

censured_words = ["слово"]
res = censure(test, censured_words)
print(f"Оригинальный текст: '{test}'")
print(f"Слова для удаления: {censured_words}")
print(f"Результат: '{res}'")
