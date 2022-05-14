/* ADIACENZA LISTE 3*3
 * [1,2,3,
 *  4,5,6,
 *  7,8,9]
 */

adiacente(List,Elem,ListAdiacenti):-
    nth1(1,List,Elem),
    length(ListAdiacenti,2),
    consecElem(Elem,List,Adiacente),
    member(Adiacente,ListAdiacenti),
    elemToNPositionForward(Elem,List,3,Adiacente2),!,
    member(Adiacente2,ListAdiacenti).

adiacente(List,Elem,ListAdiacenti):-
    nth1(9,List,Elem),
    length(ListAdiacenti,2),
    previousElem(Elem,List,Adiacente),
    member(Adiacente,ListAdiacenti),
    elemToNPositionBackward(Elem,List,3,Adiacente2),!,
    member(Adiacente2,ListAdiacenti).

adiacente(List,Elem,ListAdiacenti):-
    nth1(3,List,Elem),
    length(ListAdiacenti,2),
    previousElem(Elem,List,Adiacente),
    elemToNPositionForward(Elem,List,3,Adiacente2),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),!.

adiacente(List,Elem,ListAdiacenti):-
    nth1(4,List,Elem),
    length(ListAdiacenti,3),
    consecElem(Elem,List,Adiacente),
    elemToNPositionBackward(Elem,List,3,Adiacente2),
    elemToNPositionForward(Elem,List,3,Adiacente3),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),!,
    member(Adiacente3,ListAdiacenti).

adiacente(List,Elem,ListAdiacenti):-
    nth1(6,List,Elem),
    length(ListAdiacenti,3),
    previousElem(Elem,List,Adiacente),
    elemToNPositionBackward(Elem,List,3,Adiacente2),
    elemToNPositionForward(Elem,List,3,Adiacente3),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),!,
    member(Adiacente3,ListAdiacenti).

adiacente(List,Elem,ListAdiacenti):-
    nth1(7,List,Elem),
    length(ListAdiacenti,2),
    consecElem(Elem,List,Adiacente),
    elemToNPositionBackward(Elem,List,3,Adiacente2),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),!.

adiacente(List,Elem,ListAdiacenti):-
    nth1(Pos,List,Elem),
    Pos < 10, Pos > 6,
    length(ListAdiacenti,3),
    previousElem(Elem,List,Adiacente),
    consecElem(Elem,List,Adiacente2),
    elemToNPositionBackward(Elem,List,3,Adiacente3),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),
    member(Adiacente3,ListAdiacenti),!.


adiacente(List,Elem,ListAdiacenti):-
    nth1(Pos,List,Elem),
    Pos < 4, Pos > 1,
    length(ListAdiacenti,3),
    previousElem(Elem,List,Adiacente),
    consecElem(Elem,List,Adiacente2),
    elemToNPositionForward(Elem,List,3,Adiacente3),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),!,
    member(Adiacente3,ListAdiacenti).

adiacente(List,Elem,ListAdiacenti):-
    nth1(Pos,List,Elem),
    Pos > 3, Pos < 7,
    length(ListAdiacenti,4),
    previousElem(Elem,List,Adiacente),
    consecElem(Elem,List,Adiacente2),
    elemToNPositionBackward(Elem,List,3,Adiacente3),
    elemToNPositionForward(Elem,List,3,Adiacente4),
    member(Adiacente,ListAdiacenti),
    member(Adiacente2,ListAdiacenti),
    member(Adiacente3,ListAdiacenti),!,
    member(Adiacente4,ListAdiacenti).


consecElem(X,[X,Y|_],Y):- !.
consecElem(Elem,[_|T],ConsecElem):-
    consecElem(Elem,T,ConsecElem).

previousElem(X,[Y,X|_],Y):- !.
previousElem(X,[_|T],Prev):-
    previousElem(X,T,Prev).

% vero se ElementN e' l'elemento della lista List distante N posizioni in avanti 
% da Elem
elemToNPositionForward(Elem,List,N,ElementN):-
    N > 0,
    append(Tmp1,Tmp,List),
    append(_,[Elem],Tmp1),
    nth1(N,Tmp,ElementN),!.

% vero se ElementN e' l'elemento della lista List distante N posizioni all'indietro 
% da Elem
elemToNPositionBackward(Elem,List,N,ElementN):-
    N > 0,
    append(Tmp1,_,List),
    append(Tmp,[Elem],Tmp1),
    length(Tmp,Len),
    Pos is Len-N+1,
    nth1(Pos,Tmp,ElementN),!.
