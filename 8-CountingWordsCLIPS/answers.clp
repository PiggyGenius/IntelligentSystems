(defrule MAIN::MakeFirstWordPair
   (Paragraph ?category $? ?w1 ?w2 $?)
   (not (WordPair (CATEGORY ?category)))
   =>
   (assert (WordPair (CATEGORY ?category) (WORD1 ?w1) (WORD2 ?w2) (COUNT 0)))
   (assert (Category (NAME ?category) (M 0))))


(defrule MAIN::MakeWordPair
   (Paragraph ?category $? ?w1 ?w2 $?)
   (not (WordPair (CATEGORY ?category) (WORD1 ?w1) (WORD2 ?w2)))
   ?c <- (Category (NAME ?category) (M ?m))
   =>
   (assert (WordPair (CATEGORY ?category) (WORD1 ?w1) (WORD2 ?w2) (COUNT 0))))


(defrule MAIN::CountWordPairs
   (declare (salience -10))
   ?p <- (Paragraph ?category ?w1 ?w2 $?b)
   ?wp <- (WordPair (CATEGORY ?category) (WORD1 ?w1) (WORD2 ?w2) (COUNT ?wc))
   ?c <- (Category (NAME ?category) (M ?m))
   =>
   (modify ?wp (COUNT (+ ?wc 1)))
   (modify ?c (M (+ ?m 1)))
   (retract ?p)
   (assert (Paragraph ?category ?w2 $?b)))

(defrule CountPairsForAllCategories
   (declare (salience -20))
   ?wp <- (WordPair (WORD1 ?w1) (WORD2 ?w2))
   =>
   (bind ?count 0)
   (do-for-all-facts ((?wpa WordPair)) TRUE
	   (if (and (and (eq ?w1 ?wpa:WORD1) (eq ?w2 ?wpa:WORD2)) (neq ?wpa:CATEGORY All)) then
	      (bind ?count (+ ?count ?wpa:COUNT))))
   (assert (WordPair (CATEGORY All) (WORD1 ?w1) (WORD2 ?w2) (COUNT ?count))))

(defrule PrintMostFrequentWordPair
   (declare (salience -30))
   (WordPair (CATEGORY ?category) (WORD1 ?w1) (WORD2 ?w2) (COUNT ?wc))
   (not (WordPair (CATEGORY ?category) (WORD1 ?) (WORD2 ?) (COUNT ?wcg&:(> ?wcg ?wc))))
   =>
   (printout t "The most frequent word pair in category " ?category " is " ?w1 " " ?w2 " with count " ?wc crlf))
