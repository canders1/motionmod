for cost in 0.0 0.25 0.5 0.75 1
do
webppl sample_wp.wppl $cost "gop" > "sample_wp_gop/sample_wp_gop_$cost.txt"
webppl sample_wp.wppl $cost "nogop" > "sample_wp_nogop/sample_wp_nogop_$cost.txt"
webppl sample_wp.wppl $cost "prob" > "sample_wp_prob/sample_wp_prob_$cost.txt"
webppl sample_wp.wppl $cost "gop" "speaker" > "speaker_sample_wp_gop/speaker_sample_wp_gop_$cost.txt"
webppl sample_wp.wppl $cost "nogop" "speaker" > "speaker_sample_wp_nogop/speaker_sample_wp_nogop_$cost.txt"
webppl sample_wp.wppl $cost "prob" "speaker"> "speaker_sample_wp_prob/speaker_sample_wp_prob_$cost.txt"
done
cat sample_wp_gop/sample_wp_gop_*.txt > sample_wp_gop/sample_wp_gop.txt
cat sample_wp_nogop/sample_wp_nogop_*.txt > sample_wp_nogop/sample_wp_nogop.txt
cat sample_wp_prob/sample_wp_prob_*.txt > sample_wp_prob/sample_wp_prob.txt
cat speaker_sample_wp_gop/speaker_sample_wp_gop_*.txt > speaker_sample_wp_gop/speaker_sample_wp_gop.txt
cat speaker_sample_wp_nogop/speaker_sample_wp_nogop_*.txt > speaker_sample_wp_nogop/speaker_sample_wp_nogop.txt
cat speaker_sample_wp_prob/speaker_sample_wp_prob_*.txt > speaker_sample_wp_prob/speaker_sample_wp_prob.txt
python parse_results.py sample_wp_gop/sample_wp_gop.txt gop sample_wp_gop.csv
python parse_results.py sample_wp_nogop/sample_wp_nogop.txt nogop sample_wp_nogop.csv
python parse_results.py sample_wp_prob/sample_wp_prob.txt prob sample_wp_prob.csv
python parse_speaker_sample_wp_results.py speaker_sample_wp_gop/speaker_sample_wp_gop.txt speaker_sample_wp_gop speaker_sample_wp_gop.csv
python parse_speaker_sample_wp_results.py speaker_sample_wp_nogop/speaker_sample_wp_nogop.txt speaker_sample_wp_nogop speaker_sample_wp_nogop.csv
python parse_speaker_sample_wp_results.py speaker_sample_wp_prob/speaker_sample_wp_prob.txt speaker_sample_wp_prob speaker_sample_wp_prob.csv