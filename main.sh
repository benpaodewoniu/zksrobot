set -eux
sprice="1.5"
bprice="1.8"
python ./main.py ${{secrets.MAIL_USERNAME}} ${{secrets.MAIL_PASSWORD}} ${{secrets.RECEIVER}} $sprice $bprice