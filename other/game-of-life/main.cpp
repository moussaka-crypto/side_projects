#define CIMGGIP_MAIN
#include "grid_util.h"

/*
* Inspired by https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
* This has to be the stupidest project I've done up to date.
* Enjoy or something...
*/
int main()
{
	bool grid[grid_size][grid_size] = { 0 };
	bool next_grid[grid_size][grid_size] = { 0 };
	init_grid(grid);
	while (gip_window_not_closed())
	{
		gip_white_background();
		gip_stop_updates(); 
		for (int y = 0; y < grid_size; ++y) {
			for (int x = 0; x < grid_size; ++x) {

				unsigned char* cellColor = grid[x][y] ? gip_rgb(153, 255, 51) : gip_rgb(40, 0, 80);

				gip_draw_rectangle(
					border + x * box_size, border + y * box_size,
					border + (x + 1) * box_size, border + (y + 1) * box_size,
					cellColor);
			}
		}
		gip_start_updates(); 
		gip_sleep(1);
		for (int y = 0; y < grid_size; y++) {
			for (int x = 0; x < grid_size; x++) {
				
				int living_neighbors = count_living_neighbors(grid, x, y);

				if (grid[x][y])
					next_grid[x][y] = !(living_neighbors < 2 || living_neighbors > 3);
				else
					next_grid[x][y] = (living_neighbors == 3);
			}
		}
		for (int y = 0; y < grid_size; y++) {
			for (int x = 0; x < grid_size; x++) {
				grid[x][y] = next_grid[x][y];
			}
		}
	}
	return 0;
}
