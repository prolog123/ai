#pragma once

#include <string>

class Jug
{
public:
	unsigned int water;
	Jug(unsigned int max) noexcept;

	inline bool isEmpty() const noexcept { return water == 0; }
	inline bool isFull() const noexcept { return water == MAX; }

	void fill() noexcept;
	void empty() noexcept;

	void transferFrom(Jug& jug) noexcept;

	void operator= (Jug& j) { water = j.water; }

private:
	void clip() noexcept;

	const unsigned int MAX;
};

struct jugs
{
	Jug one;
	Jug two;

	bool operator== (const jugs& j)
	{
		return ((one.water == j.one.water) && (two.water == j.two.water));
	}
};

struct goal
{
	unsigned int firstJug;
	unsigned int secondJug;
};

std::string toStr(const jugs& jugs);