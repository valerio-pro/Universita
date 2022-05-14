
/* Cheese Problem IN Prolog */

/* Map 3x3, coordinates X (row) and Y (column)
   Chese Position: predicate 
     cheese(X,Y)
	 
   Mouse Position: predicate
     mouse(X,Y)
	 

   State Declaration is a list
   [cheese(XC,YC), mouse(XM, YM)]
   and at every time stamp the list corresponds to the current state of the environment
   
   There is only one cheese is implied by the fact that there is only ONE 
   cheese(X,Y) 
   predicate in the state declaration.
   
   Goal:
   The mouse can stop when there is no further cheese that is falling down
   ======================================================================== */
/*   General Cyle */
run_problem_instance :-
		random_pos_the_cheese(YC),   /* if YC==0 then there is no further cheese 
		                                and the run stop 
		                               At every first move the chese start at XC=3, i.e. the roof */
		random_pose_the_mouse(YM), /* At every first move YM<>0 (i.e. there is always a mouse)
		                              and XM = 1 */
		start_msg([cheese(3,YC), mouse(1,YM)]),
		solve([cheese(3,YC), mouse(1,YM)], 0, Feed),
		write("\n Task carried out: !!"),nl,
		write("The mouse has eaten "), write(Feed), write(" cheese bits!!\n"),nl.
		
solve([cheese(XC,YC), mouse(_,_)], CurrFeed, CurrFeed) :-
        check_goal_satisfaction(cheese(XC,YC)),
		!.
solve([cheese(XC,YC), mouse(XM, YM)], CurrFeed, AllFeeds) :-
		upd_message( [cheese(XC,YC), mouse(XM, YM)] ),
		decide_rule( [cheese(XC,YC), mouse(XM, YM)], CurrFeed, Rule),
		apply_action(Rule, [cheese(XC,YC), mouse(XM, YM)], CurrFeed, NewState, NewFeed),
		write('               ======> Action:  |'), write(Rule),write('|'), nl,
        env_step(NewState, NextState),
		!,
		solve( NextState, NewFeed, AllFeeds).

start_msg([cheese(3,YC), mouse(1,YM)]) :-
		write("--------------------------- Start from -------------------------------"),nl,
		write("State: "), write(cheese(3, YC)), write(" and "), write(mouse(1,YM) ),
		nl.

upd_message( [cheese(XC,YC), mouse(XM, YM)] ) :-
		nl, write('Acting on a state such that:'),nl,
		write('The mouse is in '), write((XM,YM)), write(' and the cheese in '), write((XC, YC)),
		print_state([cheese(XC,YC), mouse(XM, YM)] ).


random_pos_the_cheese(YC) :-  /* if YC==0 then there is no further cheese and the run stop 
		                               At every first move the chese start at XC=3, i.e. the roof */
							YC is random(4).
        

random_pose_the_mouse(YM) :- /* At every first move YM<>0 (i.e. there is always a mouse)
		                              and XM = 1 */	
							YM is random(2)+1.
							
check_goal_satisfaction(cheese(_,0)) :- !. /* No cheese left to eat */


env_step([cheese(1, _), mouse(XM, YM)], [cheese(3, NewYC), mouse(XM, YM)]) :- 
                                /* generate a new starting position at column NewYC */
	random_pos_the_cheese(NewYC),
	nl,
	( NewYC \== 0,
	  write('New cheese bit falling from position: '), print((3, NewYC)), write(' >>> '),
	  readln(_)
	  ;
	  write('No more cheese falling!\n')).

env_step([cheese(XC, YC), mouse(XM, YM)], [cheese(NewXC, YC), mouse(XM, YM)]) :- 
                                                                     /* falling down ...*/
	XC > 1,
	NewXC is XC-1.

/* This is the agent program: the agent here selects the best move for the current 
   world's state of affairs */
decide_rule( [cheese(1, Y), mouse(1,Y)], _, eat) :-
	!.
decide_rule( [cheese(_anyXC, Y), mouse(_anyXM, Y)], _, stand) :-
	\+(_anyXC == _anyXM),
	!.
decide_rule( [cheese(_, NewYC), mouse(_, YM)], _, moveright) :-
    NewYC > YM,
	!.
decide_rule( [cheese(_, NewYC), mouse(_, YM)], _, moveleft) :-
    NewYC < YM,
	!.
decide_rule( _anyState, _anyFeed, _, stand) :-
	!.

/* This is the environment update process: the environment given an action is updated */
apply_action(eat, [cheese(1, YC), mouse(1, YC)], CurrFeed, 
                    [cheese(1, YC), mouse(1, YC)], NewFeed) :- 
	NewFeed is CurrFeed+1.
apply_action(stand, [cheese(NewXC, NewYC), mouse(XM, YM)], CurrFeed, 
                     [cheese(NewXC, NewYC), mouse(XM, YM)], CurrFeed) :- 
	!.
apply_action(moveright, [cheese(NewXC, NewYC), mouse(XM, YM)], CurrFeed, 
                         [cheese(NewXC, NewYC), mouse(XM, NewYM)], CurrFeed) :- 
	NewYM is YM+1,!.
apply_action(moveleft, [cheese(NewXC, NewYC), mouse(XM, YM)], CurrFeed, 
                         [cheese(NewXC, NewYC), mouse(XM, NewYM)], CurrFeed) :- 
	NewYM is YM-1,!.

print_state([cheese(XC,YC), mouse(XM, YM)] ) :-
          nl,write('_____________'),nl,
		  member(X,[3,2,1]),
		  write('|'),
		  ( member(Y,[1,2,3]),
		    print_cell([cheese(XC,YC), mouse(XM, YM)], X, Y),
			write('|')
			;
			nl ),
		   fail.
print_state(_) :- write('_____________'),nl.
			
print_cell([cheese(X,Y), mouse(X, Y)], X, Y) :-			
			  write(' E!'),!.
print_cell([cheese(X,Y), mouse(_, _)], X, Y) :-			
			  write(' C '),!.	  
print_cell([cheese(_,_), mouse(X,Y)], X, Y) :-			
			  write(' M '),!.
print_cell([cheese(_,_), mouse(_,_)], _, _) :-			
			  write('   ') .
		  
		  
		  