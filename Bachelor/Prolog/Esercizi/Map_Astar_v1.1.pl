/* Python version
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))
	*/

/* Prolog Version */

arc('Arad', 'Zerind', 75).
arc('Arad', 'Sibiu', 140).
arc('Arad', 'Timisoara', 118).
arc('Bucharest', 'Urziceni', 85).
arc('Bucharest', 'Pitesti', 101).
arc('Bucharest', 'Giurgiu', 90).
arc('Bucharest', 'Fagaras', 211).
arc('Craiova', 'Drobeta', 120).
arc('Craiova', 'Rimnicu', 146).
arc('Craiova', 'Pitesti', 138).
arc('Drobeta', 'Mehadia', 75).
arc('Eforie', 'Hirsova', 86).
arc('Fagaras', 'Sibiu', 99).
arc('Hirsova', 'Urziceni', 98).
arc('Iasi', 'Vaslui', 92).
arc('Iasi', 'Neamt', 87).
arc('Lugoj', 'Timisoara', 111).
arc('Lugoj', 'Mehadia', 70).
arc('Oradea', 'Zerind', 71).
arc('Oradea', 'Sibiu', 151).
arc('Pitesti', 'Rimnicu', 97).
arc('Rimnicu', 'Sibiu', 80).
arc('Urziceni', 'Vaslui', 142). 


loc('Arad', 91, 492). 
loc('Bucharest', 400, 327). 
loc('Craiova', 253, 288).
loc('Drobeta', 165, 299). 
loc('Eforie', 562, 293). 
loc('Fagaras', 305, 449).
loc('Giurgiu', 375, 270). 
loc('Hirsova', 534, 350). 
loc('Iasi', 473, 506).
loc('Lugoj', 165, 379). 
loc('Mehadia', 168, 339). 
loc('Neamt', 406, 537).
loc('Oradea', 131, 571). 
loc('Pitesti', 320, 368). 
loc('Rimnicu', 233, 410).
loc('Sibiu', 207, 457). 
loc('Timisoara', 94, 410). 
loc('Urziceni', 456, 350).
loc('Vaslui', 509, 444). 
loc('Zerind', 108, 531).

/* Prolog as a Relational system 

  query1: Which cities have distances higher than 100?
   SQL:
      SELECT FROMNODE, TONODE 
	  FROM ARC
	  WHERE DISTANCE > 100 */

query1(FromNode, ToNode) :-
	arc(FromNode, ToNode, D),
	D>100.

query1_1(NodePairs, D) :-
	select_pairs(NodePairs, D).

select_pairs(Nodes, D):-
	setof((FromNode,ToNode), Dist^(arc(FromNode, ToNode, Dist), Dist>D), Nodes).

/* Query2: Which are the locations of cities that are farer than 100 from some other ones?
   SQL:
      SELECT FROMNODE, LAT, LONG 
	  FROM ARC, LOC
	  WHERE ( DISTANCE > 100 AND LOC.NODE = ARC.FROMNODE) 
	                                                                  */ 

query2(FromNode, Lat, Long) :-
	arc(FromNode, _, D),
	D>100,
	loc(FromNode, Lat, Long).

query2_1(FromNode, FinalNodes, D) :-
	select(FromNode, Nodes, D),
	add_locs(Nodes, FinalNodes).
	

select(Nodes, D):-
	setof(FromNode, Dist^T^(arc(FromNode, T, Dist), Dist>D), Nodes).
	

	  

/* Query3: Which cities are reachable with two hops from X?
   SQL:
      SELECT FROMNODE, LAT, LONG 
	  FROM ARC AS A1, ARC AS A2, LOC
	  WHERE ( DISTANCE > 100 AND LOC.NODE = ARC.FROMNODE) 
	                                                                  */ 
query3(FromNode, A) :-
	go(FromNode,T, _), go(T, A, _), A\== FromNode.
	
query3_1(FromNode, FinalNodes) :-
	setof(Nodes, query3(FromNode, Nodes), FinalNodes).
	
go(A,B,K) :-
	(arc(A,B,K);arc(B,A,K)).
	
add_locs([], []).
add_locs([H|Nodes], [(H,Lat,Long)|FinalNodes]) :-
	loc(H, Lat, Long),
	add_locs(Nodes, FinalNodes).


/* A-star Solving */
solve(Start, Soln, Function) :- 
	f_function_new(Start, 0, 0, F), /* Heuristic function */
	/* Search over active successors/states
		One successor is a 4-ple:
		- Current Node 
		- Current Depth D
		- Current Incurred Cost
		- Current Estimated Cost F 
		- Current Solution (in reverse order) */
	search([(Start,0, 0, F,[])], S, Function), 
	reverse(S,Soln).


/* f defined as arc cost plus heuristic cost: g(n) + h(n) */
f_function_new(State, IncurredCost, ArcCost, F) :- 
	h_function_ed(State, IncurredCost, H),
	F is ArcCost + H.

/* heuristics of local arc cost */
h_function(_State, Cost, Cost).
/* heuristics: distance to target */   
h_function_ed(State, _, H) :- 
    euclidean_dist_to_goal(State, H). 

euclidean_dist_to_goal(State, H) :-
	goal(Target),
	loc(State, X1,Y1),
	loc(Target, X2, Y2),
	H is sqrt( (X1-X2)*(X1-X2) + (Y1-Y2)*(Y1-Y2) ). 

