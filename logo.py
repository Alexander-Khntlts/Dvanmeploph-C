#--> Author's Info
Author    = 'Dapunta Adyapaksi Ratya'
Developer = 'Denventa Ferly Afriliyan'
Facebook  = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Instagram = 'Instagram.com/afriliyanferlly_shishigami'
Version = '0.1'

#--> Import Module
import sys, time

#--> Style Warna
Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu

#--> Animasi
def urut(i,t):
    for e in i + '\n': sys.stdout.write(e); sys.stdout.flush(); time.sleep(t)

#--> Logo
def logo():
    sp = ' '*7
    print('     %s   ________                                            .__                .__              _________   '%(M))    
    print('     %s   \______ \___  _______    ____   _____   ____ ______ |  |   ____ ______ |  |__           \_   ___ \ '%(M))
    print('     %s    |    |  \  \/ /\__  \  /    \ /     \_/ __ \\____ \|  |  /  _ \\____ \|  |  \   %s______ /    \  \/  '%(M,P,M))
    print('     %s    |    `   \   /  / __ \|   |  \  Y Y  \  ___/|  |_> >  |_(  <_> )  |_> >   Y  \ %s/_____/ \     \____  '%(M,P,M)) 
    print('     %s   /_______  /\_/  (____  /___|  /__|_|  /\___  >   __/|____/\____/|   __/|___|  /          \______  /  '%(M))
    print('     %s           \/           \/     \/      \/     \/|__|               |__|        \/                  \/  '%(M))
    print('     %s Author %s: %sDapunta Adyapaksi Ratya  %s Developer %s: %sDenventa Afriliyan Ferly  '%(P,K,M,P,K,M))
