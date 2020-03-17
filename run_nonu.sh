for cost in 0.0 0.25 0.5 0.75 1
do
webppl noneven_together_p_1st.wppl $cost "gop" > "nonu_aug_gop/aug_gop_$cost.txt"
webppl noneven_together_p_1st.wppl $cost "nogop" > "nonu_aug_nogop/aug_nogop_$cost.txt"
webppl noneven_together_p_1st.wppl $cost "prob" > "nonu_aug_prob/aug_prob_$cost.txt"

webppl noneven_apart_p_1st.wppl $cost "gop" > "nonu_apart_gop/aug_gop_$cost.txt"
webppl noneven_apart_p_1st.wppl $cost "nogop" > "nonu_apart_nogop/aug_nogop_$cost.txt"
webppl noneven_apart_p_1st.wppl $cost "prob" > "nonu_apart_prob/aug_prob_$cost.txt"

webppl noneven_together_p_1st.wppl $cost "gop" "speaker"> "speak_nonu_aug_gop/aug_gop_$cost.txt"
webppl noneven_together_p_1st.wppl $cost "nogop" "speaker"> "speak_nonu_aug_nogop/aug_nogop_$cost.txt"
webppl noneven_together_p_1st.wppl $cost "prob" "speaker"> "speak_nonu_aug_prob/aug_prob_$cost.txt"

webppl noneven_apart_p_1st.wppl $cost "gop" "speaker"> "speak_nonu_apart_gop/aug_gop_$cost.txt"
webppl noneven_apart_p_1st.wppl $cost "nogop" "speaker"> "speak_nonu_apart_nogop/aug_nogop_$cost.txt"
webppl noneven_apart_p_1st.wppl $cost "prob" "speaker"> "speak_nonu_apart_prob/aug_prob_$cost.txt"
done
cat nonu_aug_gop/aug_gop_*.txt > nonu_aug_gop/aug_gop.txt
cat nonu_aug_nogop/aug_nogop_*.txt > nonu_aug_nogop/aug_nogop.txt
cat nonu_aug_prob/aug_prob_*.txt > nonu_aug_prob/aug_prob.txt

cat nonu_apart_gop/aug_gop_*.txt > nonu_apart_gop/aug_gop.txt
cat nonu_apart_nogop/aug_nogop_*.txt > nonu_apart_nogop/aug_nogop.txt
cat nonu_apart_prob/aug_prob_*.txt > nonu_apart_prob/aug_prob.txt

cat speak_nonu_aug_gop/aug_gop_*.txt > speak_nonu_aug_gop/aug_gop.txt
cat speak_nonu_aug_nogop/aug_nogop_*.txt > speak_nonu_aug_nogop/aug_nogop.txt
cat speak_nonu_aug_prob/aug_prob_*.txt > speak_nonu_aug_prob/aug_prob.txt

cat speak_nonu_apart_gop/aug_gop_*.txt > speak_nonu_apart_gop/aug_gop.txt
cat speak_nonu_apart_nogop/aug_nogop_*.txt > speak_nonu_apart_nogop/aug_nogop.txt
cat speak_nonu_apart_prob/aug_prob_*.txt > speak_nonu_apart_prob/aug_prob.txt

python parse_results.py nonu_aug_gop/aug_gop.txt nonu_gop nonu_aug_gop.csv
python parse_results.py nonu_aug_nogop/aug_nogop.txt nonu_nogop nonu_aug_nogop.csv
python parse_results.py nonu_aug_prob/aug_prob.txt nonu_prob nonu_aug_prob.csv

python parse_results.py nonu_apart_gop/aug_gop.txt nonu_gop nonu_apart_gop.csv
python parse_results.py nonu_apart_nogop/aug_nogop.txt nonu_nogop nonu_apart_nogop.csv
python parse_results.py nonu_apart_prob/aug_prob.txt nonu_prob nonu_apart_prob.csv

python parse_speaker_results.py speak_nonu_aug_gop/aug_gop.txt nonu_gop speak_nonu_aug_gop.csv
python parse_speaker_results.py speak_nonu_aug_nogop/aug_nogop.txt nonu_nogop speak_nonu_aug_nogop.csv
python parse_speaker_results.py speak_nonu_aug_prob/aug_prob.txt nonu_prob speak_nonu_aug_prob.csv

python parse_speaker_results.py speak_nonu_apart_gop/aug_gop.txt nonu_gop speak_nonu_apart_gop.csv
python parse_speaker_results.py speak_nonu_apart_nogop/aug_nogop.txt nonu_nogop speak_nonu_apart_nogop.csv
python parse_speaker_results.py speak_nonu_apart_prob/aug_prob.txt nonu_prob speak_nonu_apart_prob.csv
