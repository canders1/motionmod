for cost in 0.0 0.25 0.5 0.75 1
do
webppl sample_p_1st.wppl $cost "gop" > "aug_gop/aug_gop_$cost.txt"
done
cat aug_gop/aug_gop_*.txt > aug_gop/aug_gop.txt
python parse_results.py aug_gop/aug_gop.txt gop aug_gop.csv