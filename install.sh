clear
Red='\033[0;31m'
function display(){
	echo 
	echo -e $Red '                          ########   #######  ####  ######   #######   ##    ## #### ########            ###    ########  ########   '
  echo -e $Red '                          ##     ## ##     ##  ##  ##    ## ##     ##  ###   ##  ##     ##              ## ##   ##     ## ##     ##  '
  echo -e $Red '                          ##     ## ##     ##  ##  ##       ##     ##  ####  ##  ##     ##             ##   ##  ##     ## ##     ##  '
  echo -e $Red '                          ########  ##     ##  ##   ######  ##     ##  ## ## ##  ##     ##            ##     ## ########  ########   '
  echo -e $Red '                          ##        ##     ##  ##        ## ##     ##  ##  ####  ##     ##            ######### ##   ##   ##         '
  echo -e $Red '                          ##        ##     ##  ##  ##    ## ##     ##  ##   ###  ##     ##            ##     ## ##    ##  ##         '
  echo -e $Red '                          ##         #######  ####  ######   #######   ##    ## ####    ##   #######  ##     ## ##     ## ##    		 '
	echo -e $Red '------------------------------------------------------------------------------------------------------------------------------------------------------------------ '  
  echo -e $Red '| Developer: Kedar Parikh | Email: kedar@decryptingtechnology.com | Website: www.decryptingtechnology.com | YouTube Channel: www.youtube.com/DecryptingTechnology |'
  echo -e $Red '------------------------------------------------------------------------------------------------------------------------------------------------------------------ '
}

display

echo -e $Red '[+] Updating APT'
apt update -qq
clear
display
echo -e $Red '[✔]Updating APT'
echo ''
echo '[+] Installing Python3 and Pip3'
apt install python3
apt install python3-pip
clear
display
echo -e $Red '[✔]Updating APT'
echo -e $Red '[✔]Installing Python3 and Pip3'
echo ''
echo -e $Red '[+] Installing Python Libraries'
pip3 install scapy
pip3 install colorama
clear
display
echo -e $Red '[✔]Updating APT'
echo -e $Red '[✔]Installing Python3 and Pip3'
echo -e $Red '[✔]Installing Python Libraries'
echo ''
echo '[+] Creating Terminal Shortcut'
path=`pwd`
echo 'alias poisonit="'python3 $path'"/poisonit.py' >> ~/.bashrc
clear
display
echo -e $Red '[✔]Updating APT'
echo -e $Red '[✔]Installing Python3 and Pip3'
echo -e $Red '[✔]Installing Python Libraries'
echo -e $Red '[✔]Creating Terminal Shortcut'
echo -e $Red 'Installation Complete!'
echo -e $Red 'Note: Restart the terminal after installation'
echo -e $Red 'Note: Type poisonit to start the tool'
echo -e $Red 'Thank you for installing Poisonit'

