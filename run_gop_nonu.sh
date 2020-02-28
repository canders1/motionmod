for cost in 0.0 0.25 0.5 0.75 1
do
webppl noneven_p_1st.wppl $cost "gop" > "nonu_aug_gop/aug_gop_$cost.txt"
done
cat nonu_aug_gop/aug_gop_*.txt > nonu_aug_gop/aug_gop.txt
python parse_results.py nonu_aug_gop/aug_gop.txt nonu_gop nonu_aug_gop.csv