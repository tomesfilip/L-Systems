class SentenceGenerator:
    @staticmethod
    def generate_word(axiom: str, rules: dict, iter_count: int = 2):
        sentences = []
        word = axiom
        for i in range(iter_count):
            new_word = ""
            for character in word:
                new_word += rules[character] if character in rules.keys() else character
            word = new_word
            sentences.append(word)
        return sentences
