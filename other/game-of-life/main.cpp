#define CIMGGIP_MAIN
#include "grid_util.h"

/*This has to be the stupidest project I've done up to date...*/

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

