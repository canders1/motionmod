for cost in 0.0 0.25 0.5 0.75 1
do
webppl sample_p_1st.wppl $cost "nogop" > "aug_nogop/aug_nogop_$cost.txt"
done
cat aug_nogop/aug_nogop_*.txt > aug_nogop/aug_nogop.txt
python parse_results.py aug_nogop/aug_nogop.txt nogop aug_nogop.csv