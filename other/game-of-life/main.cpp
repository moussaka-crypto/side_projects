#include <iostream>
#include <string>
#define CIMGGIP_MAIN
#include "CImgGIP08.h"
using namespace std;
using namespace cimg_library;

/*This has to be the stupidest project I've done up to date...*/

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

// Prototyp der Funktionen zum Vorbelegen des Grids ...
void grid_init(bool grid[][grid_size]);

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

int main()
{
	bool grid[grid_size][grid_size] = { 0 };
	bool next_grid[grid_size][grid_size] = { 0 };

	// Erstes Grid vorbelegen ...
	grid_init(grid);
	while (gip_window_not_closed())
	{
		// Spielfeld anzeigen ..
		gip_white_background();
		gip_stop_updates(); // ... schaltet das Neuzeichnen nach
							   // jeder Bildschirmänderung aus
		// TO DO
		for (int y = 0; y < grid_size; ++y) {
			for (int x = 0; x < grid_size; ++x) {
				if (grid[x][y]) {
					gip_draw_rectangle(border + x * box_size, border + y * box_size,
						border + (x + 1) * box_size, border + (y + 1) * box_size,
						//gip_rgb(75, 0, 130)); // indigo for living cells
						gip_rgb(57, 255, 20)); // neon green for living cells
				}
				else {
					gip_draw_rectangle(border + x * box_size, border + y * box_size,
						border + (x + 1) * box_size, border + (y + 1) * box_size,
						gip_rgb(54, 54, 54)); // grey for dead
				}
			}
		}

		gip_start_updates(); // ... alle Bildschirmänderungen (auch die
							 // nach dem gip_stop_updates() ) wieder anzeigen
		gip_sleep(1);
		// Berechne das naechste Spielfeld ...
		// Achtung; Für die Zelle (x,y) darf die Position (x,y) selbst *nicht*
		// mit in die Betrachtungen einbezogen werden.
		// Ausserdem darf bei zellen am rand nicht über den Rand hinausgegriffen
		// werden (diese Zellen haben entsprechend weniger Nachbarn) ...
		// TO DO
		for (int y = 0; y < grid_size; y++) {
			for (int x = 0; x < grid_size; x++) {
				
				int living_neighbors = count_living_neighbors(grid, x, y);
				bool alive = grid[x][y];

				if (alive)
					next_grid[x][y] = !(living_neighbors < 2 || living_neighbors > 3);
				else
					next_grid[x][y] = (living_neighbors == 3);
			}
		}
		// Kopiere das naechste Spielfeld in das aktuelle Spielfeld ...
		// TO DO
		for (int y = 0; y < grid_size; y++) {
			for (int x = 0; x < grid_size; x++) {
				grid[x][y] = next_grid[x][y];
			}
		}
	}
	return 0;
}

void clearInput() {
	cin.clear();
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

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

		cin >> eingabe;
		clearInput();

		// TODO: add exception handling
		/*try {
			cin >> eingabe;
			if (eingabe != 99 && (eingabe < 0 || eingabe > 6))
				throw eingabe;
		}
		catch (...) {
			cout << "Ungueltige Eingabe. Bitte versuchen Sie es erneut." << endl;
			system("PAUSE");
			clearInput();
		}*/

	} while (eingabe != 99 && (eingabe < 0 || eingabe > 6));

	// TODO: maybe adjust this code to be in the loop
	if (eingabe == 0)
	{
		// Erstes Grid vorbelegen (per Zufallszahlen) ...
		// TO DO
		for (int y = 0; y < grid_size; y++) {
			for (int x = 0; x < grid_size; x++) {
				grid[x][y] = gip_random(0, 1);
			}
		}
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
	else if (eingabe == 99)
		exit(0);
}