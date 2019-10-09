for cost in 0.0 0.25 0.5 0.75 1
do
webppl sample_p_1st.wppl $cost 'prob' "speaker"> "speaker_aug_prob/prob_$cost.txt"
webppl sample_p_1st.wppl $cost 'nogop' "speaker"> "speaker_aug_nogop/nogop_$cost.txt"
webppl sample_p_1st.wppl $cost 'gop' "speaker"> "speaker_aug_gop/gop_$cost.txt"
done
cat speaker_aug_prob/prob_*.txt > speaker_aug_prob/aug_prob.txt
cat speaker_aug_gop/gop_*.txt > speaker_aug_gop/aug_gop.txt
cat speaker_aug_nogop/nogop_*.txt > speaker_aug_nogop/aug_nogop.txt
python parse_speaker_results.py speaker_aug_prob/aug_prob.txt prob speaker_aug_prob.csv
python parse_speaker_results.py speaker_aug_gop/aug_gop.txt gop speaker_aug_gop.csv
python parse_speaker_results.py speaker_aug_nogop/aug_nogop.txt nogop speaker_aug_nogop.csv