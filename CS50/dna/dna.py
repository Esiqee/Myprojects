import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    filename = sys.argv[1]
    with open(filename) as file:
        reader = csv.reader(file)
        database = list(reader)

    # TODO: Read DNA sequence file into a variable
    filename = sys.argv[2]
    with open(filename) as file:
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    seq = database[0][1:]
    result = []
    combination = 0
    for combination in range(len(seq)):
        result.append(longest_match(dna, seq[combination]))
        combination + 1

    # TODO: Check database for matching profiles
    strresult = []
    for element in result:
        strresult.append(str(element))
    # if person is found print name and end program
    person = 0
    for person in range(len(database)):
        if database[person][1:] == strresult:
            print(database[person][0])
            exit()
        person + 1
    # if person is not found
    print("No match")

    return

    # tests
    # print(database)
    # print(dna)
    # print(seq)
    # print(result)
    # print(strresult)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
