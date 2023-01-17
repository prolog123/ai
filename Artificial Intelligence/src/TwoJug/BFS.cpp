#include "BFS.h"

#include <unordered_map>

#include <iostream>

static std::vector<jugs> queue;
static unsigned int q_front = 0;
static std::unordered_map<std::string, std::vector<std::string>> neighbours;
static std::vector<std::string> path;

namespace BFS
{
	void printPath()
	{
		std::cout << "Traversal Path:" << std::endl;
		for (auto& pair : queue)
			std::cout << "(" << pair.one.water << ", " << pair.two.water << ") ";
		std::cout << std::endl;

		std::cout << "Final Path:" << std::endl;
		for (auto& pair : path)
			std::cout << pair << " ";
		std::cout << std::endl;
	}

	std::string finalPath(const std::string& node)
	{
		// std::cout << node << " ";
		path.push_back(node);
		for (auto& pair : neighbours)
		{
			if (std::find(pair.second.begin(), pair.second.end(), node) != pair.second.end())
			{
				return finalPath(pair.first);
			}
		}
		return "";
	}

	std::vector<std::string> search(Jug& jug1, Jug& jug2, const goal& g)
	{
		queue.push_back({ jug1, jug2 });
		while (!(jug1.water == g.firstJug && jug2.water == g.secondJug))
		{
			std::string parent = toStr(queue[q_front]);
			neighbours[parent] = std::vector<std::string>();

			++q_front;
			{
				Jug j1 = jug1;
				Jug j2 = jug2;

				if (!j1.isFull())
				{
					j1.fill();
					jugs j = { j1, jug2 };
					if (std::find(queue.begin(), queue.end(), j) == queue.end())
					{
						queue.push_back({ j1, jug2 });
						neighbours[parent].push_back(toStr({ j1, jug2 }));
					}
				}
				if (!j2.isFull())
				{
					j2.fill();
					jugs j = { jug1, j2 };
					if (std::find(queue.begin(), queue.end(), j) == queue.end())
					{
						queue.push_back({ jug1, j2 });
						neighbours[parent].push_back(toStr({ jug1, j2 }));
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
					if (std::find(queue.begin(), queue.end(), j) == queue.end())
					{
						queue.push_back({ j1, jug2 });
						neighbours[parent].push_back(toStr({ j1, jug2 }));
					}
				}
				if (!j2.isEmpty())
				{
					j2.empty();
					jugs j = { jug1, j2 };
					if (std::find(queue.begin(), queue.end(), j) == queue.end())
					{
						queue.push_back({ jug1, j2 });
						neighbours[parent].push_back(toStr({ jug1, j2 }));
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
					if (std::find(queue.begin(), queue.end(), j) == queue.end())
					{
						queue.push_back({ j1, j2 });
						neighbours[parent].push_back(toStr({ j1, j2 }));
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
					if (std::find(queue.begin(), queue.end(), j) == queue.end())
					{
						queue.push_back({ j1, j2 });
						neighbours[parent].push_back(toStr({ j1, j2 }));
					}
				}
			}

			jug1 = queue[q_front].one;
			jug2 = queue[q_front].two;
		}

		finalPath(toStr(queue[q_front]));

		return path;
	}
}
