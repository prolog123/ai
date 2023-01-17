#pragma once

#include "Jugs.h"

#include <vector>

namespace BFS 
{
	void printPath();
	std::string finalPath(const std::string& node);
	std::vector<std::string> search(Jug& jug1, Jug& jug2, const goal& g);
}
