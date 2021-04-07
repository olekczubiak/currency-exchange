#!/bin/bash
# chmod +x this file to run!!!

echo -ne '#                          (4%)\r'
# rm html/* ### DEL OLD FILES
# sleep 1 
echo -ne '##                         (12%)\r'
echo -ne '######                     (25%)\r'
# python get_website.py ### DOWNLOAD 
echo -ne '#########                  (36%)\r'
echo -ne '############               (50%)\r'
# sleep 0.3
echo -ne '################           (68%)\r'
# sleep 0.2
echo -ne '##################         (75%)\r'
# sleep 0.3
echo -ne '########################   (100%)\r'
echo -ne '\n'


echo "TOPFX:"
python parse_topfx.py
echo "Liderwalut:"
python parse_liderwalut.py
echo "InternetowyKantor:"
python parse_internetowykantor.py
# read var
# echo $var