search([], [], _) :- fail.
search([(State, _D, IncurredCost, _, Soln) | _], Soln, IncurredCost) :- 
						goal(State).
search([ State | Frontier], Solution, IncurredCost) :- 
					  write('Expanding ...  \n'), write(State),write('\n'), 
                      expand(State, Nodes_from_State),
					  estimate(State, Nodes_from_State, Candidates),
					  /* write('Candidates: '), write(Candidates),nl,*/
					  insert_all(Candidates, Frontier, NewFrontier),
                      /* write('\nContinuation from: '),nl,
					   mine_print(NewFrontier), write('RecCall...\n\n'),
					  nl,nl,*/
					  search(NewFrontier, Solution, IncurredCost).

mine_print([]).
mine_print([(State, Depth, Incurred, Estimated, RevPat)| _ ]) :-
						tab(1),print('State: '),print(State),nl,
						tab(1),print('Depth: '),print(Depth),nl,
						tab(1),print('Incurred: '),print(Incurred),nl,
						tab(1),print('Estimated: '),print(Estimated),nl,
						tab(1),print('RevPath: '),print(RevPat), nl.

/* 
The version of the 'expand' predicate given here simply uses Prolog's bagof computation 
(thus bundling up a lot of work).

bagof(+Template, :Goal, -Bag)
*/
expand((State, _, _, _, Ancestors), AllNodeFromState) :-
			 bagof(
				(Child, ArcCost, [Move|Ancestors]), 
				(Child, ArcCost, Move)^move(State, Child, ArcCost, Move),
				AllNodeFromState
				).

estimate(_, [], []) :-!.
estimate((State, Depth, IncurredCost, EC, Ancestors), 
             [(Child, ArcCost, [Move|Ancestors]) | OtherChildren], 
             [(Child, NDepth, NewIncurredCost, EstimatedCost, [Move|Ancestors]) | AlltheRest] ) :-
						
			NDepth is Depth + 1,
            \+ inpath(Child, Ancestors),
            f_function_new(Child, IncurredCost, ArcCost, F),
			NewIncurredCost is IncurredCost+ArcCost,
			EstimatedCost is IncurredCost+F,
			!,
			estimate((State, Depth, IncurredCost, EC, Ancestors), 
							OtherChildren, AlltheRest).

estimate((State, Depth, IncurredCost, EC, Ancestors), [_| OtherChildren], AlltheRest ) :-
			 !,
			 estimate((State, Depth, IncurredCost, EC, Ancestors), OtherChildren, AlltheRest).

/*
inpath considers the path as a list of arcs of nodes
(Node1, Node2) means there's an arc between them
*/
inpath(Child, [(Child,_)|_]) :-!.
inpath(Child, [(_,Child)|_]) :-!.
inpath(Child, [_|Rest]) :-
		inpath(Child, Rest).


/*
The (application dependent) 'move' predicate should generate the 'Child' states, 
in such a way as to obtain them all by backtracking. 
(See the 8-puzzle example in the next section.) 
As previously stated, the 'Move' can either be the the whole parent node itself
or some appropriate substitute. 
(Actually, one should rewrite the 'expand' clause if one is going to use the whole node,
rather than some symbolic representation, as we do in the next section.)
*/
move(State, Child, Cost, (State,Child)) :-
	arc(State, Child, Cost).
move(State, Child, Cost, (State,Child)) :-
	arc(Child, State, Cost).

insert_all([F|R],Open1,Open3) :- 
	ordered_insert(F,Open1,Open2),
    insert_all(R,Open2,Open3).
	
insert_all([],Open,Open).

ordered_insert(B, Open, Open) :- repeated_node(B,Open), !.
ordered_insert(B, [C|R], [B|R]) :- cheaper_alternative(B,C),!.
ordered_insert(B, [C|R], [B,C|R]) :- cheaper(B,C), !.
ordered_insert(B,[B1|R],[B1|S]) :- ordered_insert(B, R, S).
ordered_insert(B,[],[B]).

repeated_node((Node,D,IC,EC,_), [(Node,D,IC,EC,_)|_]) :- !.
repeated_node(State, [_|Tail]) :- repeated_node(State,Tail), !. 

cheaper_alternative( (Node,_,_,EC1,_), (Node,_,_,EC2,_) ) :- EC1 <  EC2.
cheaper( (_,_,_,EC1,_), (_,_,_,EC2,_) ) :- EC1 <  EC2.

/* logging predicates */
pretty_write([]).
pretty_write([(St,End)]) :-
	write(St),
	write(' -> '), write(End),
	!.
pretty_write([(St,_) | Rest]) :-
	write(St), write(' -> '),
	!,
	pretty_write(Rest).

/* main predicate */
makepath(Source, Target, Sol) :-
	abolish(goal/1),
	assert(goal(Target)),
	solve(Source, Sol, Cost),
	nl,
	write('The Solution is: '), pretty_write(Sol), write(' with Cost: '), write(Cost),nl,
	nl, write('Done!!\n').
	
	
/* calls default path to test */
go:-makepath('Arad','Bucharest', _Sol).

/* calls path from Arad to X */
go(X):-makepath('Arad',X, Sol), nl,nl, write(Sol),nl.

