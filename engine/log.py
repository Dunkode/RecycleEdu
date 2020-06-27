from datetime import date, datetime

def abre_log():
    try:
        abre_log = open('log.txt', 'r')
        return abre_log
    except:
        abre_log = open('log.txt', 'w')
        
        abre_log = open('log.txt', 'a')
        prim_escrita = abre_log.write('\033[1;34m\033[m{:-^80}\033[1;34m\033[m\n'.format('\033[1mHISTÓRICO DE PARTIDAS\033[m'))

        abre_log = open('log.txt', 'r')
        return abre_log



def salva_inicio():
    hora  = '{}:{}:{}'.format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    dia = '{}/{}/{}  {}'.format(date.today().day, date.today().month, date.today().year, hora)

    return dia

def salva_final():
    hora  = '{}:{}:{}'.format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    dia = '{}/{}/{}  {}'.format(date.today().day, date.today().month, date.today().year, hora)
    return dia

def salva_parti(nomes, palavra, erros, vencedor, inicio, fim):
    fim = salva_final()
    arq_log = open('log.txt', 'a')

    if vencedor == 1:
        jog_venc = ['\033[1;31mDesafiante\033[m', '\033[31m' + nomes[0] + '\033[m']
    elif vencedor == 2:
        jog_venc = ['\033[1;32mCompetidor \033[1;32m', '\033[32m' + nomes[1] + '\033[m']
    
    escrita = arq_log.write(('\033[34m' + '=' * 80 + '\033[m' ) + '\n')
    escrita = arq_log.write('\033[1;37mVencedor:\033[m  {} {}  \033[1m||\033[m  \033[1mPalavra: \033[m\033[1;34m{}\033[m  \033[1m||\033[m  \033[1;31mErros:\033[m \033[31m{}\033[m \n'.format(jog_venc[0], jog_venc[1], palavra, erros))
    escrita = arq_log.write('\033[1;34mComeço da partida: {}\033[m  \033[1m||\033[m  \033[36mFinal da partida: {}\033[m\n'.format(inicio, fim))
    escrita = arq_log.write(('\033[34m' + '=' * 80 + '\033[m') + '\n')


def mostra_hist():
    arq_log = open('log.txt', 'r')
    leitura = arq_log.read()
    return leitura
