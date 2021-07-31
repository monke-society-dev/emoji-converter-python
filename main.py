
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "\U0001f606",
        ":(": "\U0001f61E",
        ";)": "\N{winking face}",
        ":|": "\N{zipper-mouth face}",
        "(:": "\U0001F643	",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
result = emoji_converter(message)
print(result)