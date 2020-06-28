def abre_log():
    try:
        abre_log = open('log.txt', 'r')
        return abre_log
    except:
        abre_log = open('log.txt', 'w')
        
        abre_log = open('log.txt', 'a')
        prim_escrita = abre_log.write('{:-^80}\n'.format('HISTÓRICO DE JOGADORES'))

        abre_log = open('log.txt', 'r')
        return abre_log

def salva_nome(nome, email):
    arq_log = open('log.txt', 'a')
    esc_nome = arq_log.write("\nNome: {}\nEmail: {}\n\n".format(nome, email))
