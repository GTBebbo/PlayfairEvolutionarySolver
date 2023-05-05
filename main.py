from evolution import Simulation
from settings import CIPHERTEXT_FILE, MAX_GENERATIONS, PLAINTEXT_FILE, POPULATION

class Solver:

    def __init__(self, cipher_file_path: str, plain_file_path: str):
        """ Creates the Solver and loads the ciphertext and plaintext.

        Args:
            cipher_file_path: The path to the cipher.text file inc the filename.
            plain_file_path: The path to the plain.text file inc the filename.
        """
        self._load_ciphertext(cipher_file_path)
        self._load_plaintext(plain_file_path)
        self.simulation = Simulation(
                POPULATION,
                max_generations=MAX_GENERATIONS,
        )

    def solve(self):
        self.simulation.go(self.ciphertext, self.plaintext)

    def _load_ciphertext(self, cipher_file_path: str) -> None:
        """Load the ciphertext into the solver.

        This will also process the ciphertext to remove spaces and newlines.

        Args:
            cipher_file_path: The path to the cipher.text file inc the filename.
        """
        with open(cipher_file_path, 'r') as cipher_file:
            ciphertext = cipher_file.read()
            # Remove space and newline characters.
            ciphertext = ciphertext.replace('\r', '')
            ciphertext = ciphertext.replace('\n', '')
            ciphertext = ciphertext.replace(' ', '')
            if len(ciphertext) % 2:
                ciphertext = ciphertext[:-1]
            self.ciphertext = ciphertext

    def _load_plaintext(self, plain_file_path: str) -> None:
        """Load the plaintext into the solver.

        This will also process the plaintext to remove spaces and newlines.

        Args:
            cipher_file_path: The path to the cipher.text file inc the filename.
        """
        with open(plain_file_path, 'r') as plain_file:
            plaintext = plain_file.read()
            # Remove space and newline characters.
            plaintext = plaintext.replace('\r', '')
            plaintext = plaintext.replace('\n', '')
            plaintext = plaintext.replace(' ', '')

            self.plaintext = plaintext


def main():
    solver = Solver(CIPHERTEXT_FILE, PLAINTEXT_FILE)
    print(f"CIPHER TEXT: {solver.ciphertext}")
    print(f"PLAIN TEXT:  {solver.plaintext}")
    print("Beginning simulation")
    print()
    solver.solve()


if __name__ == "__main__":
    main()
