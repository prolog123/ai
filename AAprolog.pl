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

% Sum of series

% The sum of an empty list is 0.
sum([], 0).
% The sum of a list is the head of the list plus the sum of its tail.
sum([Head|Tail], Sum) :-
    sum(Tail, Sum1),
    Sum is Sum1 + Head.
 
% Generate lsit from 1 to N
generate_list(1, [1]).
generate_list(N, List) :-
    N > 1,
    N1 is N - 1,
    generate_list(N1, List1),
    append(List1, [N], List).
 
series_sum(N, Sum) :-
    generate_list(N, List),
    sum(List, Sum).
