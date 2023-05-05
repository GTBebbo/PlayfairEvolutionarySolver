class Playfair:

    def __init__(self, key: str):
        self.key = key
        self.key_table = {}
        x = 0
        y = 0
        for c in key:
            self.key_table[c] = (x, y)
            x = (x + 1) % 5
            if x == 0:
                y += 1

    def _char_from_index(self, x: int, y: int) -> chr:
        if x < 0 or x > 4:
            x = (x + 5) % 5
        if y < 0 or y > 4:
            y = (y + 5) % 5
        return self.key[5*y+x]

    def decrypt(self, cipher: str) -> str:
        plaintext = ""
        for i in range(0, len(cipher), 2):
            first, second = self.key_table[cipher[i]], self.key_table[cipher[i+1]] 
            if first[0] == second[0]:
                # Xs are equal, same column
                plaintext += self._char_from_index(first[0], first[1]-1)
                plaintext += self._char_from_index(second[0], second[1]-1)
            elif first[1] == second[1]:
                # Ys are equal, same row
                plaintext += self._char_from_index(first[0]-1, first[1])
                plaintext += self._char_from_index(second[0]-1, second[1])
            else:
                # Forms a rectangle
                plaintext += self._char_from_index(second[0], first[1])
                plaintext += self._char_from_index(first[0], second[1])
        return plaintext

    def __str__(self):
        return "\n".join([self.key[:5], self.key[5:10], self.key[10:15], self.key[15:20], self.key[20:]])


if __name__ == "__main__":
    # A quick test of the playfair algorithm
    playfair = Playfair("ALGORITHMSBCDEFKNPQUVWXYZ")
    cipher = "YLNREXRQATQBMLNGOVLOOIDY"
    print(f"cipher: {cipher}")
    plain = playfair.decrypt(cipher)
    print(f"plain: {plain}")
    # Best challenge solution
    playfair = Playfair("EATWHNCYSOBDFPRKLMGIVXZQU")
    cipher = "WEECGNHYLTVRRIKSAHAEEXATONIXHMNCHYWEWBXCFMHLDOSFEAIOABNEAKSRABMHKNRYBHHSDIPAHDNCHKOENCRIYRMHOYBHTWRIEABHGOSNHIDMWLHEATWYHYBNHTOPNRKNLA"
    print(len(cipher))
    print(f"cipher: {cipher}")
    plain = playfair.decrypt(cipher)
    print(f"plain: {plain}")
    # My challenge solution
    playfair = Playfair("ATWHECYSONDFPRBLMGIKXZQUV")
    cipher = "WEECGNHYLTVRRIKSAHAEEXATONIXHMNCHYWEWBXCFMHLDOSFEAIOABNEAKSRABMHKNRYBHHSDIPAHDNCHKOENCRIYRMHOYBHTWRIEABHGOSNHIDMWLHEATWYHYBNHTOPNRKNLA"
    print(len(cipher))
    print(f"cipher: {cipher}")
    plain = playfair.decrypt(cipher)
    print(f"plain: {plain}")
