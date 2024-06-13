import emoji

emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis disponíveis:")
for emoji_code, emoji_char in emojis_disponiveis.items():
    print(f"{emoji_char} - {emoji_code}")

frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

frase_emojizada = emoji.emojize(frase_codificada)

print("\nFrase emojizada:")
print(frase_emojizada)