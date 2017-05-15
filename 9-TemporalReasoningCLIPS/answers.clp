(defrule R1
	(RELATIONS (int1 ?sa) (int2 ?sb) (relations $? ?rab $?))
	(RELATIONS (int1 ?sb) (int2 ?sc) (relations $? ?rbc $?))
	(TABLE (r1 ?rab) (r2 ?rbc) (relations $?rac))
	=>
	(assert (TEMP (nom (str-cat ?rab " " ?rbc)) (int1 ?sa) (int2 ?sb) (relations $?rac)))
)

(defrule R2
	?t1 <- (TEMP (nom ?name1) (int1 ?sa) (int2 ?sb) (relations $?rab1))
	?t2 <- (TEMP (nom ?name2) (int1 ?sa) (int2 ?sb) (relations $?rab2))
	(test (neq ?name1 ?name2))
	=>
	(retract ?t1)
	(retract ?t2)
	(assert (TEMP (nom (str-cat ?name1 " " ?name2)) (int1 ?sa) (int2 ?sb) (relations (UNION $?rab1 $?rab2))))
)

(defrule R3
	(declare (salience -10))
	?t <- (TEMP (int1 ?sa) (int2 ?sb) (relations $?r))
	=>
	(retract ?t)
	(assert (RELATIONS (int1 ?sa) (int2 ?sb) (relations $?r)))
)

(defrule R4
	?rab1 <- (RELATIONS (int1 ?sa) (int2 ?sb) (relations $?r1))
	?rab2 <- (RELATIONS (int1 ?sa) (int2 ?sb) (relations $?r2))
	(test (neq (INTERSECTION $?r1 $?r2) (INTERSECTION $?r2 $?r1)))
	=>
	(retract ?rab1)
	(retract ?rab2)
	(assert (RELATIONS (int1 ?sa) (int2 ?sb) (relations (INTERSECTION $?r1 $?r2))))
)

;(assert (RELATIONS (int1 A) (int2 B) (relations b o m d s)))
;(assert (RELATIONS (int1 B) (int2 C) (relations bi)))
