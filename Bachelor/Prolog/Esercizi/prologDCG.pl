% Formazione di predicati "verbo(nome1,nome2)" per ottenere una semantica formale
% dal linguaggio naturale

% Una query ?- s(Pred,[giuseppe,corre],[]) restituisce il 
% predicato "corre(giuseppe)"

% Una query ?- s(_,[giuseppe,corre],[]) e' true se "corre(giuseppe)" puo' essere
% derivato all'interno della grammatica

% Una "frase" e' composta da una "frase nominale" (np) seguita da una 
% "frase verbale" (vp)

% DCG --> "Definite Clause Grammars"

% Al posto di ottenere predicati della logica del primo ordine si puo' ottenere
% la derivazione effettuata con:
% 
%								s(s(np(N),vp(V))) --> np(N), vp(V).
%								s(s(np(N),vp(V,N1))) --> np(N), vp(V,N1).
%								vp(v(V)) --> v(V).
%								...
%								...
%								np(n(N)) --> det(_), n(N).
%								...
%								...
%								n(nome) --> [nome].
%								...
%								...
%								v(verbo) --> [verbo].


s(Pred) --> np(N), vp(V), {Pred =.. [V,N]}.
s(Pred) --> np(N), vp(V,N1), {Pred =.. [V,N,N1]}, !.
    
np(N) --> n(N).
np(N) --> det(_), n(N).

vp(V) --> v(V).
vp(V,N) --> v(V), np(N).
vp(V,N) --> v(V), pp(N).

pp(N) --> prep(_), np(N).

det(il) --> [il].
det(lo) --> [lo].
det(la) --> [la].
det(i) --> [i].
det(gli) --> [gli].
det(le) --> [le].

prep(di) --> [di].
prep(a) --> [a].
prep(da) --> [da].
prep(in) --> [in].
prep(con) --> [con].
prep(su) --> [su].
prep(per) --> [per].
prep(tra) --> [tra].
prep(fra) --> [fra].

n(giuseppe) --> [giuseppe].
n(mario) --> [mario].
n(valerio) --> [valerio].
n(mela) --> [mela].
n(acqua) --> [acqua].
n(vino) --> [vino].
n(matita) --> [matita].

v(scrive) --> [scrive].
v(beve) --> [beve].
v(corre) --> [corre].
v(mangia) --> [mangia].


/** <examples>
?- s(Pred,[giuseppe,scrive,con,la,matita],[]).
?- s(Pred,[giuseppe,mangia,la,mela],[]).
?- s(_,[giuseppe,mangia,la,mela],[]).
*/
