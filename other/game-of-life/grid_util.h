#pragma once
#include <iostream>
#include <string>
#include <limits>
#include "CImgGIP08.h"
#define STATIC_PATTERN_SIZE 3
#define BLINKER_PATTERN_SIZE 3
#define OCTAGON_PATTERN_SIZE 8
#define GLIDER_PATTERN_SIZE 3
#define SPACESHIP1_PATTERN_SIZE 5
#define SPACESHIP2_PATTERN_SIZE 6
using namespace std;
using namespace cimg_library;

const int grid_size = 18; // Anzahl an Kaestchen in x- und y-Richtung
const int box_size = 30; // size der einzelnen Kaestchen (in Pixel)
const int border = 20;  // Rand links und oben bis zu den ersten Kaestchen (in Pixel)

unsigned char* gip_rgb(int r, int g, int b) {
	static unsigned char color[3];
	color[0] = (unsigned char)r;
	color[1] = (unsigned char)g;
	color[2] = (unsigned char)b;
	return color;
}

int count_living_neighbors(bool grid[][grid_size], int x, int y) {

	int count = 0;
	for (int i = -1; i <= 1; i++) {
		for (int j = -1; j <= 1; j++) {

			int x_neighbor = x + i;
			int y_neighbor = y + j;

			if (x_neighbor >= 0 && x_neighbor < grid_size &&
				y_neighbor >= 0 && y_neighbor < grid_size) {

				if (!(i == 0 && j == 0) && grid[x_neighbor][y_neighbor])
					count++;
			}
		}
	}
	return count;
}

const static int PATTERN_SIZE[4] = { 3,5,6,8 };

void grid_init(bool grid[][grid_size])
{
	int eingabe;
	do {
		system("CLS");
		cout << "Bitte waehlen Sie die Vorbelegung des Grids aus:" << endl
			<< "0 - Zufall" << endl
			<< "1 - Statisch" << endl
			<< "2 - Blinker" << endl
			<< "3 - Oktagon" << endl
			<< "4 - Gleiter" << endl
			<< "5 - Segler 1 (Light-Weight Spaceship)" << endl
			<< "6 - Segler 2 (Middle-Weight Spaceship)" << endl
			<< "99 - Quit" << endl
			<< "?> ";

		string input;
		getline(cin, input);
		if (input.empty()) {
			cout << "Ungueltige Auswahl. Bitte erneut waehlen." << endl;
			continue;
		}
		try {
			eingabe = std::stoi(input);
		}
		catch (const std::invalid_argument&) {
			eingabe = -1;
		}

		if (cin.fail()) {
			cout << "Ungueltige Eingabe. Bitte nur Zahlen verwenden." << endl;
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;
		}

		switch (eingabe) {
		case 0:
			for (int y = 0; y < grid_size; y++) {
				for (int x = 0; x < grid_size; x++) {
					grid[x][y] = gip_random(0, 1);
				}
			}
			break;
		case 1: {
			char staticPattern[STATIC_PATTERN_SIZE][STATIC_PATTERN_SIZE] =
			{
			{ '.', '*', '.' },
			{ '*', '.', '*' },
			{ '.', '*', '.' },
			};
			for (int y = 0; y < STATIC_PATTERN_SIZE; y++)
				for (int x = 0; x < STATIC_PATTERN_SIZE; x++)
					grid[x][y + STATIC_PATTERN_SIZE] = (staticPattern[y][x] == '*');
		}
			  break;
		case 2: {
			char blinkerPattern[BLINKER_PATTERN_SIZE][BLINKER_PATTERN_SIZE] =
			{
			{ '.', '*', '.' },
			{ '.', '*', '.' },
			{ '.', '*', '.' },
			};
			for (int y = 0; y < BLINKER_PATTERN_SIZE; y++)
				for (int x = 0; x < BLINKER_PATTERN_SIZE; x++)
					grid[x][y + BLINKER_PATTERN_SIZE] = (blinkerPattern[y][x] == '*');
		}
			  break;
		case 3: {
			char octagonPattern[OCTAGON_PATTERN_SIZE][OCTAGON_PATTERN_SIZE] =
			{
			{ '.', '.', '.', '*', '*', '.', '.', '.' },
			{ '.', '.', '*', '.', '.', '*', '.', '.' },
			{ '.', '*', '.', '.', '.', '.', '*', '.' },
			{ '*', '.', '.', '.', '.', '.', '.', '*' },
			{ '*', '.', '.', '.', '.', '.', '.', '*' },
			{ '.', '*', '.', '.', '.', '.', '*', '.' },
			{ '.', '.', '*', '.', '.', '*', '.', '.' },
			{ '.', '.', '.', '*', '*', '.', '.', '.' },
			};
			for (int y = 0; y < OCTAGON_PATTERN_SIZE; y++)
				for (int x = 0; x < OCTAGON_PATTERN_SIZE; x++)
					grid[x][y + 1] = (octagonPattern[y][x] == '*');
		}
			  break;
		case 4: {
			char gliderPattern[GLIDER_PATTERN_SIZE][GLIDER_PATTERN_SIZE] =
			{
			{ '.', '*', '.' },
			{ '.', '.', '*' },
			{ '*', '*', '*' },
			};
			for (int y = 0; y < GLIDER_PATTERN_SIZE; y++)
				for (int x = 0; x < GLIDER_PATTERN_SIZE; x++)
					grid[x][y + GLIDER_PATTERN_SIZE] = (gliderPattern[y][x] == '*');
		}
			  break;
		case 5: {
			char spaceship1Pattern[SPACESHIP1_PATTERN_SIZE][SPACESHIP1_PATTERN_SIZE] =
			{
			{ '*', '.', '.', '*', '.' },
			{ '.', '.', '.', '.', '*' },
			{ '*', '.', '.', '.', '*' },
			{ '.', '*', '*', '*', '*' },
			{ '.', '.', '.', '.', '.' },
			};
			for (int y = 0; y < SPACESHIP1_PATTERN_SIZE; y++)
				for (int x = 0; x < SPACESHIP1_PATTERN_SIZE; x++)
					grid[x][y + 3] = (spaceship1Pattern[y][x] == '*');
		}
			  break;
		case 6: {
			char spaceship2Pattern[SPACESHIP2_PATTERN_SIZE][SPACESHIP2_PATTERN_SIZE] =
			{
			{ '.', '*', '*', '*', '*', '*' },
			{ '*', '.', '.', '.', '.', '*' },
			{ '.', '.', '.', '.', '.', '*' },
			{ '*', '.', '.', '.', '*', '.' },
			{ '.', '.', '*', '.', '.', '.' },
			{ '.', '.', '.', '.', '.', '.' },
			};
			for (int y = 0; y < SPACESHIP2_PATTERN_SIZE; y++)
				for (int x = 0; x < SPACESHIP2_PATTERN_SIZE; x++)
					grid[x][y + 3] = (spaceship2Pattern[y][x] == '*');
		}
			  break;
		case 99:
			exit(0);
		default:
			cout << "Ungueltige Auswahl. Bitte erneut waehlen." << endl;
			break;
		}
	} while (eingabe != 99 && (eingabe < 0 || eingabe > 6));
}