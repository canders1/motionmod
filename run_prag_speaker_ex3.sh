for cost in 0.0 0.5 1
do
webppl ex3.wppl $cost 'prob' "pragspeaker"> "ex3_prob/prob_$cost.txt"
webppl ex3.wppl $cost 'nogop' "pragspeaker"> "ex3_nogop/nogop_$cost.txt"
webppl ex3.wppl $cost 'gop' "pragspeaker"> "ex3_gop/gop_$cost.txt"

webppl ex3.wppl $cost 'prob' "pragspeakerdouble"> "ex3_double_prob/prob_$cost.txt"
webppl ex3.wppl $cost 'nogop' "pragspeakerdouble"> "ex3_double_nogop/nogop_$cost.txt"
webppl ex3.wppl $cost 'gop' "pragspeakerdouble"> "ex3_double_gop/gop_$cost.txt"

webppl ex3.wppl $cost 'prob' "pragspeakerearly"> "ex3_early_prob/prob_$cost.txt"
webppl ex3.wppl $cost 'nogop' "pragspeakerearly"> "ex3_early_nogop/nogop_$cost.txt"
webppl ex3.wppl $cost 'gop' "pragspeakerearly"> "ex3_early_gop/gop_$cost.txt"
done
cat ex3_prob/prob_*.txt > ex3_prob/prob.txt
cat ex3_gop/gop_*.txt > ex3_gop/gop.txt
cat ex3_nogop/nogop_*.txt > ex3_nogop/nogop.txt

cat ex3_double_prob/prob_*.txt > ex3_double_prob/prob.txt
cat ex3_double_gop/gop_*.txt > ex3_double_gop/gop.txt
cat ex3_double_nogop/nogop_*.txt > ex3_double_nogop/nogop.txt

cat ex3_early_prob/prob_*.txt > ex3_early_prob/prob.txt
cat ex3_early_gop/gop_*.txt > ex3_early_gop/gop.txt
cat ex3_early_nogop/nogop_*.txt > ex3_early_nogop/nogop.txt

python parse_speaker_results.py ex3_prob/prob.txt prob ex3_prob.csv
python parse_speaker_results.py ex3_gop/gop.txt gop ex3_gop.csv
python parse_speaker_results.py ex3_nogop/nogop.txt nogop ex3_nogop.csv

python parse_speaker_results.py ex3_double_prob/prob.txt prob ex3_double_prob.csv
python parse_speaker_results.py ex3_double_gop/gop.txt gop ex3_double_gop.csv
python parse_speaker_results.py ex3_double_nogop/nogop.txt nogop ex3_double_nogop.csv

python parse_speaker_results.py ex3_early_prob/prob.txt prob ex3_early_prob.csv
python parse_speaker_results.py ex3_early_gop/gop.txt gop ex3_early_gop.csv
python parse_speaker_results.py ex3_early_nogop/nogop.txt nogop ex3_early_nogop.csv