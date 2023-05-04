% Factorial
factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Result1),
    Result is N * Result1.

main :-
    write('Enter a number: '),
    read(N),
    factorial(N, Result),
    write('The factorial of '), write(N), write(' is '), write(Result), nl.


% Reverse List
size([],0).
size([_|T],N):-
  size(T,N1),
  N is N1+1.
rev([],[]).
rev([E],[E]).
rev([H|T],R):-
    rev(T,R1),
    append(R1,[H],R).


% Length of List
my_length([_|Tail], Length) :-
    my_length(Tail, Length1),
    Length is Length1 + 1.


% Length + Reverse List
my_length_and_reverse(List, Length, Reversed):-
    my_length(List, Length),
    my_reverse(List, Reversed).
