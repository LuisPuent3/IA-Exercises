% Base de conocimiento médica simple

% Hechos: síntomas y enfermedades
sintoma(juan, fiebre).
sintoma(juan, tos).
sintoma(juan, dolor_cabeza).
sintoma(pedro, congestion_nasal).
sintoma(pedro, estornudos).
sintoma(pedro, picazon_ojos).

% Reglas para diagnóstico
enfermedad(Persona, gripe) :-
    sintoma(Persona, fiebre),
    sintoma(Persona, tos).

enfermedad(Persona, resfriado) :-
    sintoma(Persona, congestion_nasal),
    sintoma(Persona, estornudos).

enfermedad(Persona, alergia) :-
    sintoma(Persona, estornudos),
    sintoma(Persona, picazon_ojos),
    not(sintoma(Persona, fiebre)).

% Reglas para tratamiento
tratamiento(Persona, descanso_y_liquidos) :-
    enfermedad(Persona, gripe).

tratamiento(Persona, antihistaminicos) :-
    enfermedad(Persona, alergia).

tratamiento(Persona, vitamina_c) :-
    enfermedad(Persona, resfriado).

% Consultas de ejemplo:
% ?- enfermedad(juan, X).
% X = gripe.

% ?- tratamiento(juan, X).
% X = descanso_y_liquidos.

% ?- enfermedad(pedro, X).
% X = resfriado ;
% X = alergia.

halt.