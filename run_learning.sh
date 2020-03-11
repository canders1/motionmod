for cost in 0
do
webppl learning.wppl $cost 'test' > "learning_test/test_$cost.txt"
done
cat learning_test/test_*.txt > learning_test/learning_test.txt
python parse_learning.py learning_test/learning_test.txt learning_test/worlds.txt learning_test.tsv