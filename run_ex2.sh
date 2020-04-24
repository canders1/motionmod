for cost in 0.0 0.25 0.5 0.75 1
do
webppl ex2.wppl $cost "gop" > "ex2_gop/ex2_gop_$cost.txt"
webppl ex2.wppl $cost "nogop" > "ex2_nogop/ex2_nogop_$cost.txt"
webppl ex2.wppl $cost "prob" > "ex2_prob/ex2_prob_$cost.txt"
done
cat ex2_gop/ex2_gop_*.txt > ex2_gop/ex2_gop.txt
cat ex2_nogop/ex2_nogop_*.txt > ex2_nogop/ex2_nogop.txt
cat ex2_prob/ex2_prob_*.txt > ex2_prob/ex2_prob.txt
python parse_ex1.py ex2_gop/ex2_gop.txt gop ex2_gop.csv
python parse_ex1.py ex2_nogop/ex2_nogop.txt nogop ex2_nogop.csv
python parse_ex1.py ex2_prob/ex2_prob.txt prob ex2_prob.csv