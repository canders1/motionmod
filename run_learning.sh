for cost in 0.0 0.5 1
do
webppl learning.wppl $cost 'test' > "learning_test/test_$cost.txt"
done
cat learning_test/test_*.txt > learning_test/learning_test.txt
python parse_learning_results.py learning_test/learning_test.txt test learning_test.csv