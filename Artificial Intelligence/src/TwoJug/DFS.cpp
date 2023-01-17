#include "DFS.h"

#include <list>
#include <iostream>

static std::vector<jugs> stack;
static unsigned int s_top = -1;
static std::vector<std::string> path;

namespace DFS
{
	void printPath()
	{
		std::cout << "Path: ";
		for (auto& pair : path)
			std::cout << pair << " ";
		std::cout << std::endl;
	}

	std::vector<std::string> search(Jug& jug1, Jug& jug2, const goal& g)
	{
		stack.push_back({ jug1, jug2 });
		++s_top;
		if (!(jug1.water == g.firstJug && jug2.water == g.secondJug))
		{
			{
				Jug j1 = jug1;
				Jug j2 = jug2;

				if (!j1.isFull())
				{
					j1.fill();
					jugs j = { j1, jug2 };
					if (std::find(stack.begin(), stack.end(), j) == stack.end())
					{
						path.push_back(toStr({ j1, jug2 }));
						return search(j1, jug2, g);
					}
				}
				if (!j2.isFull())
				{
					j2.fill();
					jugs j = { jug1, j2 };
					if (std::find(stack.begin(), stack.end(), j) == stack.end())
					{
						path.push_back(toStr({ jug1, j2 }));
						return search(jug1, j2, g);
					}
				}
			}

			{
				Jug j1 = jug1;
				Jug j2 = jug2;

				if (!j1.isEmpty())
				{
					j1.empty();
					jugs j = { j1, jug2 };
					if (std::find(stack.begin(), stack.end(), j) == stack.end())
					{
						path.push_back(toStr({ j1, jug2 }));
						return search(j1, jug2, g);
					}
				}
				if (!j2.isEmpty())
				{
					j2.empty();
					jugs j = { jug1, j2 };
					if (std::find(stack.begin(), stack.end(), j) == stack.end())
					{
						path.push_back(toStr({ jug1, j2 }));
						return search(jug1, j2, g);
					}
				}
			}

			{
				Jug j1 = jug1;
				Jug j2 = jug2;

				if (!j1.isEmpty())
				{
					j2.transferFrom(j1);
					jugs j = { j1, j2 };
					if (std::find(stack.begin(), stack.end(), j) == stack.end())
					{
						path.push_back(toStr({ j1, j2 }));
						return search(j1, j2, g);
					}
				}
			}

			{
				Jug j1 = jug1;
				Jug j2 = jug2;

				if (!j2.isEmpty())
				{
					j1.transferFrom(j2);
					jugs j = { j1, j2 };
					if (std::find(stack.begin(), stack.end(), j) == stack.end())
					{
						path.push_back(toStr({ j1, j2 }));
						return search(j1, j2, g);
					}
				}
			}
		}

		return path;
	}
}
