for cost in 0.0 0.25 0.5 0.75 1
do
webppl xnew_prob_aug.wppl $cost > "prob_$cost.txt"
done