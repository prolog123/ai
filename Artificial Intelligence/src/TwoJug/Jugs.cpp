#include "Jugs.h"

Jug::Jug(unsigned int max) noexcept 
	: water(0), MAX(max) {}

void Jug::fill() noexcept 
{
	water = MAX;
}

void Jug::empty() noexcept
{
	water = 0;
}

void Jug::transferFrom(Jug& jug) noexcept

{
	unsigned int oldValue = water;
	water += jug.water;
	clip();

	jug.water -= water - oldValue;
}

void Jug::clip() noexcept
{
	if (water > MAX) water = MAX;
	// else if (water < 0) water = 0;
}

std::string toStr(const jugs& jugs)
{
	std::string str = "(";
	str += std::to_string(jugs.one.water);
	str += ", ";
	str += std::to_string(jugs.two.water);
	str += ")";

	return str;
}
