webppl speaker_default.wppl "gop" "speaker" > "speaker_default_speaker_gop/speaker_default_speaker_gop.txt"
webppl speaker_default.wppl "nogop" "speaker" > "speaker_default_speaker_nogop/speaker_default_speaker_nogop.txt"
webppl speaker_default.wppl "prob" "speaker" > "speaker_default_speaker_prob/speaker_default_speaker_prob.txt"
webppl speaker_default.wppl "gop" > "speaker_default_gop/speaker_default_gop.txt"
webppl speaker_default.wppl "nogop" > "speaker_default_nogop/speaker_default_nogop.txt"
webppl speaker_default.wppl "prob" > "speaker_default_prob/speaker_default_prob.txt"

python parse_speaker_results.py speaker_default_speaker_gop/speaker_default_speaker_gop.txt gop speaker_default_speaker_gop.csv
python parse_speaker_results.py speaker_default_speaker_nogop/speaker_default_speaker_nogop.txt nogop speaker_default_speaker_nogop.csv
python parse_speaker_results.py speaker_default_speaker_prob/speaker_default_speaker_prob.txt prob speaker_default_speaker_prob.csv
python parse_results.py speaker_default_gop/speaker_default_gop.txt speaker_default_gop speaker_default_gop.csv
python parse_results.py speaker_default_nogop/speaker_default_nogop.txt speaker_default_nogop speaker_default_nogop.csv
python parse_results.py speaker_default_prob/speaker_default_prob.txt speaker_default_prob speaker_default_prob.csv