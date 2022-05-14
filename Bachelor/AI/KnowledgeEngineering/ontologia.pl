% Definizione di Ontologia

% Il predicato "categoria" indica le categorie piu' generali
categoria(oggettoFisico).
categoria(tempo).
categoria(luogo).

% I predicati "is_a" indicano le relazioni tra le categorie. Un "ostacolo"
% e' un "oggettoFisico", una "buca" e' un "ostacolo", e cosi' via...
is_a(ostacolo,oggettoFisico).
is_a(agente,oggettoFisico).
is_a(buca,ostacolo).
is_a(drago,ostacolo).

% Il predicato "sp(X,Y)" stabilisce il concetto di specializzazione tra categorie.
% La categoria "X" specializza la categoria "Y"
sp(X,Y):-
    is_a(X,Y).
sp(X,Y):-
    is_a(X,Z),
    sp(Z,Y).
