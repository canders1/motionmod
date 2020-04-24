for cost in 0.0 0.25 0.5 0.75 1
do
webppl ex1.wppl $cost "gop" > "ex1_gop/ex1_gop_$cost.txt"
webppl ex1.wppl $cost "nogop" > "ex1_nogop/ex1_nogop_$cost.txt"
webppl ex1.wppl $cost "prob" > "ex1_prob/ex1_prob_$cost.txt"
done
cat ex1_gop/ex1_gop_*.txt > ex1_gop/ex1_gop.txt
cat ex1_nogop/ex1_nogop_*.txt > ex1_nogop/ex1_nogop.txt
cat ex1_prob/ex1_prob_*.txt > ex1_prob/ex1_prob.txt
python parse_ex1.py ex1_gop/ex1_gop.txt gop ex1_gop.csv
python parse_ex1.py ex1_nogop/ex1_nogop.txt nogop ex1_nogop.csv
python parse_ex1.py ex1_prob/ex1_prob.txt prob ex1_prob.csv
