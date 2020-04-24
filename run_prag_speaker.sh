for cost in 0.0 0.25 0.5 0.75 1
do
webppl sample_p_1st.wppl $cost 'prob' "pragspeaker"> "pragspeaker_prob/prob_$cost.txt"
webppl sample_p_1st.wppl $cost 'nogop' "pragspeaker"> "pragspeaker_nogop/nogop_$cost.txt"
webppl sample_p_1st.wppl $cost 'gop' "pragspeaker"> "pragspeaker_gop/gop_$cost.txt"

webppl sample_p_1st.wppl $cost 'prob' "pragspeakerdouble"> "pragspeaker_double_prob/prob_$cost.txt"
webppl sample_p_1st.wppl $cost 'nogop' "pragspeakerdouble"> "pragspeaker_double_nogop/nogop_$cost.txt"
webppl sample_p_1st.wppl $cost 'gop' "pragspeakerdouble"> "pragspeaker_double_gop/gop_$cost.txt"

webppl sample_p_1st.wppl $cost 'prob' "pragspeakerearly"> "pragspeaker_early_prob/prob_$cost.txt"
webppl sample_p_1st.wppl $cost 'nogop' "pragspeakerearly"> "pragspeaker_early_nogop/nogop_$cost.txt"
webppl sample_p_1st.wppl $cost 'gop' "pragspeakerearly"> "pragspeaker_early_gop/gop_$cost.txt"
done
cat pragspeaker_prob/prob_*.txt > pragspeaker_prob/prob.txt
cat pragspeaker_gop/gop_*.txt > pragspeaker_gop/gop.txt
cat pragspeaker_nogop/nogop_*.txt > pragspeaker_nogop/nogop.txt

cat pragspeaker_double_prob/prob_*.txt > pragspeaker_double_prob/prob.txt
cat pragspeaker_double_gop/gop_*.txt > pragspeaker_double_gop/gop.txt
cat pragspeaker_double_nogop/nogop_*.txt > pragspeaker_double_nogop/nogop.txt

cat pragspeaker_early_prob/prob_*.txt > pragspeaker_early_prob/prob.txt
cat pragspeaker_early_gop/gop_*.txt > pragspeaker_early_gop/gop.txt
cat pragspeaker_early_nogop/nogop_*.txt > pragspeaker_early_nogop/nogop.txt

python parse_speaker_results.py pragspeaker_prob/prob.txt prob pragspeaker_prob.csv
python parse_speaker_results.py pragspeaker_gop/gop.txt gop pragspeaker_gop.csv
python parse_speaker_results.py pragspeaker_nogop/nogop.txt nogop pragspeaker_nogop.csv

python parse_speaker_results.py pragspeaker_double_prob/prob.txt prob pragspeaker_double_prob.csv
python parse_speaker_results.py pragspeaker_double_gop/gop.txt gop pragspeaker_double_gop.csv
python parse_speaker_results.py pragspeaker_double_nogop/nogop.txt nogop pragspeaker_double_nogop.csv

python parse_speaker_results.py pragspeaker_early_prob/prob.txt prob pragspeaker_early_prob.csv
python parse_speaker_results.py pragspeaker_early_gop/gop.txt gop pragspeaker_early_gop.csv
python parse_speaker_results.py pragspeaker_early_nogop/nogop.txt nogop pragspeaker_early_nogop.csv