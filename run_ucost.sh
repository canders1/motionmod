webppl sample_p_1st_ucost.wppl "gop" > "ucost_aug_gop.txt"
python ucost_parse_results.py ucost_aug_gop.txt ucost_gop ucost_aug_gop.csv
webppl sample_p_1st_ucost.wppl "nogop" > "ucost_aug_nogop.txt"
python ucost_parse_results.py ucost_aug_nogop.txt ucost_nogop ucost_aug_nogop.csv