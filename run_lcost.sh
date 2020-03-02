for cost in 0.0 0.25 0.5 0.75 1
do
webppl lcost.wppl $cost "gop" > "lcost_gop/lcost_gop_$cost.txt"
webppl lcost.wppl $cost "nogop" > "lcost_nogop/lcost_nogop_$cost.txt"
webppl lcost.wppl $cost "prob" > "lcost_prob/lcost_prob_$cost.txt"
done
cat lcost_gop/lcost_gop_*.txt > lcost_gop/lcost_gop.txt
cat lcost_nogop/lcost_nogop_*.txt > lcost_nogop/lcost_nogop.txt
cat lcost_prob/lcost_prob_*.txt > lcost_prob/lcost_prob.txt
python parse_results.py lcost_gop/lcost_gop.txt lcost_gop lcost_gop.csv
python parse_results.py lcost_nogop/lcost_nogop.txt lcost_nogop lcost_nogop.csv
python parse_results.py lcost_prob/lcost_prob.txt lcost_prob lcost_prob.csv