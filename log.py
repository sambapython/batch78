import logging
logging.info("strt the program")# it's already configured the default basic Config. It will not consider
# any config later
#NOTE: what ever the basic config writing it, make sure that will execute before executing any log message.
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt", format="%(asctime)s->%(levelname)s==>%(message)s")
n1=input("Entere a number:")
n2=input("Enter a numebr:")
logging.debug(f"before conversion: n1={n1}, n2={n2}")
try:
    n1=int(n1)
    n2=int(n2)
    logging.debug(f"after conversion: n1={n1}, n2={n2}")
    res=n1/n2
    print(f"result={res}")
    logging.debug(f"result={res}")
except ZeroDivisionError as err:
    logging.error("ERROR: %s"%err)
    print("expecting second number not equals to zero")
except ValueError as err:
    logging.error("ERROR: %s"%err)
    print("expecting only the digits.")
except Exception as err:
    logging.error("ERROR:some issue")
    print("ERROR: %s"%err)
logging.info("end")