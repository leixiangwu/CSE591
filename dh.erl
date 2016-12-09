-module(dh).
-export([start/0, diffie_start/0, hellman_start/0, genereate_prime_base/0, genereate_prime_modulo/0, genereate_hellman_secret/0, genereate_diffie_secret/0, dh_cal/3]).

% 1. A->B: P, G
% 2. A->B: kap(P, G, Xa)
% 3. B->A: kap(P, G, Xb)
% 4. A->B: {one()}kap(P, kap(P, G, Xb), Xa)

% generate a prime base
genereate_prime_base() ->
	3.

% generate a prime modolo
genereate_prime_modulo() ->
    883.

% generate a secret key
genereate_hellman_secret() ->
	4.

% generate a secret key
genereate_diffie_secret() ->
    5.

% Encrypt the message using the given secret key
% encrypt(msg, secret_key) ->
    % msg.

% Decrypt the message using the given secret key
% decrypt(msg, secret_key)->
    % msg.

dh_cal(Base, Power, Mod)->
    X = math:pow(Base, Power),
    round(X) rem Mod.

diffie_start() ->
	receive
		{receive_hellman, Hellman} ->
	    	G = genereate_prime_base(),
	    	P = genereate_prime_modulo(),
			% Step 1
			io:format("Diffie ~p sends g = ~p and p = ~p to Hellman ~p~n", [self(), G, P, Hellman]),
			Hellman ! {g_and_p, G, P, self()},
			diffie_start();
		{received_g_p, G, P, Hellman} ->
			% Step 1 is done
		    Diffie_A = dh:genereate_diffie_secret(),
			% Step 2
			A = dh_cal(G, Diffie_A, P),
			io:format("Diffie ~p sends A = ~p to Hellman ~p~n", [self(), A, Hellman]),
			Hellman ! {send_A, G, P, A, self()},
			diffie_start();
			% Step 2 is done
		{send_B, P, B} ->
		    Diffie_A = dh:genereate_diffie_secret(),
        	Secret = dh_cal(B, Diffie_A, P),
        	io:format("Diffie's secret key is ~p~n", [Secret])
    end.

hellman_start() ->
    receive
    	{g_and_p, G, P, Diffie} ->
	        io:format("Hellman ~p received g = ~p and p = ~p from Diffie ~p~n", [self(), G, P, Diffie]),
	        Diffie ! {received_g_p, G, P, self()},
	        hellman_start();
		{send_A, G, P, A, Diffie} ->
		    Diffie_B = genereate_hellman_secret(),
	        Secret = dh_cal(A, Diffie_B, P),
        	io:format("Hellman's secret key is ~p~n", [Secret]),
        	% Step 3
	        B = dh_cal(G, Diffie_B, P),
        	io:format("Hellman ~p sends B = ~p to Diffie ~p~n", [self(), B, Diffie]),
			Diffie ! {send_B, P, B}
	    	% Step 3 is done
	end.

start()->
	Diffie_PID = spawn(dh, diffie_start, []),
	Hellman_Pid = spawn(dh, hellman_start, []),
	Diffie_PID ! {receive_hellman, Hellman_Pid}.

% def main():
%     diffie = new(Diffie)
%     hellman = new(Hellman)
%     setup(diffie, (hellman,))
%     setup(hellman, (diffie,))
%     start(hellman)
%     start(diffie)
