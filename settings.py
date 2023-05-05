"""Settings"""

# Alphabet is the letters that will be used to build the table
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Exclude J from the alphabet

# The maximum number of generations until the program stops and outputs the
# current best answer
MAX_GENERATIONS = 10000

# The number of solutions in each generation
# This should be an even number and greater than KEEP_FITTEST
POPULATION = 1500

# The number of best solutions carried over from the previous generation
# This should be an even number
KEEP_FITTEST = 30

# The path to the cipher text file
CIPHERTEXT_FILE = "cipher.text"

# The path to the plain text file (The known plain text of the cipher)
PLAINTEXT_FILE = "plain.text"

def validate_settings():
    errors = []
    warnings = []

    # Validate Alphabet
    if not len(ALPHABET) == 25:
        errors.append("The alphabet must contain 25 characters")
    if not len(set(ALPHABET)) == len(ALPHABET):
        errors.append("The alphabet must contain unique characters")
    if not ALPHABET == ALPHABET.upper():
        warnings.append("Letters in the alphabet should be uppercase")

    # Validate Max Generations
    if MAX_GENERATIONS < 1:
        errors.append("The Max Generations must be a positive integer")
    if MAX_GENERATIONS < 15:
        warnings.append("The Max Generations is too low, you may not get good "
                        "results")
    
    # Validate Population
    if POPULATION < 1:
        errors.append("The Population size must be a positive integer")
    if POPULATION < 10:
        warnings.append("The Population size is small, you may not get good "
                        "results")
    if POPULATION - KEEP_FITTEST < 1:
        errors.append("The Population must be larger than KEEP_FITTEST")

    # Validate Keep Fittest
    if KEEP_FITTEST < 0:
        errors.append("Keep Fittest must be 0 or a positive integer")
    if POPULATION - KEEP_FITTEST < POPULATION // 2:
        warnings.append("More than half the population is kept between "
                        "generations, you may not get good results")

    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        exit()

    # We don't bother validating the ciphertext and plaintext files as they
    # will error at the start of the program.

validate_settings()

