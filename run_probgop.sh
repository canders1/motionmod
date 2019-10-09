for cost in 0.0 0.25 0.5 0.75 1
do
webppl sample_p_1st.wppl $cost "prob" > "aug_prob/prob_$cost.txt"
done
cat aug_prob/prob_*.txt > aug_prob/aug_prob.txt
python parse_results.py aug_prob/aug_prob.txt prob aug_prob.csv