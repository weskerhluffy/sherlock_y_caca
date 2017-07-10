'''
Created on 08/07/2017

@author:
'''
import logging
import sys
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def sherlock_caca_core(mierdas):
    putos_alto = [0]
    putos_bajo = [0]
    
    logger_cagada.debug("las mierdas %s" % mierdas)
    
    for caca in range(1, len(mierdas)):
        putos_alto.append(max(mierdas[caca] - 1 + putos_bajo[caca - 1], abs(mierdas[caca] - mierdas[caca - 1]) + putos_alto[caca - 1]))
        logger_cagada.debug("comparando para bajo %s y %s, putos alto anterior %s mierdas anterior %s" % (putos_bajo[caca - 1], mierdas[caca - 1] - 1 + putos_alto[caca - 1], putos_alto[caca - 1], mierdas[caca - 1]))
        putos_bajo.append(max(putos_bajo[caca - 1], mierdas[caca - 1] - 1 + putos_alto[caca - 1]))
    
    logger_cagada.debug("putos altos %s" % putos_alto)
    logger_cagada.debug("putos bajos %s" % putos_bajo)
    
    max_caca = max(putos_alto[-1], putos_bajo[-1])
    
    return max_caca

def sherlock_caca_main():
    lineas = list(sys.stdin)
    
    for linea in lineas[2::2]:
        mierdas = [int(x) for x in linea.strip().split(" ")]
        resucaca = sherlock_caca_core(mierdas)
        
        logger_cagada.debug("cagada %s" % resucaca)
        print(resucaca)
    

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)

        sherlock_caca_main()
