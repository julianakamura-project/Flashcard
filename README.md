# Flashy – French/English Flashcards

## Introduction

**Flashy** is a simple French-to-English flashcard application built with Python and Tkinter. It is designed to help users practice French vocabulary by showing a French word first and revealing its English translation after a short delay.

This project was created as a practical exercise in building graphical user interfaces, working with CSV files, and keeping track of learning progress between sessions.

## Program Overview

The application displays one flashcard at a time in a desktop window.

### How it works

1. A French word appears on the front of the card.
2. After **3 seconds**, the card flips automatically to show the English translation.
3. Select the **wrong** button to move to another word and keep the current word in the study list.
4. Select the **right** button when you have learned the word. The word is removed from the remaining study list, and the updated list is saved.
5. When all words have been marked as learned, the application displays an **“All words learned!”** message and an Exit button.

### Vocabulary and progress files

The program uses two CSV files in the `data` folder:

- `french_words.csv` — the original vocabulary list, containing French words and their English translations.
- `words_to_learn.csv` — the remaining words to study. The program loads this file when it exists, allowing progress to carry over between sessions. If it does not exist, the program starts with the original vocabulary list.

The interface also uses image files stored in the `images` folder for the flashcard backgrounds and the correct/incorrect buttons.

## Learning Goals

Through this project, I practiced:

- Creating a desktop GUI with **Tkinter**.
- Arranging interface elements with a `Canvas` and buttons.
- Updating text and images dynamically in response to user actions.
- Using Tkinter's `after()` method to schedule the automatic card flip.
- Selecting random vocabulary entries with Python's `random` module.
- Reading CSV data with **Pandas** and converting it into dictionaries.
- Saving updated study progress back to a CSV file.
- Managing application state, including the current flashcard and remaining vocabulary.

## Project Roadmap

All planned features for this version have been completed.

- [x] Create the flashcard interface with Tkinter.
- [x] Display French vocabulary words on the front of each card.
- [x] Automatically reveal the English translation after 3 seconds.
- [x] Select vocabulary words randomly.
- [x] Add a button to move to another card without marking the current word as learned.
- [x] Add a button to mark a word as learned and remove it from the remaining study list.
- [x] Save the remaining vocabulary to `words_to_learn.csv`.
- [x] Load saved progress when the program is opened again.
- [x] Use the original `french_words.csv` list when no progress file exists.
- [x] Display a completion message and an Exit button when all words have been learned.

## License

See the `LICENSE` file included in this repository for the license terms.
