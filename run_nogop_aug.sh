for cost in 0.0 0.25 0.5 0.75 1
do
webppl xnew_aug.wppl $cost "nogop" > "aug_nogop_$cost.txt"
done
cat aug_nogop_*.txt > aug_nogop.txt
python parse_results.py aug_nogop.txt nogop aug_nogop.csv