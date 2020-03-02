for cost in 0.0 0.25 0.5 0.75 1
do
webppl irrational_speaker.wppl $cost "gop" "speaker" > "irr_speaker_gop/irr_speaker_gop_$cost.txt"
webppl irrational_speaker.wppl $cost "nogop" "speaker" > "irr_speaker_nogop/irr_speaker_nogop_$cost.txt"
webppl irrational_speaker.wppl $cost "gop" > "speaker_bias_gop/speaker_bias_gop_$cost.txt"
webppl irrational_speaker.wppl $cost "nogop" > "speaker_bias_nogop/speaker_bias_nogop_$cost.txt"
webppl irrational_speaker.wppl $cost "prob" > "speaker_bias_prob/speaker_bias_prob_$cost.txt"
done
cat irr_speaker_gop/irr_speaker_gop_*.txt > irr_speaker_gop/irr_speaker_gop.txt
cat irr_speaker_nogop/irr_speaker_nogop_*.txt > irr_speaker_nogop/irr_speaker_nogop.txt
cat speaker_bias_gop/speaker_bias_gop_*.txt > speaker_bias_gop/speaker_bias_gop.txt
cat speaker_bias_nogop/speaker_bias_nogop_*.txt > speaker_bias_nogop/speaker_bias_nogop.txt
cat speaker_bias_prob/speaker_bias_prob_*.txt > speaker_bias_prob/speaker_bias_prob.txt
python parse_irr_speaker_results.py irr_speaker_gop/irr_speaker_gop.txt gop irr_speaker_gop.csv
python parse_irr_speaker_results.py irr_speaker_nogop/irr_speaker_nogop.txt nogop irr_speaker_nogop.csv
python parse_results.py speaker_bias_gop/speaker_bias_gop.txt speaker_bias_gop speaker_bias_gop.csv
python parse_results.py speaker_bias_nogop/speaker_bias_nogop.txt speaker_bias_nogop speaker_bias_nogop.csv
python parse_results.py speaker_bias_prob/speaker_bias_prob.txt speaker_bias_prob speaker_bias_prob.csv