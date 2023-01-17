#include "TwoJug.h"

#include "Jugs.h"
#include "DFS.h"
#include "BFS.h"

#include <iostream>

void TwoJugs::main()
{
	Jug jug1(5);
	Jug jug2(4);

	std::cout << "\nDFS" << std::endl;
	std::vector<std::string> pathDFS = DFS::search(jug1, jug2, { 2,0 });
	DFS::printPath();

	std::cout << "\nBFS" << std::endl;
	std::vector<std::string> pathBFS = BFS::search(jug1, jug2, { 2,0 });
	BFS::printPath();
}
