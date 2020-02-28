for cost in 0.0 0.25 0.5 0.75 1
do
webppl noneven_p_1st.wppl $cost "gop" > "nonu_aug_gop/aug_gop_$cost.txt"
webppl noneven_p_1st.wppl $cost "nogop" > "nonu_aug_nogop/aug_nogop_$cost.txt"
webppl noneven_p_1st.wppl $cost "prob" > "nonu_aug_prob/aug_prob_$cost.txt"
done
cat nonu_aug_gop/aug_gop_*.txt > nonu_aug_gop/aug_gop.txt
cat nonu_aug_nogop/aug_nogop_*.txt > nonu_aug_nogop/aug_nogop.txt
cat nonu_aug_prob/aug_prob_*.txt > nonu_aug_prob/aug_prob.txt
python parse_results.py nonu_aug_gop/aug_gop.txt nonu_gop nonu_aug_gop.csv
python parse_results.py nonu_aug_nogop/aug_nogop.txt nonu_nogop nonu_aug_nogop.csv
python parse_results.py nonu_aug_prob/aug_prob.txt nonu_prob nonu_aug_prob.csv