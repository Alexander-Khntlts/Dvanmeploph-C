#--> Author's Info
Author    = 'Dapunta Khurayra X'
Developer = 'Denventa Ferly Afriliyan'
Facebook  = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Instagram = 'Instagram.com/afriliyanferlly_shishigami'

#--> oImprt Module
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
    print('   %s%s________                                    __'%(sp,M))          
    print('  %s%s\______ \   ____   _______  __ ____   _____/  |______'%(sp,M,M))   
    print(' %s%s |    |  \_/ __ \ /    \  \/ // __ \ /    \   __\__  \'%(sp,M,M))  
    print('%s%s |    `   \  ___/|   |  \   /\  ___/|   |  \  |  / __ \_'%(sp,M))
    print('%s%s/_______  /\___  >___|  /\_/  \___  >___|  /__| (____  /'%(sp,M))
    print('   %s%sMulti Brute Force Facebook %s0.1 By Denventa/n'%(sp,P,U))
    print('       %s%s─────────────── %s• %sDenventa %s• %s───────────────\n%s'%(sp,Z,M,P,M,Z,P))

          
