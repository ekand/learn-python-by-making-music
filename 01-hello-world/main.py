import scamp


def text_to_melody(text):
    note_mapping = {
        'H': 60,
        'e': 62,
        'l': 64,
        'o': 65,
        ',': 67,
        ' ': 69,
        'W': 71,
        'r': 72,
        'd': 74,
    }

    melody = []
    for char in text:
        note = note_mapping.get(char)
        if note:
            melody.append(note)

    return melody


def main():
    text = "Hello, World"
    melody = text_to_melody(text)

    tempo = 120
    s = scamp.Session(tempo=tempo)

    violin = s.new_part('violin')

    for note in melody:
        violin.play_note(note, 0.8, 0.5)


if __name__ == "__main__":
    main()

