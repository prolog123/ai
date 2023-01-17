#pragma once

#include "Jugs.h"

#include <vector>

namespace DFS
{
	void printPath();
	std::vector<std::string> search(Jug& jug1, Jug& jug2, const goal& g);
}
