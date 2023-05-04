size([],0).
size([_|T],N):-size(T,N1),N is N1+1.
rev([],[]).
rev([E],[E]).
rev([H|T],R):-
    rev(T,R1),
    append(R1,[H],R).
