import streamtologger
import logging

log_file = "log_test.log"

open(log_file, "w").close()
streamtologger.redirect(target=log_file, print_to_screen=False)
logging.basicConfig(filename=log_file, filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

a = 5
b = 0

logging.info(msg=f"\nA= {a}\nB= {b}\n")

try:
    c = a / b
except Exception as e:
    logging.error("Division by 0 test", exc_info=True)


