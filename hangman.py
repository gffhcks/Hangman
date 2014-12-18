#!/usr/bin/env python

wordlist = [
'Hamburger',
'Hamburglar',
'Ronald',
'Grimace',
'Fries',
'Wendy',
'King',
]

class Puzzle(object):
    def __init__(self, word, chances=6):
        self.answer = word.upper()
        self.state = [None for letter in word]
        self.guessed = []
        self.chances = chances

    def print_word(self):
        word = ''
        for letter in self.state:
            if letter:
                word = word + letter + " "
            else:
                word = word + "_ "
        print word

    def print_guessed(self):
        print "Guessed:"
        guessed = ''
        for guess in self.guessed:
            guessed = guessed + guess + " "
        print guessed
        print ""

    def print_chances(self):
        print "You have {} guesses left.".format(self.chances)
        print ""


    def print_state(self):
        print ""
        print ""
        print ""
        # Print the word
        self.print_word()
        # Print the guessed letters
        self.print_guessed()
        # Print the remaining chances
        self.print_chances()

    def guess(self):
        print ""
        valid = False
        while not valid:
            letter = raw_input("Guess a letter: ")
            if len(letter) > 1:
                print "One letter at a time, please!"
                print ""
                continue
            elif letter in self.guessed:
                print "You already guessed that!"
                print ""
                continue
            elif not letter.isalpha():
                print "That's not a letter!"
                print ""
                continue
            valid = True
        letter = letter.upper()
        self.guessed.append(letter)
        found = 0
        for i in range(len(self.answer)):
            if self.answer[i] == letter:
                found = found + 1
                self.state[i] = letter
        print ""
        print ""
        print "Found {} matches.".format(found)
        print ""
        print ""
        if found == 0:
            self.chances = self.chances - 1

    def chances_left(self):
        if self.chances <= 0:
            return False
        else:
            return True

    def won(self):
        if None not in self.state:
            return True
        else:
            return False

def main():
    puzzle = Puzzle(wordlist[0])
    puzzle.print_state()
    while(True):
        puzzle.guess()
        puzzle.print_state()
        if puzzle.won():
            print "You win!! You had {} guesses left.".format(puzzle.chances)
            break
        if not puzzle.chances_left():
            print "Sorry, you lose! The word was {}.".format(puzzle.answer)
            break
    return 0

if __name__ == "__main__":
    main()
