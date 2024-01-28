#include <iostream>
#include <string>
#include <limits>
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
			// TODO: summarize the following pattern code and don't repeat yourself
		case 1: {
			//const int pattern_size_1 = 3;
			char pattern[3][3] =
			{
			{ '.', '*', '.' },
			{ '*', '.', '*' },
			{ '.', '*', '.' },
			};
			for (int y = 0; y < 3; y++)
				for (int x = 0; x < 3; x++)
					if (pattern[y][x] == '*')
						grid[x][y + 3] = true;
		}
		break;
		case 2: {
			//const int pattern_size_2 = 3;
			char pattern[3][3] =
			{
			{ '.', '*', '.' },
			{ '.', '*', '.' },
			{ '.', '*', '.' },
			};
			for (int y = 0; y < 3; y++)
				for (int x = 0; x < 3; x++)
					if (pattern[y][x] == '*')
						grid[x][y + 3] = true;
		}
		break;
		case 3: {
			//const int pattern_size_3 = 8;
			char pattern[8][8] =
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
			for (int y = 0; y < 8; y++)
				for (int x = 0; x < 8; x++)
					if (pattern[y][x] == '*')
						grid[x][y + 1] = true;
		}
		break;
		case 4: {
			//const int pattern_size_4 = 3;
			char pattern[3][3] =
			{
			{ '.', '*', '.' },
			{ '.', '.', '*' },
			{ '*', '*', '*' },
			};
			for (int y = 0; y < 3; y++)
				for (int x = 0; x < 3; x++)
					if (pattern[y][x] == '*')
						grid[x][y + 3] = true;
		}
		break;
		case 5: {
			//const int pattern_size_5 = 5;
			char pattern[5][5] =
			{
			{ '*', '.', '.', '*', '.' },
			{ '.', '.', '.', '.', '*' },
			{ '*', '.', '.', '.', '*' },
			{ '.', '*', '*', '*', '*' },
			{ '.', '.', '.', '.', '.' },
			};
			for (int y = 0; y < 5; y++)
				for (int x = 0; x < 5; x++)
					if (pattern[y][x] == '*')
						grid[x][y + 3] = true;
		}
		break;
		case 6: {
			//const int pattern_size_6 = 6;
			char pattern[6][6] =
			{
			{ '.', '*', '*', '*', '*', '*' },
			{ '*', '.', '.', '.', '.', '*' },
			{ '.', '.', '.', '.', '.', '*' },
			{ '*', '.', '.', '.', '*', '.' },
			{ '.', '.', '*', '.', '.', '.' },
			{ '.', '.', '.', '.', '.', '.' },
			};
			for (int y = 0; y < 6; y++)
				for (int x = 0; x < 6; x++)
					if (pattern[y][x] == '*')
						grid[x][y + 3] = true;
		}
		break;
		case 99:
			exit(0);
		default:
			cout << "Ungueltige Auswahl. Bitte erneut waehlen." << endl;
			break;
		}
	} while (eingabe != 99);
}
