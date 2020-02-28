for cost in 0.0 0.25 0.5 0.75 1
do
webppl simple_p_1st.wppl $cost "gop" > "simple_gop/simple_gop_$cost.txt"
webppl simple_p_1st.wppl $cost "nogop" > "simple_nogop/simple_nogop_$cost.txt"
webppl simple_p_1st.wppl $cost "prob" > "simple_prob/simple_prob_$cost.txt"
done
cat simple_gop/simple_gop_*.txt > simple_gop/simple_gop.txt
cat simple_nogop/simple_nogop_*.txt > simple_nogop/simple_nogop.txt
cat simple_prob/simple_prob_*.txt > simple_prob/simple_prob.txt
python parse_results.py simple_gop/simple_gop.txt gop simple_gop.csv
python parse_results.py simple_nogop/simple_nogop.txt nogop simple_nogop.csv
python parse_results.py simple_prob/simple_prob.txt prob simple_prob.csv