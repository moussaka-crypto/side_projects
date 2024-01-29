#pragma once
#include <iostream>
#include <string>
#include <limits>
#include "CImgGIP08.h"
constexpr auto DEFAULT_PATTERN_SIZE = 3;
constexpr auto SPACESHIP1_PATTERN_SIZE = 5;
constexpr auto SPACESHIP2_PATTERN_SIZE = 6;
constexpr auto OCTAGON_PATTERN_SIZE = 8;
using namespace std;
using namespace cimg_library;

const int grid_size = 18; // # Boxes: x and y
const int box_size = 30; // in pixels
const int border = 20;  // Left and top margin (in pixels)

const char staticPattern[DEFAULT_PATTERN_SIZE][DEFAULT_PATTERN_SIZE] =
{
	{ '.', '*', '.' },
	{ '*', '.', '*' },
	{ '.', '*', '.' },
};
const char blinkerPattern[DEFAULT_PATTERN_SIZE][DEFAULT_PATTERN_SIZE] =
{
	{ '.', '*', '.' },
	{ '.', '*', '.' },
	{ '.', '*', '.' },
};
const char gliderPattern[DEFAULT_PATTERN_SIZE][DEFAULT_PATTERN_SIZE] =
{
	{ '.', '*', '.' },
	{ '.', '.', '*' },
	{ '*', '*', '*' },
};
const char octagonPattern[OCTAGON_PATTERN_SIZE][OCTAGON_PATTERN_SIZE] =
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
const char spaceship1Pattern[SPACESHIP1_PATTERN_SIZE][SPACESHIP1_PATTERN_SIZE] =
{
	{ '*', '.', '.', '*', '.' },
	{ '.', '.', '.', '.', '*' },
	{ '*', '.', '.', '.', '*' },
	{ '.', '*', '*', '*', '*' },
	{ '.', '.', '.', '.', '.' },
};
const char spaceship2Pattern[SPACESHIP2_PATTERN_SIZE][SPACESHIP2_PATTERN_SIZE] =
{
	{ '.', '*', '*', '*', '*', '*' },
	{ '*', '.', '.', '.', '.', '*' },
	{ '.', '.', '.', '.', '.', '*' },
	{ '*', '.', '.', '.', '*', '.' },
	{ '.', '.', '*', '.', '.', '.' },
	{ '.', '.', '.', '.', '.', '.' },
};

unsigned char* gip_rgb(int r, int g, int b) {
	return new unsigned char[3] { static_cast<unsigned char>(r),
								  static_cast<unsigned char>(g),
								  static_cast<unsigned char>(b) };
}

int count_living_neighbors(bool grid[][grid_size], int x, int y) {

	int count = 0;
	for (int i = -1; i <= 1; i++) {
		for (int j = -1; j <= 1; j++) {

			if (i || j) {
				int x_neighbor = x + i;
				int y_neighbor = y + j;

				if (x_neighbor >= 0 && x_neighbor < grid_size &&
					y_neighbor >= 0 && y_neighbor < grid_size &&
					grid[x_neighbor][y_neighbor])
				{
					count++;
				}
			}
		}
	}
	return count;
}

void init_pattern(bool grid[][grid_size], const char pattern[], int patternSize, int xOffset, int yOffset)
{
	int idx = 0;
	for (int y = 0; y < patternSize; ++y)
	{
		for (int x = 0; x < patternSize; ++x)
		{
			grid[x + xOffset][y + yOffset] = (pattern[idx] == '*');
			++idx;
		}
	}
}

void init_grid(bool grid[][grid_size])
{
	int i = -1;
	do {
		system("CLS");
		cout << "Please choose the preset for the grid:" << endl
			<< "0: Random" << endl
			<< "1: Static" << endl
			<< "2: Blinker" << endl
			<< "3: Octagon" << endl
			<< "4: Glider" << endl
			<< "5: Glider 1 (Light-Weight Spaceship)" << endl
			<< "6: Glider 2 (Middle-Weight Spaceship)" << endl
			<< "99: Quit" << endl
			<< "player@game-of-life:~$ ";

		string s;
		getline(cin, s);
		if (s.empty()) {
			cout << "Invalid Input. Please try again." << endl; system("PAUSE");
			continue;
		}
		try {
			i = std::stoi(s);
		}
		catch (const std::invalid_argument&) {
			i = -1;
		}

		if (cin.fail()) {
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;
		}

		switch (i) {
		case 0:
			for (int y = 0; y < grid_size; y++) {
				for (int x = 0; x < grid_size; x++) {
					grid[x][y] = gip_random(0, 1);
				}
			}
		break;
		case 1: {
			init_pattern(grid, reinterpret_cast<const char*>(staticPattern), DEFAULT_PATTERN_SIZE, 0, DEFAULT_PATTERN_SIZE);
		}
		break;
		case 2: {
			init_pattern(grid, reinterpret_cast<const char*>(blinkerPattern), DEFAULT_PATTERN_SIZE, 0, DEFAULT_PATTERN_SIZE);
		}
		break;
		case 3: {
			init_pattern(grid, reinterpret_cast<const char*>(octagonPattern), OCTAGON_PATTERN_SIZE, 0, 1);
		}
		break;
		case 4: {
			init_pattern(grid, reinterpret_cast<const char*>(gliderPattern), DEFAULT_PATTERN_SIZE, 0, DEFAULT_PATTERN_SIZE);
		}
		break;
		case 5: {
			init_pattern(grid, reinterpret_cast<const char*>(spaceship1Pattern), SPACESHIP1_PATTERN_SIZE, 0, 3);
		}
		break;
		case 6: {
			init_pattern(grid, reinterpret_cast<const char*>(spaceship2Pattern), SPACESHIP2_PATTERN_SIZE, 0, 3);
		}
		break;
		case 99:
			exit(0);
		default:
			cout << "Invalid Input. Please try again." << endl; system("PAUSE");
			break;
		}
	} while (i != 99 && (i < 0 || i > 6));
}
