let rec gcd a b =
if b = 0 then a else gcd b (a mod b);;

let rec pi max i c =
let x = Random.int max in
let y = Random.int max in
let this = (if gcd x y = 1 then 1.0 else 0.0) in

let _ = print_string "Round #" in
let _ = print_float i in
let _ = print_endline "" in

let _ = print_string "Die size: " in
let _ = print_int max in
let _ = print_endline "" in

let r = ( c+.this ) /. i in
let _ = print_string "Guess for π: " in
let _ = print_float( (6. /. r)** 0.5 ) in
let _ = print_string "\n" in

let _ = print_string "New die size: " in
let new_max = read_line () in
let new_max = ( try
		int_of_string new_max
		with Failure _ -> max ) in
let _ = print_endline "" in

(pi new_max (i+.1.0) (c+.this) );;

pi 64 1.0 1.0;;

