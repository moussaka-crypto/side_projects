#include <iostream>
#define CIMGGIP_MAIN
#include "CImgGIP08.h"
using namespace std;
using namespace cimg_library;

const int grid_size = 10; // Anzahl an Kaestchen in x- und y-Richtung
const int box_size = 30; // size der einzelnen Kaestchen (in Pixel)
const int border = 20; // Rand links und oben bis zu den ersten Kaestchen (in Pixel)

// Prototyp der Funktionen zum Vorbelegen des Grids ...
void grid_init(bool grid[][grid_size]);

int main()
{
	bool grid[grid_size][grid_size] = { 0 };
	bool next_grid[grid_size][grid_size] = { 0 };
	// Erstes Grid vorbelegen ...
	grid_init(grid);
	while (gip_window_not_closed())
	{
		// Spielfeld anzeigen ...
		// gip_stop_updates(); // ... schaltet das Neuzeichnen nach
		// jeder Bildschirmänderung aus
		// TO DO
		// gip_start_updates(); // ... alle Bildschirmänderungen (auch die
								// nach dem gip_stop_updates() ) wieder anzeigen
		gip_sleep(3);
		// Berechne das naechste Spielfeld ...
		// Achtung; Für die Zelle (x,y) darf die Position (x,y) selbst *nicht*
		// mit in die Betrachtungen einbezogen werden.
		// Ausserdem darf bei zellen am rand nicht über den Rand hinausgegriffen
		// werden (diese Zellen haben entsprechend weniger Nachbarn) ...
		// TO DO
		// Kopiere das naechste Spielfeld in das aktuelle Spielfeld ...
		// TO DO
	}
	return 0;
}

void grid_init(bool grid[][grid_size])
{
	int eingabe = -1;
	do {
		cout << "Bitte waehlen Sie die Vorbelegung des Grids aus:" << endl
			<< "0 - Zufall" << endl
			<< "1 - Statisch" << endl
			<< "2 - Blinker" << endl
			<< "3 - Oktagon" << endl
			<< "4 - Gleiter" << endl
			<< "5 - Segler 1 (Light-Weight Spaceship)" << endl
			<< "6 - Segler 2 (Middle-Weight Spaceship)" << endl
			<< "? ";
		cin >> eingabe;
		cin.clear();
		cin.ignore(1000, '\n');
	} while (eingabe < 0 || eingabe > 6);
	if (eingabe == 0)
	{
		// Erstes Grid vorbelegen (per Zufallszahlen) ...
		// TO DO
	}
	else if (eingabe == 1)
	{
		const int pattern_size = 3;
		char pattern[pattern_size][pattern_size] =
		{
		{ '.', '*', '.' },
		{ '*', '.', '*' },
		{ '.', '*', '.' },
		};
		for (int y = 0; y < pattern_size; y++)
			for (int x = 0; x < pattern_size; x++)
				if (pattern[y][x] == '*')
					grid[x][y + 3] = true;
	}
	else if (eingabe == 2)
	{
		const int pattern_size = 3;
		char pattern[pattern_size][pattern_size] =
		{
		{ '.', '*', '.' },
		{ '.', '*', '.' },
		{ '.', '*', '.' },
		};
		for (int y = 0; y < pattern_size; y++)
			for (int x = 0; x < pattern_size; x++)
				if (pattern[y][x] == '*')
					grid[x][y + 3] = true;
	}
	else if (eingabe == 3)
	{
		const int pattern_size = 8;
		char pattern[pattern_size][pattern_size] =
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
		for (int y = 0; y < pattern_size; y++)
			for (int x = 0; x < pattern_size; x++)
				if (pattern[y][x] == '*')
					grid[x][y + 1] = true;
	}
	else if (eingabe == 4)
	{
		const int pattern_size = 3;
		char pattern[pattern_size][pattern_size] =
		{
		{ '.', '*', '.' },
		{ '.', '.', '*' },
		{ '*', '*', '*' },
		};
		for (int y = 0; y < pattern_size; y++)
			for (int x = 0; x < pattern_size; x++)
				if (pattern[y][x] == '*')
					grid[x][y + 3] = true;
	}
	else if (eingabe == 5)
	{
		const int pattern_size = 5;
		char pattern[pattern_size][pattern_size] =
		{
		{ '*', '.', '.', '*', '.' },
		{ '.', '.', '.', '.', '*' },
		{ '*', '.', '.', '.', '*' },
		{ '.', '*', '*', '*', '*' },
		{ '.', '.', '.', '.', '.' },
		};
		for (int y = 0; y < pattern_size; y++)
			for (int x = 0; x < pattern_size; x++)
				if (pattern[y][x] == '*')
					grid[x][y + 3] = true;
	}
	else if (eingabe == 6)
	{
		const int pattern_size = 6;
		char pattern[pattern_size][pattern_size] =
		{
		{ '.', '*', '*', '*', '*', '*' },
		{ '*', '.', '.', '.', '.', '*' },
		{ '.', '.', '.', '.', '.', '*' },
		{ '*', '.', '.', '.', '*', '.' },
		{ '.', '.', '*', '.', '.', '.' },
		{ '.', '.', '.', '.', '.', '.' },
		};
		for (int y = 0; y < pattern_size; y++)
			for (int x = 0; x < pattern_size; x++)
				if (pattern[y][x] == '*')
					grid[x][y + 3] = true;
	}
}